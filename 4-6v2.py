from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
start_time = time.time()
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock([9,8,24,16,17,4,13,15])
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:252] = [0,0,-1]
waves[300:301] = [17,-1]
waves[350:353] = [0,0,0,-1]
waves[400:403] = [0,0,0,-1]
waves[450:457] = [0,0,0,0,1,2,17,-1]
waves = tuple(waves)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(10)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
SetGraves([(1,8)])

PlantWhenAvailable(1,25,(1,1))
PlantWhenAvailable(2,0,(1,9))
PlantWhenAvailable(1,25,(1,2))
PlantWhenAvailable(2,0,(1,8))
PlantWhenAvailable(1,25,(2,1))
PlantWhenAvailable(2,0,(1,7))

Prejudge(1,1)
WriteZombies([0],[1])
PlantWhenAvailable(3,0,(3,7))
PlantWhenAvailable(2,0,(2,9))

Prejudge(0,2)
WriteZombies([0],[1])
PlantWhenAvailable(1,25,(2,2))

Prejudge(0,3)
WriteZombies([0],[1])
PlantWhenAvailable(2,0,(2,8))
PlantWhenAvailable(1,25,(2,3))


Prejudge(0,4)
WriteZombies([0,0],[1,2])
PlantWhenAvailable(2,0,(2,7))
PlantWhenAvailable(6,25,(6,9))

Prejudge(0,5)
WriteZombies([0,0],[1,2])
PlantWhenAvailable(2,0,(1,6))

Prejudge(0,6)
WriteZombies([0,0],[1,2])
PlantWhenAvailable(3,0,(3,8))
PlantWhenAvailable(2,0,(1,9))

Prejudge(0,7)
WriteZombies([17],[6])

Prejudge(0,8)
WriteZombies([0,0,0],[1,2,3])
PlantWhenAvailable(4,25,(3,9))
PlantWhenAvailable(2,0,(3,9))

Prejudge(0,9)
WriteZombies([0,0,0],[1,2,3])
PlantWhenAvailable(2,0,(2,9))

Prejudge(1,10)
WriteZombies([0,0,0,0,1,2,17],[1,2,3,4,5,5,1])
SetAmbushZombies([(3,9),(4,9),(4,8)])
use_shovel(2,9)
Prejudge(200,10)
PlantWhenAvailable(8,125,(2,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)