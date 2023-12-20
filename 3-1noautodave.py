from pvz import ReadMemory, WriteMemory, SetZombies, Prejudge, game_ui, Sleep, AutoCollect, Card,RunningInThread,select_seeds_and_lets_rock, update_game_scene,use_shovel
from pvz.core import seeds_string
from pvz.core import zombies_string
import time
def PlantWhenAvailable(SeedNumber, plant_cost, square):
    j = 0
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
            if(j >= 10 and ReadMemory("bool", slots_offset + 0x70+SeedNumber*0x50)):
                Card(SeedNumber+1,square)
                break
@RunningInThread
def FastSun():
    SunsFallen = -1
    while(game_ui() == 3 and ReadMemory("bool", 0x6A9EC0, 0x768, 0x5603)):
        if(ReadMemory("int", 0x6A9EC0,0x768,0x553c) != SunsFallen):
            SunsFallen += 1
            WriteMemory("int",min(425 + SunsFallen * 10, 950),0x6A9EC0,0x768,0x5538)
@RunningInThread
def FastPlants():
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
            elif not plant_dead and not plant_squished and (plant_type == 0 or plant_type == 6):
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
                    WriteMemory("int",0, plants_offset + 0x58 + i * 0x14c)
                if(ReadMemory("int", plants_offset + 0x58 + i * 0x14c) > 135):
                    WriteMemory("int",135, plants_offset + 0x58 + i * 0x14c)
@RunningInThread
def thirtyFiveRule():
    for i in range(1,9):
        Prejudge(1,i)
        WriteMemory("int",(int)(ReadMemory("int",0x6a9ec0, 0x768, 0x5598)*0.65), 0x6a9ec0, 0x768, 0x5594)
        WriteMemory("int",2499,0x6a9ec0, 0x768, 0x55A0)
        WriteMemory("int",2499,0x6a9ec0, 0x768, 0x559C)

def WriteZombies(zombie_Types,zombie_rows=[0],zombies_speed=[0]):
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
                    if(ReadMemory("int", 0x6A9EC0, 0x768, 0x557C) % 10 == 0):
                        WriteMemory("float",819, zombies_offset + 0x2c + i * 0x15c)
                    else:
                        WriteMemory("float",779, zombies_offset + 0x2c + i * 0x15c)
                if(zombie_rows[0] != 0):
                    WriteMemory("int",zombie_rows[j] - 1, zombies_offset + 0x1c + i * 0x15c)
                    WriteMemory("float",50+(zombie_rows[j] - 1)*100, zombies_offset + 0x30 + i * 0x15c)
                if(zombies_speed[0] != 0):
                    WriteMemory("float",zombies_speed[j], zombies_offset + 0x34 + i * 0x15c)
                    if(zombies_speed[j] > 0.3 and zombies_speed[j] < 0.375):
                        WriteMemory("int",15,zombies_offset + 0x40 + i * 0x15c)
                j += 1
                if(j == len(zombie_Types)):
                    break
@RunningInThread
def SetAmbushZombies(zombie_coords):
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
                if not zombie_dead and ReadMemory("int", zombies_offset + 0x8 + i * 0x15c) <= 680:
                    WriteMemory("float", -40 + 80*zombie_coords[j][1], zombies_offset + 0x2c + i * 0x15c)
                    WriteMemory("float", 50+(zombie_coords[j][0] - 1)*85, zombies_offset + 0x30 + i * 0x15c)
                    WriteMemory("int",zombie_coords[j][0] - 1, zombies_offset + 0x1c + i * 0x15c)
                    j += 1
                    if(j == len(zombie_coords)):
                        break

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
Sleep(310)
select_seeds_and_lets_rock([0,1,2,3,4,6,16,5])
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150] = 0
waves[151] = 0
waves[152] = -1
waves[200] = 0
waves[201] = 0
waves[202] = -1
waves[250] = 2
waves[251] = -1
waves[300] = 0
waves[301] = 0
waves[302] = 0
waves[303] = -1
waves[350] = 0
waves[351] = 2
waves[352] = -1
waves[400] = 0
waves[401] = 2
waves[402] = -1
waves[450:458] = [0,0,0,0,0,1,2,2,-1]
waves = tuple(waves)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule()
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
Prejudge(1,1)
WriteZombies([0],[5])
Prejudge(75,1)
Card(1, (5,6))
Prejudge(0,2)
WriteZombies([0],[2])
Prejudge(75,2)
PlantWhenAvailable(0,100,(2,6))
PlantWhenAvailable(4,25,(1,9))
Prejudge(0,3)
WriteZombies([0],[5])
Prejudge(0,4)
WriteZombies([0,0],[2,6])
PlantWhenAvailable(0,100,(2,5))
Prejudge(0,5)
WriteZombies([0,0],[2,5])
PlantWhenAvailable(4,25,(6,9))
Prejudge(0,6)
WriteZombies([2],[1])
Prejudge(0,7)
WriteZombies([0,0,0],[2,2,5])
Prejudge(0,8)
WriteZombies([0,2],[2,6])
Prejudge(0,9)
WriteZombies([0,2],[6,6])
Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,2],[2,3,4,2,3,4,2,3])
SetAmbushZombies([(3,8),(4,8)])
Prejudge(215,10)
Card(7,(3,9))
Card(3,(3,9))
while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)
