from pvz import ReadMemory, WriteMemory, SetZombies, Prejudge, game_ui, Sleep, AutoCollect, Card, RunningInThread
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
            if(collected):
                collected_items += 1
        if(ReadMemory("bool", slots_offset + 0x70+SeedNumber*0x50) and ReadMemory("int", 0x6A9EC0, 0x768, 0x5560) + collected_items*25 >= plant_cost):
            j += 1
            if(j >= 3):
                Card(SeedNumber+1,square)
                break
@RunningInThread
def FastSun():
    SunsFallen = -1
    print("hi")
    while(game_ui() == 3):
        if(ReadMemory("int", 0x6A9EC0,0x768,0x553c) != SunsFallen):
            SunsFallen += 1
            WriteMemory("int",min(425 + SunsFallen * 10, 950),0x6A9EC0,0x768,0x5538)
@RunningInThread
def FastPlants():
    plants = []
    while(game_ui() == 3):
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
            elif not plant_dead and not plant_squished and plant_type == 0:
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
                    WriteMemory("int",0, plants_offset + 0x58 + i * 0x14c)
                if(ReadMemory("int", plants_offset + 0x58 + i * 0x14c) > 135):
                    WriteMemory("int",135, plants_offset + 0x58 + i * 0x14c)

# pls



@RunningInThread
def thirtyFiveRule():
    for i in range(1,9):
        Prejudge(1,i)
        WriteMemory("int",(int)(ReadMemory("int",0x6a9ec0, 0x768, 0x5598)*0.65), 0x6a9ec0, 0x768, 0x5594)


# pls


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

while(game_ui() != 2):
    Sleep(10)
start_time = time.time()
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150] = 0
waves[151] = 0
waves[152] = -1
waves[200] = 0
waves[201] = 0
waves[202] = -1
waves[250] = 0
waves[251] = 0
waves[252] = -1
waves[300] = 0
waves[301] = 0
waves[302] = 0
waves[303] = -1
waves[350] = 2
waves[351] = 0
waves[352] = -1
waves[400] = 2
waves[401] = 0
waves[402] = -1
waves[455] = 2
waves[456] = 2
waves[457] = 0
waves[458] = -1
waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(10)
AutoCollect(interval_cs=1)
thirtyFiveRule()
FastSun()
Prejudge(1,1)
items_offset = ReadMemory("int", 0x6A9EC0, 0x768, 0xE4)
WriteZombies([0],[3],[0.37])
Prejudge(75,1)
PlantWhenAvailable(0,100,(3,6))
Prejudge(1,2)
WriteZombies([0],[2],[0.37])
Prejudge(75,2)
PlantWhenAvailable(0,100,(2,6))
Prejudge(1,3)
WriteZombies([0],[3],[0.37])
Prejudge(1,4)
WriteZombies([0,0],[2,4],[0.37,0.23])
PlantWhenAvailable(0,100,(2,5))
Prejudge(1,5)
WriteZombies([0,0],[2,5],[0.37,0.37])
Prejudge(1,6)
WriteZombies([0,0],[1,3],[0.37,0.37])
PlantWhenAvailable(0,100,(3,5))
Prejudge(1,7)
WriteZombies([0,0,0],[2,2,3],[0.37,0.37,0.37])
Prejudge(1,8)
WriteZombies([0,2],[1,4],[0.37,0.37])
Prejudge(1,9)
WriteZombies([0,2],[5,5],[0.37,0.37])
Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,2])
Prejudge(60,10)
Card(3,(2,9))
print(time.time()-start_time)




