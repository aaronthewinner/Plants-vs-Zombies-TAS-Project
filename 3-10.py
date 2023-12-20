from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
Sleep(320)
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1500)
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
waves[450:463] = [0,0,0,0,0,0,0,0,1,2,4,14,14,-1]
waves[500:503] = [4,4,4,-1]
waves[550:553] = [4,4,4,-1]
waves[600:603] = [4,4,12,-1]
waves[650:653] = [4,4,12,-1]
waves[700:705] = [0,4,4,14,14,-1]
waves[750:755] = [4,4,4,14,14,-1]
waves[800:803] = [4,12,12,-1]
waves[850:853] = [4,12,12,-1]
waves[900:903] = [12,12,12,-1]
waves[950:964] = [0,0,0,0,0,0,0,0,0,1,4,12,12,12,-1]
waves[1000:1007] = [11,11,11,14,14,14,14,-1]
waves[1050:1058] = [11,11,11,11,14,14,14,14,-1]
waves[1100:1105] = [0,2,12,12,12,-1]
waves[1150:1155] = [0,2,12,12,12,-1]
waves[1200:1205] = [2,4,12,12,12,-1]
waves[1250:1255] = [2,4,12,12,12,-1]
waves[1300:1309] = [11,11,11,11,14,14,14,14,14,-1]
waves[1350:1360] = [11,11,11,11,11,14,14,14,14,14,-1]
waves[1400:1405] = [2,12,12,12,12,-1]
waves[1450:1475] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,4,11,12,12,12,14,-1]
waves = tuple(waves)

while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(30)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)

Prejudge(1,1)
WriteZombies([0,2],[1,1])
Delay(1)
SetConveyorPlant(1,20)
Delay(100)
PlantConveyorPlant(1,(1,1))
Delay(1)
SetConveyorPlant(1,20)

Prejudge(1,2)
WriteZombies([0,2],[2,2])
Delay(100)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(1,20)

Prejudge(1,3)
WriteZombies([0,2],[2,2])
Delay(100)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,16)
Delay(1)
PlantConveyorPlant(2,(3,1))

Prejudge(1,4)
WriteZombies([2,4],[5,5])
Delay(100)
PlantConveyorPlant(1,(5,1))
Delay(1)
SetConveyorPlant(1,20)

Prejudge(1,5)
WriteZombies([2,4],[5,5])
Delay(100)
PlantConveyorPlant(1,(5,1))
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,16)
Delay(1)
PlantConveyorPlant(2,(4,1))

Prejudge(1,6)
WriteZombies([2,4],[6,6])
Delay(100)
PlantConveyorPlant(1,(6,1))
Delay(1)
SetConveyorPlant(1,20)

Prejudge(1,7)
WriteZombies([0,4,4],[1,1,1])
Delay(100)
PlantConveyorPlant(1,(1,1))
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,20)

Prejudge(1,8)
WriteZombies([0,4,4],[2,2,2])
Delay(100)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,20)

Prejudge(1,9)
WriteZombies([0,4,4],[3,3,3])
Delay(100)
PlantConveyorPlant(1,(3,1))
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,20)
Delay(1)
SetConveyorPlant(3,20)
Delay(1)
SetConveyorPlant(4,20)
Delay(1)
SetConveyorPlant(5,20)

Prejudge(1,10)
WriteZombies([0,0,0,0,0,0,0,0,1,2,4,14,14],[4,4,4,4,4,4,4,4,4,4,4,4,4])
Delay(215)
PlantConveyorPlant(1,(4,1))
Delay(1)
PlantConveyorPlant(1,(5,1))
Delay(1)
PlantConveyorPlant(1,(6,1))
Delay(1)
PlantConveyorPlant(1,(1,1))
Delay(1)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(1,20)

Prejudge(1,11)
WriteZombies([4,4,4],[5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,1))
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,20)

Prejudge(1,12)
WriteZombies([4,4,4],[6,6,6])
Delay(100)
PlantConveyorPlant(1,(6,1))
Delay(1)
SetConveyorPlant(2,20)

Prejudge(1,13)
WriteZombies([4,4,12],[1,1,1])
Delay(100)
PlantConveyorPlant(1,(1,1))
Delay(1)
SetConveyorPlant(2,20)
Delay(1)
SetConveyorPlant(3,20)

