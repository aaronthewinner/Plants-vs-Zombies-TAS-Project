from pvz import *
from pvz.extra import *
import time

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

def SetConveyorPlant(slot, new_plant):
    while(ReadMemory("int",0x6A9EC0, 0x768, 0x144, 0xC + slot*0x50) == -1):
        Sleep(0.1)
    WriteMemory("int",new_plant, 0x6A9EC0, 0x768, 0x144, 0xC + slot*0x50)
def PlantConveyorPlant(slot, coords):
    while(ReadMemory("int",0x6A9EC0, 0x768, 0x144, 0xC + slot*0x50) == -1 or ReadMemory("int", 0x6A9EC0, 0x768, 0x144, 0x8 + slot*0x50)+50*(slot-1) > 499):
        Sleep(0.1)
    safe_click()
    LeftClick(ReadMemory("int", 0x6A9EC0, 0x768, 0x144, 0x8 + slot*0x50)+105+50*(slot-1),12)
    ClickGrid(coords)
@RunningInThread
def SlowZombies():
    while(game_ui() == 3 and ReadMemory("bool", 0x6A9EC0, 0x768, 0x5603)):
        zombies_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)
        zombies_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
        for i in range(zombies_count_max):
            zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
        if(not zombie_dead and ReadMemory("float", zombies_offset + 0x34 + i * 0x15c) > 0.231):
            WriteMemory("float",0.23, zombies_offset + 0x34 + i * 0x15c)
            WriteMemory("int",12,zombies_offset + 0x40 + i * 0x15c)
            asm_init()
            asm_mov_exx("esi", zombies_offset + i * 0x15C)
            asm_call(0x0052F050)
            asm_ret()
            asm_code_inject_safely()
@RunningInThread
def UpdateBoss():
    zomboss_offset = ReadMemory("int",0x6A9EC0,0x768, 0x90)
    while(game_ui() == 3 and ReadMemory("bool", 0x6A9EC0, 0x768, 0x5603)):
        if(ReadMemory("int",zomboss_offset + 0x130) != -1):
            WriteMemory("int",0,zomboss_offset + 0x130)
        if(ReadMemory("int",zomboss_offset + 0x12C) == 0 and ReadMemory("int",zomboss_offset + 0x114) > 450):
            WriteMemory("int",450,zomboss_offset + 0x114)
        if(ReadMemory("int",zomboss_offset + 0x12C) == 1 and ReadMemory("int",zomboss_offset + 0x114) > 375):
            WriteMemory("int",375,zomboss_offset + 0x114)    
        if((ReadMemory("int",zomboss_offset + 0x114) == 0 or ReadMemory("int",zomboss_offset + 0x13C) == 0) and  ReadMemory("int",zomboss_offset + 0x28) == 79):
            WriteMemory("int",0,zomboss_offset + 0x68)
        if(ReadMemory("int",zomboss_offset + 0x60) > 3000 and ReadMemory("int",zomboss_offset + 0x13C) > 4000):
            WriteMemory("int",4000,zomboss_offset + 0x13C)
        if(ReadMemory("int",zomboss_offset + 0x14C) == 1):
            WriteMemory("int",0,zomboss_offset+0x14C)
        if(ReadMemory("int",zomboss_offset + 0x148) != -1):
            WriteMemory("int",4,zomboss_offset+0x148)
        if(ReadMemory("int",zomboss_offset + 0x80) != -1):
            WriteMemory("int",2,zomboss_offset+0x80)
        
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(11):
    safe_click()
    LeftClick(300,300) 
Sleep(1)
update_game_scene()
Sleep(350)
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves = tuple(waves)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)

WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)

Delay(100)
UpdateBoss()
SlowZombies()
Delay(600)
PlantConveyorPlant(1,(3,2))
Delay(10)
PlantConveyorPlant(2,(2,2))
use_shovel(1,3)
Delay(1)
Delay(200)
PlantConveyorPlant(2,(3,1))
Delay(10)
SetConveyorPlant(2,20)
Delay(90)
SetConveyorPlant(3,20)
Delay(90)
SetConveyorPlant(4,39)
Delay(10)
PlantConveyorPlant(4,(4,2))
Delay(90)
SetConveyorPlant(4,20)
Delay(90)
SetConveyorPlant(5,20)
Delay(90)
SetConveyorPlant(6,39)
Delay(10)
PlantConveyorPlant(6,(5,2))
Delay(90)
SetConveyorPlant(6,20)
Delay(90)
SetConveyorPlant(7,20)
Delay(90)
SetConveyorPlant(8,20)
Delay(90)
SetConveyorPlant(9,20)
Delay(90)
SetConveyorPlant(10,20)

Delay(700)
PlantConveyorPlant(1,(1,1))
Delay(1)
PlantConveyorPlant(1,(2,1))
Delay(1)
PlantConveyorPlant(1,(3,1))
Delay(1)
PlantConveyorPlant(1,(4,1))
Delay(1)
PlantConveyorPlant(1,(5,1))
Delay(100)
PlantConveyorPlant(1,(1,1))
Delay(1)
PlantConveyorPlant(1,(2,1))
Delay(1)
PlantConveyorPlant(1,(3,1))
Delay(1)
PlantConveyorPlant(1,(4,1))
Delay(1)
SetConveyorPlant(2,20)
Delay(450)
PlantConveyorPlant(1,(5,1))
Delay(90)
SetConveyorPlant(2,20)


Delay(90)
SetConveyorPlant(3,20)
Delay(90)
SetConveyorPlant(4,20)
Delay(90)
SetConveyorPlant(5,20)
Delay(90)
SetConveyorPlant(6,20)
Delay(90)
SetConveyorPlant(7,20)
Delay(90)
SetConveyorPlant(8,20)
Delay(90)
SetConveyorPlant(9,20)
Delay(90)
SetConveyorPlant(10,20)
Delay(500)
FastPlants()
PlantConveyorPlant(1,(1,1))
Delay(1)
PlantConveyorPlant(1,(2,1))
Delay(1)
PlantConveyorPlant(1,(3,1))
Delay(1)
PlantConveyorPlant(1,(4,1))
Delay(1)
PlantConveyorPlant(1,(5,1))
Delay(100)
PlantConveyorPlant(1,(1,1))
Delay(1)
PlantConveyorPlant(1,(2,1))
Delay(1)
PlantConveyorPlant(1,(3,1))
Delay(1)
PlantConveyorPlant(1,(4,1))
Delay(1)
PlantConveyorPlant(1,(5,1))
Delay(90)
SetConveyorPlant(1,20)

Delay(90)
SetConveyorPlant(2,20)
PlantConveyorPlant(1,(1,2))
Delay(1)
PlantConveyorPlant(1,(2,1))
Delay(90)
SetConveyorPlant(1,20)

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)