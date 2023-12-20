from pvz import *
from pvz.extra import *
import time

def PlantWhenAvailable(seed_number, plant_cost, square):
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
        if(ReadMemory("int", 0x6A9EC0, 0x768, 0x5560) + collected_items*25 >= plant_cost):
            j += 1
            if(j >= 10 and ReadMemory("bool", slots_offset + 0x20+seed_number*0x50)):
                Card(seed_number,square)
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
            elif not plant_dead and not plant_squished and plant_type == 0:
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
                    WriteMemory("int",0, plants_offset + 0x58 + i * 0x14c)
                if(ReadMemory("int", plants_offset + 0x58 + i * 0x14c) > 135):
                    WriteMemory("int",135, plants_offset + 0x58 + i * 0x14c)

@RunningInThread
def thirtyFiveRule(waves):
    for i in range(1,waves):
        Prejudge(1,i)
        if(i % 10 == 9):
            continue
        WriteMemory("int",(int)(ReadMemory("int",0x6a9ec0, 0x768, 0x5598)*0.65), 0x6a9ec0, 0x768, 0x5594)
        WriteMemory("int",2499,0x6a9ec0, 0x768, 0x55A0)
        WriteMemory("int",2499,0x6a9ec0, 0x768, 0x559C)

def WriteZombies(zombie_Types,zombie_rows=[0]):
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
                    WriteMemory("float",50+(zombie_rows[j] - 1)*100, zombies_offset + 0x30 + i * 0x15c)
                j += 1
                if(j == len(zombie_Types)):
                    break

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
update_game_scene()
Sleep(320)
select_seeds_and_lets_rock((1,16,17,4,6,19,8,20))
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1500)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:201] = [2,-1]
waves[250:251] = [2,-1]
waves[300:302] = [0,2,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:457] = [0,0,0,0,0,1,4,-1]
waves[500:501] = [4,-1]
waves[550:551] = [4,-1]
waves[600:602] = [0,4,-1]
waves[650:652] = [0,4,-1]
waves[700:702] = [0,4,-1]
waves[750:752] = [2,4,-1]
waves[800:802] = [2,4,-1]
waves[850:852] = [11,11,-1]
waves[900:901] = [12,-1]
waves[950:960] = [0,0,0,0,0,0,0,0,1,12,-1]
waves[1000:1001] = [12,-1]
waves[1050:1052] = [0,12,-1]
waves[1100:1102] = [0,12,-1]
waves[1150:1152] = [0,12,-1]
waves[1200:1202] = [2,12,-1]
waves[1250:1252] = [2,12,-1]
waves[1300:1302] = [2,12,-1]
waves[1350:1353] = [2,4,4,-1]
waves[1400:1402] = [11,12,-1]
waves[1450:1465] = [0,0,0,0,0,0,0,0,0,0,1,2,4,11,12,-1]
waves = tuple(waves)

while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=0.1)
FastSun()
FastPlants()
thirtyFiveRule(20)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)

PlantWhenAvailable(1,50,(1,1))
PlantWhenAvailable(7,0,(6,1))
PlantWhenAvailable(1,50,(1,2))
PlantWhenAvailable(7,0,(6,2))
PlantWhenAvailable(1,50,(1,3))
PlantWhenAvailable(7,0,(6,3))

Prejudge(1,1)
WriteZombies([0])
PlantWhenAvailable(3,50,(6,9))
PlantWhenAvailable(1,50,(1,4))
PlantWhenAvailable(4,25,(1,8))

Prejudge(0,2)
WriteZombies([0],[6])
PlantWhenAvailable(1,50,(1,5))

Prejudge(0,3)
WriteZombies([0],[1])
PlantWhenAvailable(6,25,(3,9))
PlantWhenAvailable(1,50,(1,6))

Prejudge(0,4)
WriteZombies([0,0],[1,6])
PlantWhenAvailable(1,50,(1,7))
PlantWhenAvailable(8,125,(1,9))

