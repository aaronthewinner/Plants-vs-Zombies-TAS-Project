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
    j = 0 # 1 frame where enough sun is recorded incorrectly so counter is needed
    slots_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x144)
    while(True):
        Sleep(1)
        collected_items = 0
        items_offset = ReadMemory("int", 0x6A9EC0, 0x768, 0xE4)
        items_count = ReadMemory("int", 0x6A9EC0, 0x768, 0xF4)
        for i in range(items_count):
            collected = ReadMemory("bool", items_offset + 0x50 + 0xD8 * i)
            item_type = ReadMemory("int", items_offset + 0x58 + 0xD8 * i)
            if(collected and item_type == 4):
                collected_items += 25
        if(ReadMemory("int", 0x6A9EC0, 0x768, 0x5560) + collected_items >= plant_cost):
            j += 1
            if(j >= 10 and ReadMemory("bool", slots_offset + 0x20+seed_number*0x50)):
                Card(seed_number,square)
                break
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
            if not plant_dead and not plant_squished and plant_type == 1:
                
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
                    WriteMemory("int",300, plants_offset + 0x58 + i * 0x14c)
                else:
                    if(ReadMemory("int", plants_offset + 0x58 + i * 0x14c) > 2350 and ReadMemory("int", plants_offset + 0x58 + i * 0x14c) <= 2500):
                       WriteMemory("int", 2350,plants_offset + 0x58 + i * 0x14c) 
            elif not plant_dead and not plant_squished and (ReadMemory("int", 0x69F2C8 + plant_type * 0x24) == 1):
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
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
        if(i % 10 == 9):
            break
        WriteMemory("int",(int)(ReadMemory("int",0x6a9ec0, 0x768, 0x5598)*0.65), 0x6a9ec0, 0x768, 0x5594)
        WriteMemory("int",2499,0x6a9ec0, 0x768, 0x55A0)
        WriteMemory("int",2499,0x6a9ec0, 0x768, 0x559C)


# pls


def WriteZombies(zombie_Types,zombie_rows=[0]):
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
            if not zombie_dead and ReadMemory("int", zombies_offset + 0x8 + i * 0x15c) > 750 and ReadMemory("int", zombies_offset + 0x24 + i * 0x15c) == zombie_Types[j]:
                if(zombie_Types[j] == 3):
                    WriteMemory("float",869, zombies_offset + 0x2c + i * 0x15c)
                elif(zombie_Types[j] != 1):
                    if(read_memory("int", 0x6A9EC0, 0x768, 0x557C) % 10 == 0):
                        WriteMemory("float",819, zombies_offset + 0x2c + i * 0x15c)
                    else:
                        WriteMemory("float",779, zombies_offset + 0x2c + i * 0x15c)
                if(zombie_rows[0] != 0):
                    WriteMemory("int",zombie_rows[j] - 1, zombies_offset + 0x1c + i * 0x15c)
                    if(game_scene == 2 or game_scene == 3 or game_scene == 4):
                        WriteMemory("float",50+(zombie_rows[j] - 1)*85, zombies_offset + 0x30 + i * 0x15c)
                    else:   
                        WriteMemory("float",50+(zombie_rows[j] - 1)*100, zombies_offset + 0x30 + i * 0x15c)
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
        Sleep(0.1)
    j = 0
    while(j < len(zombie_coords)):
            zombies_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)
            zombies_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
            for i in range(zombies_count_max):
                zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
                if not zombie_dead and ReadMemory("int", zombies_offset + 0x8 + i * 0x15c) <= 680 and ReadMemory("int", zombies_offset + 0x24 + i * 0x15c) != 20:
                    if(game_scene == 2 or game_scene == 3):
                        WriteMemory("float", -65 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                    else:
                        WriteMemory("float", -55 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                    WriteMemory("float", 50+(zombie_coords[j][0] - 1)*85, zombies_offset + 0x30 + i * 0x15c)
                    WriteMemory("int",zombie_coords[j][0] - 1, zombies_offset + 0x1c + i * 0x15c)
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
                if not zombie_dead and ReadMemory("int", zombies_offset + 0x8 + i * 0x15c) <= 680 and ReadMemory("int", zombies_offset + 0x24 + i * 0x15c) == 20:
                    WriteMemory("float", -40 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                    WriteMemory("float", 50+(zombie_coords[j][0] - 1)*85, zombies_offset + 0x30 + i * 0x15c)
                    WriteMemory("int",zombie_coords[j][0] - 1, zombies_offset + 0x1c + i * 0x15c)
                    WriteMemory("int",zombie_coords[j][1] - 1, zombies_offset + 0x80 + i * 0x15c)
                    j += 1
                    if(j == len(zombie_coords)):
                        break

    
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
Sleep(600)
select_seeds_and_lets_rock((0,1,4,7,20,28,29,32))
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150] = 2
waves[151] = -1
waves[200] = 0
waves[201] = 0
waves[202] = -1
waves[300] = 0
waves[301] = 0
waves[302] = 0
waves[303] = -1
waves[350] = 0
waves[351] = 0
waves[352] = 0
waves[353] = -1
waves[400] = 0
waves[401] = 0
waves[402] = 0
waves[403] = -1
##waves[451] = 0
##waves[452] = 0
##waves[453] = 0
##waves[454] = 0
##waves[455] = 0
##waves[456] = 0
##waves[455] = 1
##waves[458] = 2
##waves[459] = 20
##waves[460] = -1
waves = tuple(waves)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(10)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
PlantWhenAvailable(2,50,(2,1))
PlantWhenAvailable(2,50,(3,1))
PlantWhenAvailable(2,50,(4,1))
Prejudge(1,1)
WriteZombies([0])
PlantWhenAvailable(2,50,(5,1))
Prejudge(1,2)
WriteZombies([0],[1])
PlantWhenAvailable(1,100,(1,5))
PlantWhenAvailable(2,50,(2,2))
Prejudge(1,3)
WriteZombies([0],[5])
#PlantWhenAvailable(2,50,(3,2))
PlantWhenAvailable(1,100,(5,5))
Prejudge(1,4)
WriteZombies([2],[3])
PlantWhenAvailable(5,125,(3,5))
Prejudge(1,5)
WriteZombies([0,0],[1,5])
PlantWhenAvailable(8, 100,(1,4))
Prejudge(1,6)
SetBungees([(3,9)])
Prejudge(1,7)
WriteZombies([0,0,0],[1,1,5])
PlantWhenAvailable(7,125,(3,5))
Prejudge(1,8)
WriteZombies([0,0,0],[1,5,5])
PlantWhenAvailable(8,100,(5,4))
Prejudge(1,9)
WriteZombies([0,0,0],[1,1,5])
PlantWhenAvailable(8,100,(1,3))
Prejudge(1,10)
WriteZombies([0,0,0,0,1,2],[4,4,4,4,4,4])
SetBungees([(4,8)])
SetAmbushZombies([(4,6),(4,7)])
Prejudge(550,10)
PlantWhenAvailable(5,125,(4,5))
while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)









