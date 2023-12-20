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
select_seeds_and_lets_rock((1,16,17,4,6,19,20,2))
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1500)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:201] = [2,-1]
waves[250:251] = [2,-1]
waves[300:302] = [0,2,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:457] = [0,0,0,0,0,1,4,-1]
waves[500:501] = [4,-1]
waves[550:551] = [4,-1]
waves[600:602] = [0,4,-1]
waves[650:652] = [0,4,-1]
waves[700:702] = [0,4,-1]
waves[750:752] = [2,4,-1]
waves[800:802] = [2,4,-1]
waves[850:852] = [14,14,-1]
waves[900:901] = [12,-1]
waves[950:960] = [0,0,0,0,0,0,0,0,1,12,-1]
waves[1000:1001] = [12,-1]
waves[1050:1052] = [0,12,-1]
waves[1100:1102] = [0,12,-1]
waves[1150:1152] = [0,12,-1]
waves[1200:1202] = [2,12,-1]
waves[1250:1252] = [2,12,-1]
waves[1300:1302] = [2,12,-1]
waves[1350:1353] = [2,4,4,-1]
waves[1400:1402] = [2,4,4,-1]
waves[1450:1466] = [0,0,0,0,0,0,0,0,0,0,1,2,3,4,12,14,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(30)
SetGraves([(5,8)])

PlantWhenAvailable(1,50,(1,1))
PlantWhenAvailable(1,50,(1,2))
PlantWhenAvailable(1,50,(1,3))

Prejudge(1,1)
WriteZombies([0],[5],[0.37])
PlantWhenAvailable(3,50,(6,9))
PlantWhenAvailable(1,50,(1,4))
PlantWhenAvailable(4,25,(1,8))

Prejudge(0,2)
WriteZombies([0],[6],[0.37])
PlantWhenAvailable(1,50,(1,5))

Prejudge(0,3)
WriteZombies([0],[1],[0.37])
PlantWhenAvailable(6,25,(3,9))
PlantWhenAvailable(1,50,(1,6))

Prejudge(0,4)
WriteZombies([0,0],[1,6],[0.37,0.325])
PlantWhenAvailable(1,50,(1,7))
PlantWhenAvailable(7,125,(1,9))

Prejudge(0,5)
WriteZombies([2],[1],[0.37])
PlantWhenAvailable(3,50,(1,9))
PlantWhenAvailable(1,50,(1,8))

Prejudge(0,6)
WriteZombies([2],[3],[0.37])
PlantWhenAvailable(4,25,(2,9))

Prejudge(0,7)
WriteZombies([0,2],[3,5],[0.37,0.37])
PlantWhenAvailable(5,150,(5,9))
PlantWhenAvailable(1,50,(6,8))

Prejudge(0,8)
WriteZombies([0,2],[2,2],[0.37,0.37])
Delay(350)
PlantWhenAvailable(6,25,(3,9))

Prejudge(0,9)
WriteZombies([0,2],[1,1],[0.37,0.37])
PlantWhenAvailable(1,50,(6,7))
PlantWhenAvailable(3,50,(1,9))
PlantWhenAvailable(4,25,(2,9))
PlantWhenAvailable(1,50,(6,6))

Prejudge(0,10)
WriteZombies([0,0,0,0,0,1,4],[4,4,4,4,4,6,6],[0.37,0.37,0.37,0.37,0.37,0.45,0.37])
PlantWhenAvailable(1,50,(6,5))

Prejudge(0,11)
WriteZombies([4],[5],[0.37])
use_shovel(5,9)
PlantWhenAvailable(5,150,(5,9))
PlantWhenAvailable(1,50,(6,4))

Prejudge(0,12)
WriteZombies([4],[6],[0.37])
use_shovel(5,9)
PlantWhenAvailable(7,125,(6,9))
PlantWhenAvailable(6,25,(3,8))

Prejudge(0,13)
WriteZombies([0,4],[3,3],[0.37,0.37])
PlantWhenAvailable(1,50,(6,3))
PlantWhenAvailable(3,50,(5,9))

Prejudge(0,14)
WriteZombies([0,4],[2,2],[0.37,0.37])
PlantWhenAvailable(4,25,(1,9))
PlantWhenAvailable(1,50,(6,2))

Prejudge(0,15)
WriteZombies([0,4],[5,5],[0.37,0.37])
PlantWhenAvailable(5,150,(2,9))
PlantWhenAvailable(1,50,(6,1))

Prejudge(0,16)
WriteZombies([2,4],[6,2],[0.37,0.37])
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,17)
WriteZombies([2,4],[1,1],[0.37,0.37])

Prejudge(0,18)
WriteZombies([14,14],[4,4],[0.68,0.68])
PlantWhenAvailable(2,25,(4,9))
PlantWhenAvailable(3,50,(4,9))

Prejudge(0,19)
WriteZombies([12],[6],[0.37])
use_shovel(6,9)
PlantWhenAvailable(4,25,(5,9))
PlantWhenAvailable(5,150,(6,9))
use_shovel(2,9)
Delay(500)
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,20)
WriteZombies([0,0,0,0,0,0,0,0,1,12],[2,2,2,2,2,1,1,1,2,1],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37])
Delay(215)
PlantWhenAvailable(7,125,(1,9))

Prejudge(0,21)
WriteZombies([12],[6],[0.37])
Delay(110)
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,22)
WriteZombies([0,12],[2,6],[0.37,0.37])
Delay(205)
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,23)
WriteZombies([0,12],[2,6]),[0.37,0.37]
Delay(310)
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,24)
WriteZombies([0,12],[2,6],[0.37,0.37])

Prejudge(0,25)
WriteZombies([2,12],[2,5],[0.37,0.37])
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,26)
WriteZombies([2,12],[2,6],[0.37,0.37])
PlantWhenAvailable(3,50,(5,9))
PlantWhenAvailable(4,25,(1,9))

Prejudge(0,27)
WriteZombies([2,12],[3,6],[0.37,0.37])
use_shovel(6,9)
PlantWhenAvailable(5,150,(6,9))

Prejudge(0,28)
WriteZombies([2,4,4],[4,4,4],[0.37,0.37,0.37])

Prejudge(0,29)
WriteZombies([2,4,4],[1,1,1],[0.37,0.37,0.37])
PlantWhenAvailable(6,25,(3,9))
use_shovel(6,8)
PlantWhenAvailable(5,150,(6,8))

Prejudge(1,30)
start = time.time()
WriteZombies([0,0,0,0,0,0,0,0,0,0,1,2,3,4,12,14],[2,3,4,2,3,4,2,3,4,2,3,4,2,3,2,4],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.68,0.37,0.37,0.91])
print(time.time()-start)
SetAmbushZombies([(3,8),(4,8),(4,9)])
use_shovel(3,9)
PlantWhenAvailable(2,25,(3,9))
Prejudge(220,30)
PlantWhenAvailable(8,150,(3,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)