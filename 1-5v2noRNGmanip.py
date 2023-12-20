from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(5):
    safe_click()
    LeftClick(300,300) 
Sleep(1)

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
Sleep(63)
use_shovel((2,6),(3,8),(4,7))

while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(5):
    safe_click()
    LeftClick(300,300) 
Sleep(1)

waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[0:2] = [2,2,-1]
waves[50:52] = [2,2,-1]
waves[100:102] = [2,2,-1]
waves[150:155] = [2,2,2,2,-1]
waves[200:205] = [2,2,2,2,-1]
waves[250:255] = [2,2,2,2,-1]
waves[300:307] = [2,2,2,2,2,2,-1]
waves[350:360] = [2,2,2,2,2,2,0,0,0,1,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
AutoCollect(interval_cs=1)
WriteMemory("unsigned char", 0x88, 0x45DE03)
WriteMemory("unsigned char", 0x93, 0x45DE04)
Prejudge(1,1)
WriteZombies([2,2],[1,2],[0.37,0.23])
Delay(80)
PlantConveyorPlant(1,(1,3))
Delay(1)
SetConveyorPlant(1,49)

Prejudge(0,2)
WriteZombies([2,2],[1,2],[0.37,0.37])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(2,3))
Delay(250)
SetConveyorPlant(2,49)

Prejudge(0,3)
WriteZombies([2,2],[3,4],[0.37,0.37])
PlantConveyorPlant(2,(3,3))
Delay(150)
SetConveyorPlant(2,49)
Delay(250)
SetConveyorPlant(3,49)

Prejudge(0,4)
WriteZombies([2,2,2,2],[3,4,5,5],[0.37,0.37,0.37,0.37])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(4,3))
Delay(150)
SetConveyorPlant(2,49)
SetConveyorPlant(3,49)

Prejudge(0,5)
WriteZombies([2,2,2,2],[1,2,3,3],[0.37,0.37,0.37,0.37])
SetConveyorPlant(3,49)
PlantConveyorPlant(2,(2,3))
Delay(100)
SetConveyorPlant(3,49)
Delay(150)
SetConveyorPlant(4,49)

Prejudge(1,6)
WriteZombies([2,2,2,2],[3,3,3,3],[0.37,0.37,0.37,0.37])
SetConveyorPlant(3,49)
PlantConveyorPlant(2,(3,3))
Delay(200)
SetConveyorPlant(4,49)

Prejudge(0,7)
WriteZombies([2,2,2,2,2,2],[3,3,3,3,5,4],[0.37,0.37,0.37,0.37,0.37,0.37])
SetConveyorPlant(3,49)
PlantConveyorPlant(2,(4,3))
Delay(150)
SetConveyorPlant(4,49)
Delay(250)
SetConveyorPlant(5,49)
Delay(250)
SetConveyorPlant(6,49)

Prejudge(0,8)
WriteZombies([2,2,2,2,2,2,0,0,0,1],[1,1,1,2,2,2,3,3,3,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45])
SetConveyorPlant(1,49)
PlantConveyorPlant(2,(2,3))
Delay(10)
SetConveyorPlant(1,49)
PlantConveyorPlant(2,(2,3))
Delay(10)
SetConveyorPlant(1,49)
PlantConveyorPlant(2,(2,3))
Delay(10)
SetConveyorPlant(1,49)
PlantConveyorPlant(2,(2,3))
Delay(10)
SetConveyorPlant(1,49)
PlantConveyorPlant(2,(2,3))
Delay(10)
SetConveyorPlant(1,49)
PlantConveyorPlant(2,(2,3))
Delay(10)
PlantConveyorPlant(1,(2,3))

while(game_ui() == 3):
    Sleep(0.1)
print(time.time()-start_time)