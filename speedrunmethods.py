from pvz import *
from pvz.extra import *
import time

def PlantWhenAvailable(seed_number, plant_cost, square): 
    """
    Waits until a seed is available in the seed bank, then plants it
    Params:

    seed_number: The slot of the plant you want to place
    plant_cost: The sun cost of the plant you are placing
    square: (x,y) coordinates of the square you want the plant on
    """
    slots_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x144)
    times_used = ReadMemory("int", slots_offset + 0x24+seed_number*0x50)
    while(True):
        Sleep(1)
        if(ReadMemory("int", slots_offset + 0x24+seed_number*0x50) != times_used):
            break
        collected_items = 0
        items_offset = ReadMemory("int", 0x6A9EC0, 0x768, 0xE4)
        items_count = ReadMemory("int", 0x6A9EC0, 0x768, 0xF4)
        for i in range(items_count):
            collected = ReadMemory("bool", items_offset + 0x50 + 0xD8 * i)
            item_type = ReadMemory("int", items_offset + 0x58 + 0xD8 * i)
            if(collected and (item_type == 4 or item_type == 5)):
                collected_items += 25
        if(ReadMemory("int", 0x6A9EC0, 0x768, 0x5560) + collected_items >= plant_cost and ReadMemory("bool", slots_offset + 0x20+seed_number*0x50)):
                Card(seed_number,square)
@RunningInThread
def FastSun():
    """
    Call once the game_ui == 3.  
    This will make all sun from the sky as fast as possible
    """
    
    SunsFallen = -1
    while(game_ui() == 3 and ReadMemory("bool", 0x6A9EC0, 0x768, 0x5603)):
        if(ReadMemory("int", 0x6A9EC0,0x768,0x553c) != SunsFallen):
            SunsFallen += 1
            WriteMemory("int",min(425 + SunsFallen * 10, 950),0x6A9EC0,0x768,0x5538)
@RunningInThread
def FastPlants():
    """
    Call once game_ui == 3
    This makes all sunflowers have the fastest possible proudction.  
    It also makes all peashooters have the best possible cycles. 
    To add other plants, add extra numbers to the first plant type check. 
    """
    plants = []
    while(game_ui() == 3 and ReadMemory("bool", 0x6A9EC0, 0x768, 0x5603)):
        plants_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0xB0)
        plants_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0xAC)
        for i in range(plants_count_max):
            plant_dead = ReadMemory("bool", plants_offset + 0x141 + i * 0x14c)
            plant_squished = ReadMemory("bool", plants_offset + 0x142 + i * 0x14c)
            plant_type = ReadMemory("int", plants_offset + 0x24 + i * 0x14c)
            plant_row = ReadMemory("int", plants_offset + 0x1c + i * 0x14c)
            plant_col = ReadMemory("int", plants_offset + 0x28 + i * 0x14c)
            if(plant_type == 42):
                plant_row += 5
            if not plant_dead and not plant_squished and plant_type == 1 or plant_type == 9:
                
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
                    WriteMemory("int",300, plants_offset + 0x58 + i * 0x14c)
                else:
                    if(ReadMemory("int", plants_offset + 0x58 + i * 0x14c) > 2350 and ReadMemory("int", plants_offset + 0x58 + i * 0x14c) <= 2500):
                       WriteMemory("int", 2350,plants_offset + 0x58 + i * 0x14c) 
            elif not plant_dead and not plant_squished and (ReadMemory("int", 0x69F2C8 + plant_type * 0x24) == 1):
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
                    if(plant_type == 8 or plant_type == 24):
                        if(plant_col == 8):
                            WriteMemory("int",675, plants_offset + 0x8 + i * 0x14c)
                        else:
                            WriteMemory("int",44 + plant_col*80, plants_offset + 0x8 + i * 0x14c)
                    WriteMemory("int",0, plants_offset + 0x58 + i * 0x14c)
                if(ReadMemory("int", plants_offset + 0x58 + i * 0x14c) > ReadMemory("int", 0x69F2CC + plant_type * 0x24) - 15):
                    WriteMemory("int",ReadMemory("int", 0x69F2CC + plant_type * 0x24) - 15, plants_offset + 0x58 + i * 0x14c)


