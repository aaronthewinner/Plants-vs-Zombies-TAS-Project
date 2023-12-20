from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
WriteMemory("int",1,0x522A11)
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(4):
    safe_click()
    LeftClick(300,300) 
Sleep(1)
    


update_game_scene()
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock((0,1,4,7,20,28,29,32))
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150] = 2
waves[151] = -1
waves[200] = 0
waves[201] = 0
waves[202] = -1
waves[300] = 0
waves[301] = 0
waves[302] = 0
waves[303] = -1
waves[350] = 0
waves[351] = 0
waves[352] = 0
waves[353] = -1
waves[400] = 0
waves[401] = 0
waves[402] = 0
waves[403] = -1

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(10)
SetGraves([(4,8)])

PlantWhenAvailable(2,50,(2,1))
PlantWhenAvailable(2,50,(3,1))
PlantWhenAvailable(2,50,(4,1))

Prejudge(1,1)
WriteZombies([0],[4],[0.37])
PlantWhenAvailable(2,50,(5,1))

Prejudge(1,2)
WriteZombies([0],[1],[0.37])
PlantWhenAvailable(1,100,(1,5))
PlantWhenAvailable(2,50,(2,2))

Prejudge(1,3)
WriteZombies([0],[5],[0.37])
PlantWhenAvailable(1,100,(5,5))

Prejudge(1,4)
WriteZombies([2],[3],[0.37,0.37])
PlantWhenAvailable(5,125,(3,5))

Prejudge(1,5)
WriteZombies([0,0],[1,5],[0.37,0.37])
PlantWhenAvailable(8, 100,(1,4))

Prejudge(1,6)
SetBungees([(3,9)])

Prejudge(1,7)
WriteZombies([0,0,0],[1,1,5],[0.37,0.37,0.37])
PlantWhenAvailable(7,125,(3,5))

Prejudge(1,8)
WriteZombies([0,0,0],[1,5,5],[0.37,0.37,0.37])
PlantWhenAvailable(8,100,(5,4))

Prejudge(1,9)
WriteZombies([0,0,0],[1,1,5],[0.37,0.37,0.37])
PlantWhenAvailable(8,100,(1,3))

Prejudge(1,10)
WriteZombies([0,0,0,0,1,2],[4,4,4,4,4,4],[0.37,0.37,0.37,0.37,0.45,0.37])
SetBungees([(4,8)])
SetAmbushZombies([(4,6),(4,7)])
Delay(550)
PlantWhenAvailable(5,125,(4,5))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)