Prejudge(0,5)
WriteZombies([2],[1])
PlantWhenAvailable(3,50,(1,9))
PlantWhenAvailable(1,50,(1,8))

Prejudge(0,6)
WriteZombies([2],[3])
PlantWhenAvailable(4,25,(2,9))

Prejudge(0,7)
WriteZombies([0,2],[3,5])
PlantWhenAvailable(5,150,(5,9))
PlantWhenAvailable(1,50,(6,8))

Prejudge(0,8)
WriteZombies([0,2],[2,2])
Delay(350)
PlantWhenAvailable(6,25,(3,9))

Prejudge(0,9)
WriteZombies([0,2],[1,1])
PlantWhenAvailable(1,50,(6,7))
PlantWhenAvailable(3,50,(1,9))
PlantWhenAvailable(4,25,(2,9))
PlantWhenAvailable(1,50,(6,6))
Delay(210)
use_shovel(6,1)

Prejudge(0,10)
WriteZombies([0,0,0,0,0,1,4],[4,4,4,4,4,6,6])
PlantWhenAvailable(1,50,(6,5))

Prejudge(0,11)
WriteZombies([4],[5])
use_shovel(5,9)
PlantWhenAvailable(5,150,(5,9))
PlantWhenAvailable(1,50,(6,4))

Prejudge(0,12)
WriteZombies([4],[6])
use_shovel(5,9)
PlantWhenAvailable(8,125,(6,9))
PlantWhenAvailable(6,25,(3,8))
PlantWhenAvailable(1,50,(6,3))

Prejudge(0,13)
WriteZombies([0,4],[3,3])
PlantWhenAvailable(3,50,(5,9))

Prejudge(0,14)
WriteZombies([0,4],[2,2])
PlantWhenAvailable(4,25,(1,9))
PlantWhenAvailable(1,50,(6,2))

Prejudge(0,15)
WriteZombies([0,4],[5,5])
PlantWhenAvailable(5,150,(2,9))
PlantWhenAvailable(1,50,(6,1))

Prejudge(0,16)
WriteZombies([2,4],[6,2])
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,17)
WriteZombies([2,4],[1,1])

Prejudge(0,18)
WriteZombies([11,11],[4,4])
PlantWhenAvailable(2,25,(4,9))
PlantWhenAvailable(3,50,(4,9))

Prejudge(0,19)
WriteZombies([12],[6])
use_shovel(6,9)
PlantWhenAvailable(4,25,(5,9))
PlantWhenAvailable(5,150,(6,9))
use_shovel(2,9)
Delay(500)
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,20)
WriteZombies([0,0,0,0,0,0,0,0,1,12],[2,2,2,2,2,1,1,1,2,1])
Delay(215)
PlantWhenAvailable(8,125,(1,9))

Prejudge(0,21)
WriteZombies([12],[6])
Delay(100)
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,22)
WriteZombies([0,12],[2,6])
Delay(205)
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,23)
WriteZombies([0,12],[2,6])
Delay(310)
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,24)
WriteZombies([0,12],[2,6])

Prejudge(0,25)
WriteZombies([2,12],[2,5])
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,26)
WriteZombies([2,12],[2,6])
PlantWhenAvailable(3,50,(5,9))
PlantWhenAvailable(4,25,(1,9))

Prejudge(0,27)
WriteZombies([2,12],[3,6])
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,28)
WriteZombies([2,4,4],[4,4,4])

Prejudge(0,29)
WriteZombies([11,12],[3,5])
PlantWhenAvailable(6,25,(3,9))

Prejudge(1,30)
WriteZombies([0,0,0,0,0,0,0,0,0,0,1,2,4,11,12],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,2])
SetAmbushZombies([(3,8),(3,7),(3,6)])
PlantWhenAvailable(5,150,(2,9))
PlantWhenAvailable(2,25,(3,9))
PlantWhenAvailable(8,125,(3,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)