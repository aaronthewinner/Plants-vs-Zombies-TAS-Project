from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
      Sleep(0.1)
press_enter()
press_enter()
press_enter()
left_click(520,280)
Sleep(150)
left_click(520,280)

press_enter()
press_enter()
left_click(600,280)
press_enter()
left_click(450,560)
Sleep(5)
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
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[0:2] = [2,2,-1]
waves[50:52] = [2,2,-1]
waves[100:102] = [2,2,-1]
waves[150:154] = [2,2,2,2,-1]
waves[200:202] = [0,7,-1]
waves[250:252] = [0,7,-1]
waves[300:304] = [0,2,2,7,-1]
waves[350:354] = [0,2,2,7,-1]
waves[400:404] = [0,2,2,7,-1]
waves[450:463] = [0,0,0,0,0,0,0,0,0,0,1,2,2,-1]
waves[500:503] = [2,7,7,-1]
waves[550:553] = [2,7,7,-1]
waves[600:605] = [2,2,2,7,7,-1]
waves[650:655] = [2,2,2,7,7,-1]
waves[700:705] = [2,2,2,7,7,-1]
waves[750:755] = [0,2,7,7,7,-1]
waves[800:805] = [0,2,7,7,7,-1]
waves[850:855] = [0,2,7,7,7,-1]
waves[900:904] = [7,7,7,7,-1]
waves[950:969] = [0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,7,7,7,11,-1]
waves = tuple(waves)

while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(20)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)

Prejudge(1,1)
WriteZombies([2,2],[1,1])
Delay(1)
SetConveyorPlant(1,2)
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,2)
WriteZombies([2,2],[2,2])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,3)
WriteZombies([2,2],[2,2])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,16)
Delay(1)
PlantConveyorPlant(2,(3,9))

Prejudge(1,4)
WriteZombies([2,2,2,2],[5,5,6,6])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,5)
WriteZombies([0,7],[5,5])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,16)
Delay(1)
PlantConveyorPlant(2,(4,9))

Prejudge(1,6)
WriteZombies([0,7],[6,5])
Delay(100)
PlantConveyorPlant(1,(6,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,7)
WriteZombies([0,2,2,7],[1,1,2,2])
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,8)
WriteZombies([0,2,2,7],[1,3,2,2])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,9)
WriteZombies([0,2,2,7],[2,3,4,2])
Delay(100)
PlantConveyorPlant(1,(3,9))
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
WriteZombies([0,0,0,0,0,0,0,0,0,0,1,2,2],[3,4,5,3,4,5,3,4,5,3,4,5,3])
Delay(215)
PlantConveyorPlant(1,(4,9))
Delay(1)
PlantConveyorPlant(1,(5,9))
Delay(1)
PlantConveyorPlant(1,(6,9))
Delay(1)
PlantConveyorPlant(1,(1,9))
Delay(1)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(1,2)

Prejudge(1,11)
WriteZombies([2,7,7],[4,5,6])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,12)
WriteZombies([2,7,7],[5,6,6])
Delay(100)
PlantConveyorPlant(1,(6,9))
Delay(1)
SetConveyorPlant(2,2)

Prejudge(1,13)
WriteZombies([2,2,2,7,7],[1,1,1,2,2])
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
SetConveyorPlant(2,2)
Delay(1)
SetConveyorPlant(3,2)

Prejudge(1,14)
WriteZombies([2,2,2,7,7],[1,3,2,2,2])
Delay(100)
PlantConveyorPlant(1,(2,9))
Delay(1)
SetConveyorPlant(3,2)

Prejudge(1,15)
WriteZombies([2,2,2,7,7],[2,3,3,2,2])
Delay(100)
PlantConveyorPlant(1,(3,9))
Delay(1)
SetConveyorPlant(3,2)
Delay(1)
SetConveyorPlant(4,2)

Prejudge(1,16)
WriteZombies([0,2,7,7,7],[3,4,5,5,5])
Delay(100)
PlantConveyorPlant(1,(4,9))
Delay(1)
SetConveyorPlant(4,2)

Prejudge(1,17)
WriteZombies([0,2,7,7,7],[4,5,5,5,6])
Delay(100)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(4,2)
Delay(1)
SetConveyorPlant(5,2)

Prejudge(1,18)
WriteZombies([0,2,7,7,7],[5,5,6,6,6])
Delay(100)
PlantConveyorPlant(1,(6,9))
Delay(1)
SetConveyorPlant(5,2)

Prejudge(1,19)
WriteZombies([7,7,7,7],[1,1,2,2])
Delay(100)
PlantConveyorPlant(1,(1,9))
Delay(1)
PlantConveyorPlant(1,(2,9))
Delay(1)
PlantConveyorPlant(1,(3,9))
Delay(1)
PlantConveyorPlant(1,(4,9))
Delay(1)
PlantConveyorPlant(1,(5,9))
Delay(1)
SetConveyorPlant(1,2)
Delay(1)
SetConveyorPlant(2,2)
Delay(1)
SetConveyorPlant(3,2)
Delay(1)
SetConveyorPlant(4,2)

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,7,7,7,11],[1,2,3,4,5,6,1,2,3,4,5,6,1,3,4,2,5,6,3])
SetAmbushZombies([(4,9),(4,8),(3,9)])
Delay(50)
PlantConveyorPlant(1,(2,9))
Delay(1)
PlantConveyorPlant(1,(5,9))
Delay(1)
PlantConveyorPlant(1,(2,8))
Delay(1)
PlantConveyorPlant(1,(5,8))
Delay(1)
SetConveyorPlant(1,2)

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)