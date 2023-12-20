from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(0.1)
start_time = time.time()
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(7):
    safe_click()
    LeftClick(300,300) 
Sleep(1)



SetGraves([(5,9),(3,9),(3,8),(3,7)])
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock([0,1,2,3,4,8])
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:251] = [5,-1]
waves[300:303] = [0,0,0,-1]
waves[350:353] = [0,0,0,-1]
waves[400:403] = [0,0,0,-1]
waves[450:459] = [0,0,0,0,0,0,0,1,5,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(10)

PlantWhenAvailable(6,0,(1,9))
PlantWhenAvailable(6,0,(1,8))
PlantWhenAvailable(6,0,(1,7))

Prejudge(1,1)
WriteZombies([0],[1],[0.37])
PlantWhenAvailable(6,0,(5,8))

Prejudge(0,2)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(5,25,(4,9))

Prejudge(0,3)
WriteZombies([0],[5],[0.305])
PlantWhenAvailable(6,0,(5,7))
Prejudge(-200,4)
use_shovel((5,8),(5,7))
Prejudge(0,4)
WriteZombies([0,0],[1,3],[0.3,0.35])
PlantWhenAvailable(6,0,(2,7))

Prejudge(0,5)
WriteZombies([0,0],[1,2],[0.3,0.37])
PlantWhenAvailable(6,0,(2,8))
Prejudge(0,6)
WriteZombies([5],[4])
PlantWhenAvailable(6,0,(5,7))
Prejudge(0,7)
WriteZombies([0,0,0],[1,2,5],[0.37,0.37,0.37])
PlantWhenAvailable(5,25,(4,9))
PlantWhenAvailable(6,0,(5,8))




Prejudge(0,8)
WriteZombies([0,0,0],[1,2,5],[0.23,0.37,0.37])
PlantWhenAvailable(6,0,(2,9))


Prejudge(0,9)
WriteZombies([0,0,0],[4,4,4],[0.37,0.37,0.37])
PlantWhenAvailable(6,0,(5,6))

Prejudge(1,10)
WriteZombies([0,0,0,0,0,0,0,1,5],[3,3,3,3,3,3,3,3,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37])

while(game_ui() == 3):
    Sleep(0.1)
print(time.time()-start_time)