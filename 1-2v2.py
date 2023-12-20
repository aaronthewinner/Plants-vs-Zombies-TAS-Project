from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150] = 0
waves[151] = 0
waves[152] = -1
waves[200] = 0
waves[201] = 0
waves[202] = -1
waves[250:255] = [0,0,0,0,1,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(6)

PlantWhenAvailable(2,50,(3,1))
PlantWhenAvailable(2,50,(3,2))
PlantWhenAvailable(2,50,(3,3))

Prejudge(1,1)
WriteZombies([0],[3],[0.37])
Delay(75)
PlantWhenAvailable(1,100,(3,7))

Prejudge(0,2)
WriteZombies([0],[4],[0.35])
Delay(75)
PlantWhenAvailable(1,100,(4,8))

Prejudge(0,3)
WriteZombies([0],[3],[0.32])
PlantWhenAvailable(1,100,(3,8))

Prejudge(0,4)
WriteZombies([0,0],[3,4],[0.37,0.37])

Prejudge(0,5)
WriteZombies([0,0],[3,3],[0.35,0.37])
Delay(75)
PlantWhenAvailable(1,100,(3,6))

Prejudge(1,6)
WriteZombies([0,0,0,0,1],[4,4,4,4,4],[0.37,0.37,0.37,0.37,0.45])

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)