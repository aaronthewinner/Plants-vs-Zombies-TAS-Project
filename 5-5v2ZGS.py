from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
import os

safe_click()
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(3):
    safe_click()
    LeftClick(300,300)
Sleep(65)
press_esc()
left_down(400,400)
Sleep(1)
left_up(400,400)
press_enter()

Sleep(47)
left_down(480,520)
Sleep(1)
left_up(480,520)

left_click(600,280)
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
left_click(600,280)
press_enter()
left_click(450,560)
left_down(560,140)
Sleep(1)
left_up(560,140)

while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(11):
    safe_click()
    LeftClick(300,300) 
Sleep(1)

while(game_ui() != 2):
    Sleep(0.1)
start_time = time.time()
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1500)
waves = list(waves)
waves[0:2] = [2,-1]
waves[50:52] = [2,-1]
waves[100:102] = [2,-1]
waves[150:152] = [4,-1]
waves[200:202] = [4,-1]
waves[250:252] = [4,-1]
waves[300:303] = [4,2,-1]
waves[350:354] = [4,0,0,-1]
waves[400:404] = [4,2,-1]
waves[500:503] = [4,4,-1]
waves[550:553] = [4,4,-1]
waves[600:604] = [4,4,2,-1]
waves[650:654] = [4,4,2,-1]
waves[700:704] = [4,4,2,-1]
waves[750:754] = [4,4,4,-1]
waves[800:804] = [4,4,4,-1]
waves[850:854] = [4,4,4,-1]
waves[900:905] = [4,4,4,2,-1]
waves[950:970] = [20,20,20,20,20,0,0,0,0,0,0,0,4,4,4,4,4,-1]
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
AutoCollect(interval_cs = 1)
SetGraves([(4,8)])

Prejudge(1,1)
SetBungeeBlitzZombies([(4,8)])
Delay(1)
SetConveyorPlant(1,33)
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,2)
SetBungeeBlitzZombies([(1,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,3)
SetBungeeBlitzZombies([(1,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,33)
Delay(1)
PlantConveyorPlant(2,(2,5))

Prejudge(1,4)
SetBungeeBlitzZombies([(1,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,5)
SetBungeeBlitzZombies([(1,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,33)
Delay(1)
PlantConveyorPlant(2,(2,7))

Prejudge(1,6)
SetBungeeBlitzZombies([(1,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,7)
SetBungeeBlitzZombies([(1,5),(2,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,8)
SetBungeeBlitzZombies([(1,5),(2,5),(3,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,9)
SetBungeeBlitzZombies([(1,5),(2,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,33)
Delay(1)
SetConveyorPlant(2,33)
Delay(1)
SetConveyorPlant(3,33)
Delay(1)
SetConveyorPlant(4,33)
Delay(1)
SetConveyorPlant(5,33)

Prejudge(1,10)
SetBungees([(1,9),(2,9),(3,9),(4,9),(5,9)])
Delay(295)
PlantConveyorPlant(1,(2,8))
Delay(1)
PlantConveyorPlant(1,(3,8))
Delay(1)
PlantConveyorPlant(1,(4,8))
Delay(1)
PlantConveyorPlant(1,(4,7))
Delay(1)
PlantConveyorPlant(1,(4,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,11)
SetBungeeBlitzZombies([(1,5),(2,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,33)
Delay(1)
PlantConveyorPlant(2,(4,5))

Prejudge(1,12)
SetBungeeBlitzZombies([(1,5),(2,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,13)
SetBungeeBlitzZombies([(1,5),(2,5),(3,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,33)
Delay(1)
PlantConveyorPlant(2,(3,5))

Prejudge(1,14)
SetBungeeBlitzZombies([(1,5),(2,5),(3,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,15)
SetBungeeBlitzZombies([(1,5),(2,5),(3,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,33)
Delay(2)
PlantConveyorPlant(2,(3,6))

Prejudge(1,16)
SetBungeeBlitzZombies([(1,5),(2,5),(3,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,17)
SetBungeeBlitzZombies([(1,5),(2,5),(3,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,33)
Delay(1)
PlantConveyorPlant(2,(3,7))

Prejudge(1,18)
SetBungeeBlitzZombies([(1,5),(2,5),(3,5)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,19)
SetBungeeBlitzZombies([(1,5),(2,5),(3,5),(3,6)])
Delay(295)
PlantConveyorPlant(1,(2,6))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)
Delay(1)
SetConveyorPlant(3,2)
Delay(1)
SetConveyorPlant(4,2)

Prejudge(1,20)
SetBungees([(2,4),(3,4),(4,4),(2,5),(2,5)])
SetBungeeBlitzZombies([(1,6),(1,7),(1,8),(2,6),(2,7),(3,8),(5,6),(5,7),(5,8),(4,6),(4,7),(3,6)])
SetAmbushZombies([(3,5),(4,5),(4,6)])
Delay(400)
PlantConveyorPlant(1,(3,5))
Delay(1)
PlantConveyorPlant(1,(2,7))
Delay(1)
PlantConveyorPlant(1,(4,7))
Delay(148)
PlantConveyorPlant(1,(3,6))

while(game_ui() == 3):
    Sleep(0.1)
print(time.time()-start_time)