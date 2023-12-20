from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock([0,1,2,3,4,6])
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:251] = [4,-1]
waves[300:303] = [0,0,0,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:458] = [0,0,0,0,0,1,2,4,-1]
waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(10)
PlantWhenAvailable(2,50,(2,5))

Prejudge(1,1)
WriteZombies([0],[2],[0.37])
Delay(75)
PlantWhenAvailable(1,100,(2,7))

Prejudge(0,2)
WriteZombies([0],[2],[0.32])
Delay(75)
PlantWhenAvailable(1,100,(2,8))
PlantWhenAvailable(5,25,(4,9))

Prejudge(0,3)
WriteZombies([0],[2],[0.32])

Prejudge(0,4)
WriteZombies([0,0],[2,3],[0.37,0.317])
PlantWhenAvailable(1,100,(2,6))

Prejudge(0,5)
WriteZombies([0,0],[2,3],[0.37,0.37])

Prejudge(0,6)
WriteZombies([4],[4],[0.37,0.37])
PlantWhenAvailable(5,25,(1,9))

Prejudge(0,7)
WriteZombies([0,0,0],[2,2,3],[0.37,0.31,0.3])

Prejudge(0,8)
WriteZombies([0,2],[1,1],[0.37,0.37])

Prejudge(0,9)
WriteZombies([0,2],[3,3],[0.37,0.37])
Delay(100)
PlantWhenAvailable(3,150,(2,9))

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,4],[3,3,3,3,3,3,3,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37])

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)