@RunningInThread
def thirtyFiveRule(waves):
    """
    All wave activations only require 35% of the wave to be hit.  
    Every wave also has the best possible auto-advance.  
    waves: The number of waves in the level
    """
    for i in range(1,waves):
        Prejudge(1,i)
        if(i % 10 == 9 or (i == 5 and ReadMemory("int",0x6a9ec0, 0x768, 0x5550) == 2)):
            continue
        WriteMemory("int",(int)(ReadMemory("int",0x6a9ec0, 0x768, 0x5598)*0.65), 0x6a9ec0, 0x768, 0x5594)
        WriteMemory("int",2499,0x6a9ec0, 0x768, 0x55A0)
        WriteMemory("int",2499,0x6a9ec0, 0x768, 0x559C)


# pls


def WriteZombies(zombie_Types,zombie_rows=[0],zombies_speed=[0]):
    """
    Call this method at the start of each wave.  
    Sets all zombies to the rows you input as well as the best possible x positions.  
    Warning: Must input zombies in order of their types(all normals first, all cones, etc...)
    """
    j = 0
    while(j < len(zombie_Types)):
        zombies_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)
        zombies_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
        for i in range(zombies_count_max):
            zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
            zombie_age = ReadMemory("int", 0x6A9EC0, 0x768, 0x90, 0x60 + 0x15C * i) 
            if not zombie_dead and zombie_age <= 50 and ReadMemory("int", zombies_offset + 0x24 + i * 0x15c) == zombie_Types[j]:
                if(zombie_Types[j] == 15):
                    WriteMemory("int", 441, zombies_offset + 0x68 + i * 0x15c)
                if(zombie_Types[j] == 8):
                    WriteMemory("int", 311, zombies_offset + 0x68 + i * 0x15c)
                if(zombie_rows[0] != 0):
                    WriteMemory("int",zombie_rows[j] - 1, zombies_offset + 0x1c + i * 0x15c)
                    WriteMemory("int",303004+10000*(zombie_rows[j]-1), zombies_offset + 0x20 + i * 0x15c)
                    if(read_memory("int", 0x6A9EC0, 0x768, 0x554C) in (2,3,4)):
                        WriteMemory("float",50+(zombie_rows[j] - 1)*85, zombies_offset + 0x30 + i * 0x15c)
                    else:   
                        WriteMemory("float",50+(zombie_rows[j] - 1)*100, zombies_offset + 0x30 + i * 0x15c)
                    if(read_memory("int", 0x6A9EC0, 0x768, 0x554C) in (2,3)):
                        asm_init()
                        asm_mov_exx("edi", zombies_offset + i * 0x15C)
                        asm_call(0x00524370)
                        asm_ret()
                        asm_code_inject_safely()    
                if(zombies_speed[0] != 0):
                    WriteMemory("float",zombies_speed[j], zombies_offset + 0x34 + i * 0x15c)
                    if(zombies_speed[j] > 0.3 and zombies_speed[j] < 0.375):
                        WriteMemory("int",15,zombies_offset + 0x40 + i * 0x15c)
                    elif (zombies_speed[j] > 0.23 and zombies_speed[j] < 0.3):
                        WriteMemory("int",12,zombies_offset + 0x40 + i * 0x15c)
                    asm_init()
                    asm_mov_exx("esi", zombies_offset + i * 0x15C)
                    asm_call(0x0052F050)
                    asm_ret()
                    asm_code_inject_safely()
                j += 1
                if(j == len(zombie_Types)):
                    break
def SetGraves(grave_locations):
    """
    Sets the grave locations for a level as desired.  
    Note: currently will not work if there are other grid items, such as a rake
    grave_locations: List of tuples, 
    Ex: [(2,5),(3,6)] sets 2 graves to row 2 col 5 and row 3 col 6
    """
    grave_offset = ReadMemory("unsigned int",0x6A9EC0,0x768,0x11C)
    for i in range(len(grave_locations)):
        WriteMemory("int",grave_locations[i][0]-1,grave_offset+0x14+i*0xEC)
        WriteMemory("int",grave_locations[i][1]-1,grave_offset+0x10+i*0xEC)
        WriteMemory("int",301004+10000*(grave_locations[i][0]-1), grave_offset+0x1C+i*0xEC)
