from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:201] = [2,-1]
waves[250:252] = [0,0,-1]
waves[300:302] = [0,2,-1]
waves[350:356] = [0,0,0,0,1,2,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(8)

PlantWhenAvailable(2,50,(3,1))

Prejudge(1,1)
WriteZombies([0],[3],[0.36])
Delay(70)
PlantWhenAvailable(1,100,(3,7))

Prejudge(1,2)
WriteZombies([0],[3],[0.3])
Delay(70)
PlantWhenAvailable(1,100,(3,8))

Prejudge(1,3)
WriteZombies([0],[3],[0.37])

Prejudge(1,4)
WriteZombies([0,0],[3,4],[0.37,0.37])
PlantWhenAvailable(1,100,(3,6))

Prejudge(1,5)
WriteZombies([2],[3],[0.23])

Prejudge(1,6)
WriteZombies([0,0],[3,4],[0.27,0.37])

Prejudge(1,7)
WriteZombies([0,2],[3,3],[0.37,0.37])
PlantWhenAvailable(3,150,(3,9))

Prejudge(1,8)
WriteZombies([0,0,0,0,1,2],[4,4,4,4,4,4],[0.37,0.37,0.37,0.37,0.45,0.37])

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)
