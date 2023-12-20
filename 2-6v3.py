from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
import os

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
SetGraves([(2,9),(4,9),(4,8),(3,9),(3,8),(3,7),(3,6)])
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock([9,1,4,3,11,8,2])

waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:251] = [7,-1]
waves[300:303] = [0,0,0,-1]
waves[350:353] = [0,0,0,-1]
waves[400:403] = [0,0,0,-1]
waves[450:457] = [0,0,0,0,1,2,7,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(10)

PlantWhenAvailable(1,25,(1,1))
PlantWhenAvailable(6,0,(1,9))
PlantWhenAvailable(1,25,(1,2))
PlantWhenAvailable(6,0,(1,8))
PlantWhenAvailable(1,25,(1,3))
PlantWhenAvailable(6,0,(1,7))

Prejudge(1,1)
WriteZombies([0],[1],[0.37])
PlantWhenAvailable(6,0,(2,8))

Prejudge(0,2)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(3,25,(5,9))

Prejudge(0,3)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(6,0,(2,7))

Prejudge(0,4)
WriteZombies([0,0],[1,3],[0.23,0.325])
PlantWhenAvailable(6,0,(2,6))

Prejudge(0,5)
WriteZombies([0,0],[1,4],[0.23,0.37])
PlantWhenAvailable(6,0,(1,6))

Prejudge(0,6)
WriteZombies([7],[5],[0.68])

Prejudge(0,7)
WriteZombies([0,0,0],[1,2,3],[0.3,0.37,0.37])
PlantWhenAvailable(3,25,(5,9))

Prejudge(0,8)
WriteZombies([0,0,0],[1,2,4],[0.23,0.37,0.37])
PlantWhenAvailable(6,0,(4,7))

Prejudge(0,9)
WriteZombies([0,0,0],[5,5,5],[0.37,0.37,0.37])
PlantWhenAvailable(5,75,(2,9))

Prejudge(1,10)
WriteZombies([0,0,0,0,1,2,7],[3,3,3,3,3,3,3],[0.37,0.37,0.37,0.37,0.45,0.37,0.68])

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)