@RunningInThread
def SetAmbushZombies(zombie_coords):
    ''' Set the ambush zombies spawns to the correct type and coordinates
    Only call when final wave is reached.  
    zombie_coords: List of Coords([(3,9),(4,9),(3,8)])
    '''
    if(ReadMemory("int", 0x6A9EC0, 0x768, 0x5574) == 0):
        print("called SetAmbushZombies too early or too late!")
        return
    while(ReadMemory("int", 0x6A9EC0, 0x768, 0x5574) != 0):
        Sleep(1)
    j = 0
    for k in range(2):
        while(j < len(zombie_coords)):
            zombies_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)
            zombies_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
            for i in range(zombies_count_max):
                zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
                if not zombie_dead and ReadMemory("int", 0x6A9EC0, 0x768, 0x90, 0x60 + 0x15C * i) <= 50 and ReadMemory("int", zombies_offset + 0x24 + i * 0x15c) != 20:
                    if(game_scene == 2 or game_scene == 3):
                        WriteMemory("float", -65 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                    else:
                        WriteMemory("float", -55 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                        SetBungees(zombie_coords)
                    WriteMemory("float", 50+(zombie_coords[j][0] - 1)*85, zombies_offset + 0x30 + i * 0x15c)
                    WriteMemory("int",zombie_coords[j][0] - 1, zombies_offset + 0x1c + i * 0x15c)
                    WriteMemory("int",303004+10000*(zombie_coords[j][0]-1), zombies_offset + 0x20 + i * 0x15c)
                    j += 1
                    if(j == len(zombie_coords)):
                        break
def SetBungees(zombie_coords):
    ''' Set the bungee zombies spawns to the correct coordinates
    zombie_coords: List of Coords([(3,9),(4,9),(3,8)])
    '''
    j = 0
    while(j < len(zombie_coords)):
            zombies_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)
            zombies_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
            for i in range(zombies_count_max):
                zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
                if not zombie_dead and ReadMemory("int", 0x6A9EC0, 0x768, 0x90, 0x60 + 0x15C * i) <= 50 and ReadMemory("int", zombies_offset + 0x24 + i * 0x15c) == 20:
                    WriteMemory("float", -40 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                    WriteMemory("float", 50+(zombie_coords[j][0] - 1)*85, zombies_offset + 0x30 + i * 0x15c)
                    WriteMemory("int",zombie_coords[j][0] - 1, zombies_offset + 0x1c + i * 0x15c)
                    WriteMemory("int",zombie_coords[j][1] - 1, zombies_offset + 0x80 + i * 0x15c)
                    WriteMemory("int",301004+10000*(zombie_coords[j][0]-1), zombies_offset+0x20+i*0x15C)
                    j += 1
                    if(j == len(zombie_coords)):
                        break
def SetConveyorPlant(slot, new_plant):
    """
    Sets a conveyor belt plant to a new plant
    Params: 
    slot: slot number of the plant to replace
    new_plant: ID of the new plant
    """
    while(ReadMemory("int",0x6A9EC0, 0x768, 0x144, 0xC + slot*0x50) == -1):
        Sleep(0.1)
    WriteMemory("int",new_plant, 0x6A9EC0, 0x768, 0x144, 0xC + slot*0x50)
def PlantConveyorPlant(slot, coords):
    """
    Plants a conveyor belt plant
    slot: slot number of the plant to place
    coords: coordinates of where the plant should be planted
    """
    while(ReadMemory("int",0x6A9EC0, 0x768, 0x144, 0xC + slot*0x50) == -1 or ReadMemory("int", 0x6A9EC0, 0x768, 0x144, 0x8 + slot*0x50)+50*(slot-1) > 499):
        Sleep(0.1)
    safe_click()
    LeftClick(ReadMemory("int", 0x6A9EC0, 0x768, 0x144, 0x8 + slot*0x50)+105+50*(slot-1),12)
    ClickGrid(coords)
def SetBungeeBlitzZombies(zombie_coords):
    j = 0
    while(j < len(zombie_coords)):
            zombies_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)
            zombies_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
            for i in range(zombies_count_max):
                zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
                if not zombie_dead and ReadMemory("int", 0x6A9EC0, 0x768, 0x90, 0x60 + 0x15C * i) <= 50 and ReadMemory("int", zombies_offset + 0x24 + i * 0x15c) != 20:
                    if(game_scene == 2 or game_scene == 3):
                        WriteMemory("float", -65 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                    else:
                        WriteMemory("float", -55 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                        SetBungees(zombie_coords)
                    WriteMemory("float", 50+(zombie_coords[j][0] - 1)*85, zombies_offset + 0x30 + i * 0x15c)
                    WriteMemory("int",zombie_coords[j][0] - 1, zombies_offset + 0x1c + i * 0x15c)
                    j += 1
                    if(j == len(zombie_coords)):
                        break
    