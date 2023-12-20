from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
SetGraves([(5,9),(4,9),(3,9),(5,8),(4,8),(3,8),(5,7),(3,7),(5,6),(3,6),(3,5)])
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock([9,8,1,2,4,10,11])
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:252] = [0,0,-1]
waves[300:303] = [0,0,0,-1]
waves[350:353] = [0,0,0,-1]
waves[400:402] = [0,2,-1]
waves[450:458] = [0,0,0,0,0,1,2,2,-1]
waves[500:501] = [6,-1]
waves[550:551] = [6,-1]
waves[600:605] = [0,0,0,0,0,-1]
waves[650:655] = [0,0,0,0,0,-1]
waves[700:705] = [0,0,0,0,0,-1]
waves[750:756] = [0,0,0,0,0,0,-1]
waves[800:806] = [0,0,0,0,0,0,-1]
waves[850:856] = [0,0,0,0,0,0,-1]
waves[900:901] = [7,-1]
waves[950:961] = [0,0,0,0,0,0,0,1,2,6,7,-1]
waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastPlants()
thirtyFiveRule(20)

PlantWhenAvailable(1,25,(1,1))
PlantWhenAvailable(2,0,(1,9))
PlantWhenAvailable(1,25,(1,2))
PlantWhenAvailable(2,0,(1,8))
PlantWhenAvailable(1,25,(1,3))
PlantWhenAvailable(2,0,(1,7))

Prejudge(1,1)
WriteZombies([0],[1],[0.37])
PlantWhenAvailable(2,0,(2,9))

Prejudge(0,2)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(1,25,(1,4))

Prejudge(0,3)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(2,0,(2,8))
PlantWhenAvailable(1,25,(1,5))

Prejudge(0,4)
WriteZombies([0,0],[1,2],[0.23,0.37])
PlantWhenAvailable(2,0,(2,7))

Prejudge(0,5)
WriteZombies([0,0],[1,2],[0.23,0.23])
PlantWhenAvailable(1,25,(2,1))
PlantWhenAvailable(2,0,(4,7))
use_shovel(2,9)
PlantWhenAvailable(5,25,(2,9))

Prejudge(0,6)
WriteZombies([0,0],[1,5],[0.23,0.36])
PlantWhenAvailable(1,25,(2,2))
PlantWhenAvailable(2,0,(4,6))

Prejudge(0,7)
WriteZombies([0,0,0],[1,3,4],[0.23,0.37,0.37])
PlantWhenAvailable(1,25,(2,3))
PlantWhenAvailable(3,50,(2,4))

Prejudge(0,8)
WriteZombies([0,0,0],[1,3,4],[0.23,0.37,0.37])
PlantWhenAvailable(2,0,(4,5))
PlantWhenAvailable(1,25,(2,5))

Prejudge(0,9)
WriteZombies([0,2],[2,2],[0.37,0.37])
PlantWhenAvailable(1,25,(4,1))
PlantWhenAvailable(3,50,(4,2))
PlantWhenAvailable(5,25,(2,9))
PlantWhenAvailable(1,25,(4,3))
PlantWhenAvailable(3,50,(4,4))

Prejudge(0,10)
WriteZombies([0,0,0,0,0,2,2,1],[2,2,2,2,2,2,2,4],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45])
use_shovel(4,5)
PlantWhenAvailable(1,25,(4,5))
Delay(300)
use_shovel(1,8)
PlantWhenAvailable(6,75,(1,8))

Prejudge(0,11)
WriteZombies([6],[5],[0.37])

Prejudge(0,12)
WriteZombies([6],[3],[0.37])
PlantWhenAvailable(2,0,(2,9))
use_shovel(1,7)
PlantWhenAvailable(6,75,(1,7))

Prejudge(0,13)
WriteZombies([0,0,0,0,0],[1,1,1,1,2],[0.37,0.37,0.37,0.37,0.23])
use_shovel(1,6)
PlantWhenAvailable(6,75,(1,6))

Prejudge(0,14)
WriteZombies([0,0,0,0,0],[1,1,1,1,1],[0.37,0.37,0.37,0.37,0.37])
PlantWhenAvailable(7,75,(3,5))

Prejudge(0,15)
WriteZombies([0,0,0,0,0],[1,1,1,1,1],[0.37,0.37,0.37,0.37,0.37])
PlantWhenAvailable(7,75,(3,6))

Prejudge(0,16)
WriteZombies([0,0,0,0,0,0],[1,1,1,1,1,1],[0.37,0.37,0.37,0.37,0.37,0.37])
use_shovel(2,9)
PlantWhenAvailable(5,25,(2,9))
PlantWhenAvailable(7,75,(3,7))

Prejudge(0,17)
WriteZombies([0,0,0,0,0,0],[1,1,1,1,1,1],[0.37,0.37,0.37,0.37,0.37,0.37])

Prejudge(0,18)
WriteZombies([0,0,0,0,0,0],[1,1,1,1,1,1],[0.37,0.37,0.37,0.37,0.37,0.37])
PlantWhenAvailable(7,75,(5,6))

Prejudge(0,19)
WriteZombies([7],[2],[0.68])
PlantWhenAvailable(7,75,(5,7))
PlantWhenAvailable(7,75,(4,9))

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,1,2,6,7],[5,3,4,5,3,4,5,3,4,5,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.37,0.68])
Prejudge(235,20)
PlantWhenAvailable(4,150,(4,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)