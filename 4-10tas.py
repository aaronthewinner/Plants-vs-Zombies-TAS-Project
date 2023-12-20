from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(3):
    safe_click()
    LeftClick(300,300) 
Sleep(1)

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
Sleep(320)
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1500)
waves = list(waves)
waves[0:2] = [0,2,-1]
waves[50:53] = [0,0,0,-1]
waves[100:102] = [0,0,0,-1]
waves[150:152] = [2,4,-1]
waves[200:202] = [2,4,-1]
waves[250:252] = [2,4,-1]
waves[300:303] = [0,4,4,-1]
waves[350:353] = [0,4,4,-1]
waves[400:403] = [0,4,4,-1]
waves[450:463] = [0,0,0,0,0,1,16,16,16,16,16,16,16,-1] 
waves[500:506] = [16,16,16,16,16,16,-1]
waves[550:556] = [16,16,16,16,16,16,-1]
waves[600:608] = [16,16,16,16,16,16,16,0,-1]
waves[650:658] = [16,16,16,16,16,16,16,0,-1]
waves[700:708] = [16,16,16,16,16,16,16,0,-1]
waves[750:759] = [16,16,16,16,16,16,16,16,16,-1]
waves[800:809] = [16,16,16,16,16,16,16,16,16,-1]
waves[850:859] = [16,16,16,16,16,16,16,16,16,-1]
waves[900:911] = [16,16,16,16,16,16,16,16,16,16,0,-1]
waves[950:964] = [0,0,0,0,0,0,0,1,2,4,4,4,4,15,16,17,18,-1]
waves = tuple(waves)

while(game_ui() != 3):
    Sleep(1)
update_game_scene()
SetGraves([(1,8)])
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(20)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)

Prejudge(1,1)
WriteZombies([0,2],[1,1],[0.368,0.37])
Delay(1)
SetConveyorPlant(1,29) #blover=27 starfruit=29 magnet=31 lily=16
Delay(100)
SetConveyorPlant(2,29)
#PlantConveyorPlant(1,(1,1))
Delay(1)


Prejudge(1,2)
WriteZombies([0,0,0],[1,6,2])
SetConveyorPlant(3,29)
Delay(500)
PlantConveyorPlant(1,(2,9))
Delay(1)
PlantConveyorPlant(1,(1,9))

Prejudge(1,3)
WriteZombies([0,0,0],[1,6,2])
use_shovel(1,9)
use_shovel(2,9)
SetConveyorPlant(2,29)
Delay(500)
PlantConveyorPlant(1,(2,9))
Delay(1)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(1,31)
Delay(1)
SetConveyorPlant(2,31)
Delay(1)
SetConveyorPlant(3,31)
Delay(1)
SetConveyorPlant(4,31)
Delay(1)

Prejudge(1,4)
WriteZombies([2,4],[1,1])
Delay(100)
PlantConveyorPlant(1,(2,8))
Delay(1)
SetConveyorPlant(4,31)

Prejudge(1,5)
WriteZombies([2,4],[1,1])
use_shovel(2,9)
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(4,31)

Prejudge(1,6)
WriteZombies([2,4],[6,6])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(4,31)

Prejudge(1,7)
WriteZombies([0,4,4],[1,1,1])
Delay(100)
PlantConveyorPlant(1,(5,8))
Delay(1)
SetConveyorPlant(4,31)
Delay(1)
PlantConveyorPlant(1,(6,2))
Delay(1)
SetConveyorPlant(5,31)

Prejudge(1,8)
WriteZombies([0,4,4],[6,6,6])
Delay(100)
PlantConveyorPlant(1,(6,8))
Delay(1)
PlantConveyorPlant(1,(6,9))
#Delay(1)
#SetConveyorPlant(4,31)
#Delay(1)
#PlantConveyorPlant(1,(6,1))
#Delay(200)
#use_shovel(6,1)
#Delay(1)
#SetConveyorPlant(5,31)

Prejudge(1,9)
WriteZombies([0,4,4],[6,6,6])
Delay(100)
PlantConveyorPlant(1,(5,8))
Delay(1)
SetConveyorPlant(4,31)
Delay(1)
SetConveyorPlant(5,31)
Delay(1)
SetConveyorPlant(1,27)
Delay(1)
SetConveyorPlant(2,27)
Delay(1)
SetConveyorPlant(3,27)
Delay(1)
SetConveyorPlant(4,27)
Delay(1)
SetConveyorPlant(5,27)

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,16,16,16,16,16,16,16],[5,5,5,5,5,5,4,4,4,4,4,4,4])
Delay(215)
PlantConveyorPlant(1,(5,7))
Delay(1)
SetConveyorPlant(5,27)
Delay(1)
SetConveyorPlant(6,27)

Prejudge(1,11)
WriteZombies([16,16,16,16,16,16],[5,5,5,5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(6,27)
Delay(1)
SetConveyorPlant(7,27)

Prejudge(1,12)
WriteZombies([16,16,16,16,16,16],[5,5,5,5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,8))
Delay(1)
SetConveyorPlant(7,27)

Prejudge(1,13)
WriteZombies([16,16,16,16,16,16,16,0],[5,5,5,5,5,5,5,2])
Delay(100)
PlantConveyorPlant(1,(5,6))
Delay(1)
SetConveyorPlant(7,27)
Delay(1)
SetConveyorPlant(8,27)

Prejudge(1,14)
WriteZombies([16,16,16,16,16,16,16,0],[5,5,5,5,5,5,5,3])
Delay(100)
PlantConveyorPlant(1,(5,5))
Delay(1)
SetConveyorPlant(8,27)

Prejudge(1,15)
WriteZombies([16,16,16,16,16,16,16,0],[5,5,5,5,5,5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,4))
Delay(1)
SetConveyorPlant(8,27)
Delay(1)
SetConveyorPlant(9,27)

Prejudge(1,16)
WriteZombies([16,16,16,16,16,16,16,16,16],[5,5,5,5,5,5,5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,3))
Delay(1)
SetConveyorPlant(4,27)

Prejudge(1,17)
WriteZombies([16,16,16,16,16,16,16,16,16],[5,5,5,5,5,5,5,5,5])
Delay(100)
PlantConveyorPlant(1,(5,2))
Delay(1)
SetConveyorPlant(4,27)
Delay(1)
SetConveyorPlant(5,27)

Prejudge(1,18)
WriteZombies([16,16,16,16,16,16,16,16,16],[5,5,5,5,5,5,5,5,5])
Delay(100)
PlantConveyorPlant(1,(2,2))
Delay(1)
SetConveyorPlant(5,29)

Prejudge(1,19)
WriteZombies([16,16,16,16,16,16,16,16,16,16,0],[5,5,5,5,5,5,5,5,5,5,5])
Delay(100)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(1,27)
Delay(300)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(2,27)
Delay(1)
SetConveyorPlant(3,27)
Delay(1)
PlantConveyorPlant(1,(2,1))
Delay(1)
SetConveyorPlant(4,27)

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,1,2,4,4,4,4,15,16,17,18],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) 
SetAmbushZombies([(3,9),(3,8),(3,7)])
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


while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)