Prejudge(1,14)
WriteZombies([4,4,12],[2,2,2])
Delay(100)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(3,20)

Prejudge(1,15)
WriteZombies([0,4,4,14,14],[3,3,3,3,3])
Delay(100)
PlantConveyorPlant(1,(3,1))
Delay(1)
SetConveyorPlant(3,20)
Delay(1)
SetConveyorPlant(4,20)

Prejudge(1,16)
WriteZombies([4,4,4,14,14],[4,4,4,4,4])
Delay(100)
PlantConveyorPlant(1,(4,1))
Delay(1)
SetConveyorPlant(4,20)

Prejudge(1,17)
WriteZombies([4,12,12],[5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,1))
Delay(1)
SetConveyorPlant(4,20)
Delay(1)
SetConveyorPlant(5,20)

Prejudge(1,18)
WriteZombies([4,12,12],[6,6,6])
Delay(100)
PlantConveyorPlant(1,(6,1))
Delay(1)
SetConveyorPlant(5,20)

Prejudge(1,19)
WriteZombies([12,12,12],[1,1,1])
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
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,20)
Delay(1)
SetConveyorPlant(3,20)
Delay(1)
SetConveyorPlant(4,20)

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,0,0,1,4,12,12,12],[2,2,2,2,2,2,2,2,2,2,2,2,2,2])
Delay(215)
PlantConveyorPlant(1,(2,1))
Delay(1)
PlantConveyorPlant(1,(3,1))
Delay(1)
PlantConveyorPlant(1,(4,1))
Delay(1)
PlantConveyorPlant(1,(5,1))
Delay(1)
SetConveyorPlant(1,20)

Prejudge(1,21)
WriteZombies([11,11,11,14,14,14,14],[3,3,3,3,3,3,3])
Delay(100)
PlantConveyorPlant(1,(3,1))
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,20)

Prejudge(1,22)
WriteZombies([11,11,11,11,14,14,14,14],[4,4,4,4,4,4,4,4])
Delay(100)
PlantConveyorPlant(1,(4,1))
Delay(1)
SetConveyorPlant(2,20)

Prejudge(1,23)
WriteZombies([0,2,12,12,12],[5,5,5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,1))
Delay(1)
SetConveyorPlant(2,20)
Delay(1)
SetConveyorPlant(3,20)

Prejudge(1,24)
WriteZombies([0,2,12,12,12],[6,6,6,6,6])
Delay(100)
PlantConveyorPlant(1,(6,1))
Delay(1)
SetConveyorPlant(3,20)

Prejudge(1,25)
WriteZombies([2,4,12,12,12],[1,1,1,1,1])
Delay(100)
PlantConveyorPlant(1,(1,1))
Delay(1)
SetConveyorPlant(3,20)
Delay(1)
SetConveyorPlant(4,20)

Prejudge(1,26)
WriteZombies([2,4,12,12,12],[2,2,2,2,2])
Delay(100)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(4,20)

Prejudge(1,27)
WriteZombies([11,11,11,11,14,14,14,14,14],[3,3,3,3,3,3,3,3,3])
Delay(100)
PlantConveyorPlant(1,(3,1))
Delay(1)
SetConveyorPlant(4,20)
Delay(1)
SetConveyorPlant(5,20)

Prejudge(1,28)
WriteZombies([11,11,11,11,11,14,14,14,14,14],[4,4,4,4,4,4,4,4,4,4])
Delay(100)
PlantConveyorPlant(1,(4,1))
Delay(1)
SetConveyorPlant(5,20)

Prejudge(1,29)
WriteZombies([2,12,12,12,12],[5,5,5,5,5])
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
Delay(1)
SetConveyorPlant(1,20)
Delay(1)
SetConveyorPlant(2,20)
Delay(1)
SetConveyorPlant(3,20)
Delay(1)
SetConveyorPlant(4,20)

Prejudge(1,30)
WriteZombies([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,4,11,12,12,12,14],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,4,6,6,6,4])
SetAmbushZombies([(4,9),(4,8),(4,7)])
Delay(205)
PlantConveyorPlant(1,(4,1))
Delay(1)
PlantConveyorPlant(1,(6,1))
Delay(10)
PlantConveyorPlant(1,(6,2))
Delay(10)
PlantConveyorPlant(1,(6,3))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)