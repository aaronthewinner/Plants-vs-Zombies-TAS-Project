from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *

while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(5):
    safe_click()
    LeftClick(300,300) 
Sleep(1)

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock([1,0,16,4,2,6,3])
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:252] = [0,0,-1]
waves[300:303] = [0,0,0,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:458] = [0,0,0,0,0,1,2,2,-1]
waves = tuple(waves)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(10)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)

PlantWhenAvailable(1,50,(2,1))

Prejudge(1,1)
WriteZombies([0],[2])
Delay(75)
PlantWhenAvailable(2,100,(2,7))

Prejudge(0,2)
WriteZombies([0],[2])
PlantWhenAvailable(2,100,(2,8))
PlantWhenAvailable(4,25,(1,9))

Prejudge(0,3)
WriteZombies([0],[2])

Prejudge(0,4)
WriteZombies([0,0],[2,5])
PlantWhenAvailable(2,100,(2,6))

Prejudge(0,5)
WriteZombies([0,0],[2,5])

Prejudge(0,6)
WriteZombies([0,0],[2,5])
PlantWhenAvailable(4,25,(6,9))

Prejudge(0,7)
WriteZombies([0,0,0],[2,2,5])

Prejudge(0,8)
WriteZombies([0,2],[1,1])

Prejudge(0,9)
WriteZombies([0,2],[6,6])

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,2],[2,3,4,2,3,4,2,3])
SetAmbushZombies([(3,8),(4,8)])
Prejudge(205,10)
PlantWhenAvailable(3,25,(3,9))
PlantWhenAvailable(5,150,(3,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)