from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
Sleep(320)
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[0:2] = [0,2,-1]
waves[50:52] = [0,2,-1]
waves[100:102] = [0,2,-1]
waves[150:152] = [2,4,-1]
waves[200:202] = [2,4,-1]
waves[250:252] = [2,4,-1]
waves[300:303] = [0,4,4,-1]
waves[350:353] = [0,4,4,-1]
waves[400:403] = [0,4,4,-1]
waves[450:463] = [0,0,0,0,0,0,0,0,0,1,2,4,4,-1]
waves[500:503] = [4,4,4,-1]
waves[550:553] = [4,4,4,-1]
waves[600:605] = [0,2,4,4,4,-1]
waves[650:655] = [0,2,4,4,4,-1]
waves[700:705] = [0,2,4,4,4,-1]
waves[750:755] = [2,4,4,4,4,-1]
waves[800:805] = [2,4,4,4,4,-1]
waves[850:855] = [2,4,4,4,4,-1]
waves[900:906] = [0,4,4,4,4,4,-1]
waves[950:967] = [0,0,0,0,0,0,0,0,0,0,1,2,3,4,4,4,4,-1]
waves = tuple(waves)

while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(20)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)

Prejudge(1,1)
WriteZombies([0,2],[1,1])
Delay(1)
SetConveyorPlant(1,2)
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,2)
WriteZombies([0,2],[2,2])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,3)
WriteZombies([0,2],[3,3])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,3)
Delay(1)
PlantConveyorPlant(2,(4,9))
use_shovel(4,9)

Prejudge(1,4)
WriteZombies([2,4],[4,4])
Delay(100)
PlantConveyorPlant(1,(4,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,5)
WriteZombies([2,4],[5,5])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,3)
Delay(1)
PlantConveyorPlant(2,(4,9))
use_shovel(4,9)

Prejudge(1,6)
WriteZombies([2,4],[1,1])
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,7)
WriteZombies([0,4,4],[1,2,3])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,8)
WriteZombies([0,4,4],[2,3,4])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,9)
WriteZombies([0,4,4],[3,4,5])
Delay(100)
PlantConveyorPlant(1,(4,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)
Delay(1)
SetConveyorPlant(3,2)
Delay(1)
SetConveyorPlant(4,2)
Delay(1)
SetConveyorPlant(5,2)

Prejudge(1,10)
WriteZombies([0,0,0,0,0,0,0,0,0,1,2,4,4],[4,5,4,5,4,5,4,5,4,5,4,5,4])
Delay(215)
PlantConveyorPlant(1,(5,9))
Delay(1)
PlantConveyorPlant(1,(1,9))
Delay(1)
PlantConveyorPlant(1,(2,9))
Delay(1)
PlantConveyorPlant(1,(3,9))
Delay(1)
PlantConveyorPlant(1,(4,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,11)
WriteZombies([4,4,4],[1,1,2])
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,12)
WriteZombies([4,4,4],[1,2,3])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,13)
WriteZombies([0,2,4,4,4],[2,3,3,3,4])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(2,2)
Delay(1)
SetConveyorPlant(3,2)

Prejudge(1,14)
WriteZombies([0,2,4,4,4],[3,4,4,4,5])
Delay(100)
PlantConveyorPlant(1,(4,9))
Delay(1)
SetConveyorPlant(3,2)

Prejudge(1,15)
WriteZombies([0,2,4,4,4],[4,4,5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(3,2)
Delay(1)
SetConveyorPlant(4,2)

Prejudge(1,16)
WriteZombies([2,4,4,4,4],[1,1,1,2,2])
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(4,2)

Prejudge(1,17)
WriteZombies([2,4,4,4,4],[1,2,2,2,3])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(4,2)
Delay(1)
SetConveyorPlant(5,2)

Prejudge(1,18)
WriteZombies([2,4,4,4,4],[2,3,3,3,4])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(5,2)

Prejudge(1,19)
WriteZombies([0,4,4,4,4,4],[3,3,4,4,5,5])
Delay(100)
PlantConveyorPlant(1,(4,9))
Delay(1)
PlantConveyorPlant(1,(5,9))
Delay(1)
PlantConveyorPlant(1,(3,9))
Delay(1)
PlantConveyorPlant(1,(2,9))
Delay(1)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)
Delay(1)
SetConveyorPlant(3,2)
Delay(1)
SetConveyorPlant(4,2)

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,0,0,0,1,2,3,4,4,4,4],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2])
Delay(218)
PlantConveyorPlant(1,(1,9))
Delay(1)
PlantConveyorPlant(1,(2,9))
Delay(1)
PlantConveyorPlant(1,(4,9))
Delay(1)
PlantConveyorPlant(1,(5,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)