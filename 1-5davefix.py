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
Prejudge(1,1)
WriteZombies([2,2],[1,2])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(1,3))
Prejudge(1,2)
WriteZombies([2,2],[1,2])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(1,3))
Prejudge(1,3)
WriteZombies([2,2],[3,4])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(3,3))
Prejudge(1,4)
WriteZombies([2,2,2,2],[3,4,5,5])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(4,3))
Prejudge(1,5)
WriteZombies([2,2,2,2],[1,2,3,3])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(2,3))
Prejudge(1,6)
WriteZombies([2,2,2,2],[3,3,3,3])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(3,3))
Prejudge(1,7)
WriteZombies([2,2,2,2,2,2],[3,3,3,3,5,4])
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(4,3))
Prejudge(2,8)
WriteZombies([2,2,2,2,2,2,0,0,0,1],[1,1,1,2,2,2,3,3,3,3])
Delay(50)
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(2,3))
Sleep(1)
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(2,3))
Sleep(1)
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(2,3))
Sleep(1)
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(2,3))
Sleep(1)
SetConveyorPlant(2,49)
PlantConveyorPlant(2,(2,3))
while(game_ui() == 3):
    Sleep(0.1)
print(time.time()-start_time)