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
SetGraves([(2,9),(4,9),(4,8),(4,7)])
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock([9,8,1,2,4,6])
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:252] = [0,0,-1]
waves[300:303] = [0,0,0,-1]
waves[350:353] = [0,0,0,-1]
waves[400:402] = [0,5,-1]
waves[450:458] = [0,0,0,0,0,1,2,2,-1]
waves[500:504] = [0,0,0,0,-1]
waves[550:554] = [0,0,0,0,-1]
waves[600:602] = [0,4,-1]
waves[650:652] = [0,4,-1]
waves[700:702] = [0,4,-1]
waves[750:756] = [0,0,0,0,0,0,-1]
waves[800:806] = [0,0,0,0,0,0,-1]
waves[850:852] = [2,4,-1]
waves[900:903] = [0,2,4,-1]
waves[950:961] = [0,0,0,0,0,0,0,1,2,4,5,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(20)

PlantWhenAvailable(1,25,(1,1))
PlantWhenAvailable(2,0,(1,9))
PlantWhenAvailable(1,25,(1,2))
PlantWhenAvailable(2,0,(1,8))
PlantWhenAvailable(1,25,(1,3))
PlantWhenAvailable(2,0,(1,7))

Prejudge(1,1)
WriteZombies([0],[1],[0.37])
PlantWhenAvailable(2,0,(5,9))

Prejudge(0,2)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(1,25,(1,4))

Prejudge(0,3)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(2,0,(5,8))
PlantWhenAvailable(1,25,(1,5))

Prejudge(0,4)
WriteZombies([0,0],[1,5],[0.23,0.37])
PlantWhenAvailable(2,0,(5,7))
PlantWhenAvailable(5,25,(3,9))

Prejudge(0,5)
WriteZombies([0,0],[1,5],[0.23,0.23])
PlantWhenAvailable(2,0,(3,8))

Prejudge(0,6)
WriteZombies([0,0],[1,5],[0.23,0.23])
PlantWhenAvailable(1,25,(5,1))
PlantWhenAvailable(2,0,(3,7))

Prejudge(0,7)
WriteZombies([0,0,0],[1,2,5],[0.23,0.345,0.23])
PlantWhenAvailable(3,50,(5,2))

Prejudge(0,8)
WriteZombies([0,0,0],[1,4,5],[0.23,0.23,0.23])
PlantWhenAvailable(1,25,(5,3))
PlantWhenAvailable(3,50,(5,4))

Prejudge(0,9)
WriteZombies([0,5],[3,3],[0.37,0.37,0.37])
Delay(50)
PlantWhenAvailable(2,0,(2,8))
Delay(310)
PlantWhenAvailable(5,25,(3,9))
Delay(150)
PlantWhenAvailable(2,0,(2,7))
PlantWhenAvailable(1,25,(5,5))

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,2],[3,3,3,3,3,2,3,3],[0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.37])
PlantWhenAvailable(3,50,(3,1))
PlantWhenAvailable(2,0,(2,6))
PlantWhenAvailable(1,25,(3,2))

Prejudge(1,11)
WriteZombies([0,0,0,0],[1,2,3,5],[0.23,0.37,0.23,0.23])
PlantWhenAvailable(3,50,(3,3))
PlantWhenAvailable(2,0,(3,9))
PlantWhenAvailable(1,25,(3,4))

Prejudge(1,12)
WriteZombies([0,0,0,0],[1,2,3,5],[0.23,0.37,0.23,0.23])
Delay(350)
use_shovel(3,9)
PlantWhenAvailable(5,25,(3,9))

Prejudge(1,13)
WriteZombies([0,4],[2,2],[0.37,0.37])
use_shovel(5,9)
PlantWhenAvailable(2,0,(5,9))

Prejudge(1,14)
WriteZombies([0,4],[4,1],[0.25,0.37])
use_shovel(1,9)
PlantWhenAvailable(6,150,(1,9))
Delay(150)
use_shovel(1,9)
PlantWhenAvailable(2,0,(1,9))

Prejudge(1,15)
WriteZombies([0,4],[3,3],[0.37,0.37])

Prejudge(1,16)
WriteZombies([0,0,0,0,0,0],[1,2,3,4,4,5],[0.23,0.37,0.23,0.37,0.37,0.23])
PlantWhenAvailable(1,25,(4,1))
PlantWhenAvailable(2,0,(3,9))

Prejudge(1,17)
WriteZombies([0,0,0,0,0,0],[1,2,3,4,4,5],[0.23,0.37,0.23,0.37,0.37,0.23])
Delay(200)
PlantWhenAvailable(2,0,(4,1))
Delay(305)
PlantWhenAvailable(1,25,(4,1))

Prejudge(1,18)
WriteZombies([2,4],[4,1],[0.37,0.37])
use_shovel(1,9)
PlantWhenAvailable(6,150,(1,9))

Prejudge(1,19)
WriteZombies([0,2,4],[4,4,4],[0.37,0.37,0.37])
use_shovel(3,9)
PlantWhenAvailable(6,150,(4,6))

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,1,2,4,5],[2,3,4,2,3,4,2,3,4,2,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37])
Prejudge(235,20)
PlantWhenAvailable(4,150,(3,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)