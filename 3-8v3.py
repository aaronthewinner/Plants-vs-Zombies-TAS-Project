from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_all_seeds([1,16,17,4,6,19,20])

safe_click()
left_down(720,580)
Sleep(2)
left_up(720,580)
left_click(430,280)
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
      Sleep(0.1)
left_click(430,280)

press_enter()
press_enter()
left_click(600,280)
press_enter()
left_click(450,560)

LeftClick(30,240)
lets_rock()
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:201] = [2,-1]
waves[250:251] = [2,-1]
waves[300:302] = [0,2,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:459] = [0,0,0,0,0,0,0,1,2,-1]
waves[500:502] = [0,14,-1]
waves[550:552] = [2,2,-1]
waves[600:603] = [0,2,2,-1]
waves[650:653] = [0,2,2,-1]
waves[700:703] = [0,2,2,-1]
waves[750:753] = [2,2,2,-1]
waves[800:803] = [2,2,2,-1]
waves[850:853] = [14,14,-1]
waves[900:903] = [0,2,2,2,-1]
waves[950:960] = [0,0,0,0,0,0,0,1,2,14,14,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(20)
SetGraves([(5,8)])

PlantWhenAvailable(1,50,(1,1))
PlantWhenAvailable(1,50,(1,2))
PlantWhenAvailable(1,50,(1,3))

Prejudge(1,1)
WriteZombies([0],[5],[0.37])
PlantWhenAvailable(3,50,(6,9))
PlantWhenAvailable(1,50,(1,4))
PlantWhenAvailable(4,25,(1,8))

Prejudge(1,2)
WriteZombies([0],[6],[0.37])
PlantWhenAvailable(1,50,(1,5))

Prejudge(1,3)
WriteZombies([0],[1],[0.37])
PlantWhenAvailable(6,25,(3,9))
PlantWhenAvailable(1,50,(1,6))

Prejudge(1,4)
WriteZombies([0,0],[1,6],[0.37,0.325])
PlantWhenAvailable(1,50,(1,7))
PlantWhenAvailable(3,50,(1,9))

Prejudge(1,5)
WriteZombies([2],[1],[0.37])
PlantWhenAvailable(7,125,(1,9))
PlantWhenAvailable(1,50,(1,8))
PlantWhenAvailable(4,25,(2,9))

Prejudge(1,6)
WriteZombies([2],[3],[0.37])

Prejudge(1,7)
WriteZombies([0,2],[3,5],[0.37,0.37])
PlantWhenAvailable(5,150,(5,9))

Prejudge(1,8)
WriteZombies([0,2],[2,2],[0.37,0.37])
PlantWhenAvailable(3,50,(1,9))
PlantWhenAvailable(1,50,(2,1))


Prejudge(1,9)
WriteZombies([0,2],[1,1],[0.37,0.37])
PlantWhenAvailable(1,50,(2,2))
PlantWhenAvailable(4,25,(2,9))
Delay(290)
use_shovel(6,1)

Prejudge(1,10)
WriteZombies([0,0,0,0,0,0,0,1,2],[4,4,4,4,6,6,6,6,6],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37])
PlantWhenAvailable(1,50,(2,3))
PlantWhenAvailable(2,25,(3,9))
PlantWhenAvailable(5,150,(3,9))

Prejudge(1,11)
WriteZombies([0,14],[3,3],[0.37,0.91])

Prejudge(1,12)
WriteZombies([2,2],[6,6],[0.37,0.37])
use_shovel(5,9)
PlantWhenAvailable(7,125,(6,9))
PlantWhenAvailable(3,50,(5,9))

Prejudge(1,13)
WriteZombies([0,2,2],[3,3,3],[0.37,0.37,0.37])
PlantWhenAvailable(4,25,(1,9))

Prejudge(1,14)
WriteZombies([0,2,2],[2,2,2],[0.37,0.37,0.37])
Delay(410)
PlantWhenAvailable(5,150,(2,9))

Prejudge(1,15)
WriteZombies([0,2,2],[5,5,5],[0.37,0.37,0.37])

Prejudge(1,16)
WriteZombies([2,2,2],[2,4,6],[0.37,0.37,0.37])
PlantWhenAvailable(5,150,(6,9))

Prejudge(1,17)
WriteZombies([2,2,2],[1,1,1],[0.37,0.37,0.37])
PlantWhenAvailable(3,50,(5,9))

Prejudge(1,18)
WriteZombies([14,14],[4,4],[0.91,0.91])

Prejudge(1,19)
WriteZombies([0,2,2,2],[5,5,5,5],[0.37,0.37,0.37,0.37])
PlantWhenAvailable(5,150,(5,9))

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,1,2,14,14],[3,3,3,3,3,3,3,3,3,3,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.91,0.91])
SetAmbushZombies([(3,8),(3,7),(3,6)])
Prejudge(205,20)
PlantWhenAvailable(2,25,(3,9))
PlantWhenAvailable(7,125,(3,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)