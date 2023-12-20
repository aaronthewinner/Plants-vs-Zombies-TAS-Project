from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
    

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
SetGraves([(5,9),(3,9),(5,8),(2,9),(2,8),(2,7),(2,6)])
Sleep(350)
select_seeds_and_lets_rock([9,1,10,3,4,8,2])

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
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(10)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)


PlantWhenAvailable(1,25,(1,1))
PlantWhenAvailable(6,0,(1,9))
PlantWhenAvailable(1,25,(1,2))
PlantWhenAvailable(6,0,(1,8))
PlantWhenAvailable(1,25,(1,3))
PlantWhenAvailable(6,0,(1,7))

Prejudge(1,1)
WriteZombies([0],[1])
PlantWhenAvailable(6,0,(3,8))

Prejudge(0,2)
WriteZombies([0],[1])
PlantWhenAvailable(1,25,(1,4))

Prejudge(0,3)
WriteZombies([0],[1])
PlantWhenAvailable(6,0,(3,7))
PlantWhenAvailable(5,25,(4,9))

Prejudge(0,4)
WriteZombies([0,0],[1,3])
PlantWhenAvailable(6,0,(3,6))

Prejudge(0,5)
WriteZombies([0,0],[2,1])
PlantWhenAvailable(6,0,(1,6))

Prejudge(0,6)
WriteZombies([7],[4])
PlantWhenAvailable(6,0,(1,9))

Prejudge(0,7)
WriteZombies([0,0,0],[1,2,3])
PlantWhenAvailable(6,0,(4,9))

Prejudge(0,8)
WriteZombies([0,0,0],[1,2,3])
PlantWhenAvailable(6,0,(4,8))

Prejudge(0,9)
WriteZombies([0,0,0],[1,3,4])
PlantWhenAvailable(6,0,(4,7))
PlantWhenAvailable(6,0,(2,1))

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,7],[3,4,5,3,4,5,3,4])
use_shovel(4,9)
Prejudge(250,10)
PlantWhenAvailable(7,150,(4,9))
while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)