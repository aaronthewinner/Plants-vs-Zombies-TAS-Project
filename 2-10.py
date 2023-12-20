from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
SetGraves([(1,9),(4,9),(5,9),(1,8),(4,8),(5,8),(5,7),(1,7),(1,6),(5,6),(5,5),(1,5),(1,4)])
Sleep(320)
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[0:2] = [0,2,-1]
waves[50:52] = [0,2,-1]
waves[100:102] = [0,2,-1]
waves[150:152] = [2,6,-1]
waves[200:202] = [2,6,-1]
waves[250:252] = [2,6,-1]
waves[300:302] = [2,7,-1]
waves[350:352] = [2,7,-1]
waves[400:402] = [2,7,-1]
waves[450:463] = [0,0,0,0,0,0,0,0,0,0,1,2,7,-1]
waves[500:502] = [7,8,-1]
waves[550:552] = [7,8,-1]
waves[600:605] = [0,7,7,-1]
waves[650:655] = [0,7,7,-1]
waves[700:705] = [0,7,7,-1]
waves[750:755] = [6,7,7,-1]
waves[800:805] = [6,7,7,-1]
waves[850:855] = [6,7,7,-1]
waves[900:906] = [7,7,7,-1]
waves[950:964] = [0,0,0,0,0,0,0,1,2,6,6,7,8,8,-1]
waves = tuple(waves)

while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(20)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)

Prejudge(1,1)
WriteZombies([0,2],[2,3])
Delay(1)
SetConveyorPlant(1,12)
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(1,12)

Prejudge(1,2)
WriteZombies([0,2],[3,2])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,12)

Prejudge(1,3)
WriteZombies([0,2],[2,3])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(1,12)
Delay(1)
SetConveyorPlant(2,11)
Delay(1)
PlantConveyorPlant(2,(4,9))

Prejudge(1,4)
WriteZombies([2,6],[2,3])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,12)

Prejudge(1,5)
WriteZombies([2,6],[4,2])
Delay(100)
PlantConveyorPlant(1,(4,9))
Delay(1)
SetConveyorPlant(1,12)
Delay(1)
SetConveyorPlant(2,11)
Delay(1)
PlantConveyorPlant(2,(4,8))

Prejudge(1,6)
WriteZombies([2,6],[4,3])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(1,12)

Prejudge(1,7)
WriteZombies([2,7],[2,4])
Delay(100)
PlantConveyorPlant(1,(4,9))
Delay(1)
SetConveyorPlant(1,12)
Delay(1)
SetConveyorPlant(2,15)

Prejudge(1,8)
WriteZombies([2,7],[2,3])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(1,15)
Delay(1)
SetConveyorPlant(2,15)

Prejudge(1,9)
WriteZombies([2,7],[5,4])
Delay(100)
PlantConveyorPlant(1,(4,7))
Delay(1)
SetConveyorPlant(1,15)
Delay(1)
SetConveyorPlant(2,11)
Delay(1)
SetConveyorPlant(3,11)
Delay(1)
SetConveyorPlant(4,11)
Delay(1)
SetConveyorPlant(5,11)

Prejudge(1,10)
WriteZombies([0,0,0,0,0,0,0,0,0,0,1,2,7],[1,2,3,1,2,3,1,2,3,1,2,3,1])
Delay(215)
PlantConveyorPlant(1,(2,7))
Delay(1)
PlantConveyorPlant(1,(1,9))
Delay(1)
PlantConveyorPlant(1,(1,8))
Delay(1)
PlantConveyorPlant(1,(5,9))
Delay(1)
PlantConveyorPlant(1,(5,8))
Delay(1)
SetConveyorPlant(1,15)

Prejudge(1,11)
WriteZombies([7,8],[1,2])
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(1,15)
Delay(1)
SetConveyorPlant(2,11)
Delay(1)
PlantConveyorPlant(2,(5,5))

Prejudge(1,12)
WriteZombies([7,8],[2,1])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,15)

Prejudge(1,13)
WriteZombies([0,7,7],[2,3,4])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(1,15)
Delay(1)
SetConveyorPlant(2,11)
Delay(1)
PlantConveyorPlant(2,(5,6))

Prejudge(1,14)
WriteZombies([0,7,7],[3,4,5])
Delay(100)
PlantConveyorPlant(1,(4,9))
Delay(1)
SetConveyorPlant(1,15)

Prejudge(1,15)
WriteZombies([0,7,7],[4,5,5])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(1,15)
Delay(1)
SetConveyorPlant(2,11)
Delay(1)
PlantConveyorPlant(2,(5,7))

Prejudge(1,16)
WriteZombies([6,7,7],[1,1,2])
Delay(100)
PlantConveyorPlant(1,(1,8))
Delay(1)
SetConveyorPlant(1,15)

Prejudge(1,17)
WriteZombies([6,7,7],[1,2,3])
Delay(100)
PlantConveyorPlant(1,(2,8))
Delay(1)
SetConveyorPlant(1,15)
Delay(1)
SetConveyorPlant(2,11)
Delay(1)
PlantConveyorPlant(2,(1,4))

Prejudge(1,18)
WriteZombies([6,7,7],[3,4,5])
Delay(100)
PlantConveyorPlant(1,(4,8))
Delay(1)
SetConveyorPlant(1,15)

Prejudge(1,19)
WriteZombies([7,7,7],[4,5,5])
Delay(100)
PlantConveyorPlant(1,(5,8))
Delay(1)
SetConveyorPlant(1,15)
Delay(1)
SetConveyorPlant(2,15)
Delay(1)
SetConveyorPlant(3,15)
Delay(1)
SetConveyorPlant(4,15)

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,1,2,6,6,7,8,8],[1,2,3,4,5,1,2,3,4,5,1,2,3,4])
Delay(215)
PlantConveyorPlant(1,(3,8))
Delay(1)
PlantConveyorPlant(1,(3,7))
Delay(1)
PlantConveyorPlant(1,(3,6))
Delay(1)
PlantConveyorPlant(1,(3,5))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)