from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(0.1)

update_game_scene()
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(0.1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(4)

PlantWhenAvailable(1,100,(3,8))
start_time = time.time()
PlantWhenAvailable(1,100,(3,7))

Prejudge(1,1)
WriteZombies([0],[3],[0.37])

Prejudge(0,2)
WriteZombies([0],[3],[0.37])

Prejudge(0,3)
WriteZombies([0],[3],[0.37])
PlantWhenAvailable(1,100,(3,6))

Prejudge(0,4)
WriteZombies([0,0],[3,3],[0.34,0.37])

while(game_ui() == 3):
    Sleep(0.1)
print(time.time()-start_time)