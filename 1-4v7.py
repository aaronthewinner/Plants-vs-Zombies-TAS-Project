from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(0.1)
start_time = time.time()
update_game_scene()
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1] #4
waves[200:202] = [0,0,-1] #5
waves[250:252] = [0,0,-1] #6
waves[300:303] = [0,0,0,-1] #7
waves[350:353] = [0,0,0,-1] #8
waves[400:402] = [0,2,-1] #9
waves[450:458] = [0,0,0,0,0,1,2,2,-1] #10

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(10)
PlantWhenAvailable(2,50,(3,5))
Prejudge(1,1)
WriteZombies([0],[3],[0.37])
Delay(75)
PlantWhenAvailable(1,100,(3,7))

Prejudge(0,2)
WriteZombies([0],[3],[0.3])
Delay(80)
PlantWhenAvailable(1,100,(3,8))

Prejudge(0,3)
WriteZombies([0],[3],[0.37])

Prejudge(0,4)
WriteZombies([0,0],[3,4],[0.37,0.297])
PlantWhenAvailable(1,100,(3,6))

Prejudge(0,5)
WriteZombies([0,0],[3,4],[0.37,0.358])

Prejudge(0,6)
WriteZombies([0,0],[3,4],[0.37,0.37])

Prejudge(0,7)
WriteZombies([0,0,0],[3,3,4],[0.37,0.3,0.37])

Prejudge(0,8)
WriteZombies([0,0,0],[3,3,4],[0.37,0.3,0.37])

Prejudge(0,9)
WriteZombies([0,2],[2,2],[0.37,0.37])
Delay(100)
PlantWhenAvailable(3,150,(2,9))

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,2],[4,4,4,4,4,4,4,4],[0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.37])

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)