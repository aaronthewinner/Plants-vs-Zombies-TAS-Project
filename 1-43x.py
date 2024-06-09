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
waves[150:152] = [2,-1] #4
waves[200:202] = [2,-1] #5
waves[250:252] = [2,-1] #6
waves[300:303] = [0,2,-1] #7
waves[350:353] = [0,2,-1] #8
waves[400:402] = [0,2,-1] #9
waves[450:458] = [0,0,0,0,0,1,2,2,-1] #10

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
WriteMemory("int",1,0x522598)
WriteMemory("int",1,0x522CB5)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(10)
Prejudge(1,1)
WriteZombies([0],[1],[0.23])
Prejudge(1,2)
WriteZombies([0],[1],[0.23])
Prejudge(1,3)
WriteZombies([0],[1],[0.23])
Prejudge(1,4)
WriteZombies([2],[2],[0.23])
Prejudge(1,5)
WriteZombies([2],[2],[0.23])
Prejudge(1,6)
WriteZombies([2],[2],[0.23])
Prejudge(1,7)
WriteZombies([0,2],[3,3],[0.23,0.23])
Prejudge(1,8)
WriteZombies([0,2],[3,3],[0.23,0.23])
Prejudge(1,9)
WriteZombies([0,2],[3,3],[0.23,0.23])
Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,2],[4,4,4,4,4,4,4,4],[0.23,0.23,0.23,0.23,0.23,0.45,0.23,0.23])
Prejudge(400,10)
PlantWhenAvailable(3,450,(4,9))