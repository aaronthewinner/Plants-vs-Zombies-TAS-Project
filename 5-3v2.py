from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:151] = [0,0,-1]
waves[200:202] = [2,-1]
waves[250:252] = [2,-1]
waves[300:302] = [0,2,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:458] = [0,0,0,0,0,1,2,2,-1]
waves[500:501] = [21,-1]
waves[550:551] = [21,-1]
waves[600:603] = [0,2,2,-1]
waves[650:652] = [0,21,-1]
waves[700:702] = [0,21,-1]
waves[750:752] = [2,21,-1]
waves[800:803] = [2,2,2,-1]
waves[850:852] = [2,21,-1]
waves[900:904] = [0,2,2,2,-1]
waves[950:962] = [0,0,0,0,0,0,0,0,1,2,2,21,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock((1,33,17,4,6,2,20,32,0))

while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(20)
SetGraves([(3,8)])

PlantWhenAvailable(1,50,(1,1))
use_shovel(5,1)
use_shovel(5,2)
use_shovel(5,3)
PlantWhenAvailable(1,50,(1,2))
PlantWhenAvailable(1,50,(1,3))

Prejudge(1,1)
WriteZombies([0],[3],[0.37])
PlantWhenAvailable(1,50,(2,1))

Prejudge(1,2)
WriteZombies([0],[2],[0.37])
PlantWhenAvailable(8,100,(2,2))
PlantWhenAvailable(2,25,(4,9))
PlantWhenAvailable(4,25,(4,9))

Prejudge(1,3)
WriteZombies([0],[2],[0.37])
PlantWhenAvailable(8,100,(2,3))
PlantWhenAvailable(2,25,(3,9))

Prejudge(1,4)
WriteZombies([0,0],[2,5],[0.37,0.33])
PlantWhenAvailable(3,50,(3,9))
PlantWhenAvailable(1,50,(3,1))
PlantWhenAvailable(2,25,(1,9))
PlantWhenAvailable(4,25,(1,9))

Prejudge(1,5)
WriteZombies([2],[4],[0.37])
PlantWhenAvailable(1,50,(3,2))

Prejudge(1,6)
WriteZombies([2],[3],[0.37])
PlantWhenAvailable(1,50,(3,3))

Prejudge(1,7)
WriteZombies([0,2],[1,1],[0.37,0.37])


Prejudge(1,8)
WriteZombies([0,2],[3,3],[0.37,0.37])
PlantWhenAvailable(1,50,(4,1))
PlantWhenAvailable(3,50,(3,9))

Prejudge(1,9)
WriteZombies([0,2],[3,3],[0.37,0.37])
PlantWhenAvailable(7,125,(3,9))
PlantWhenAvailable(4,25,(1,9))
PlantWhenAvailable(1,50,(4,2))
PlantWhenAvailable(1,50,(4,3))

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,2],[5,5,5,5,5,5,5,5],[0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.37])

Prejudge(1,11)
WriteZombies([21],[3],[0.81])
PlantWhenAvailable(5,150,(3,9))
PlantWhenAvailable(3,50,(4,9))

Prejudge(1,12)
WriteZombies([21],[4],[0.81])

Prejudge(1,13)
WriteZombies([0,2,2],[1,1,1],[0.37,0.37,0.37])
PlantWhenAvailable(4,25,(4,9))

Prejudge(1,14)
WriteZombies([0,21],[2,3],[0.37,0.81])
use_shovel(3,9)
PlantWhenAvailable(5,150,(3,9))

Prejudge(1,15)
WriteZombies([0,21],[2,3],[0.37,0.81])
Delay(95)
use_shovel(3,9)
PlantWhenAvailable(5,150,(3,9))

Prejudge(1,16)
WriteZombies([2,21],[4,2],[0.37,0.81])
PlantWhenAvailable(3,50,(1,9))

Prejudge(1,17)
WriteZombies([2,2,2],[1,1,1],[0.37,0.37,0.37])
use_shovel(2,3)
use_shovel(2,3)
use_shovel(2,2)
use_shovel(2,2)

Prejudge(1,18)
WriteZombies([2,21],[3,3],[0.37,0.81])
use_shovel(3,9)
Delay(100)
PlantWhenAvailable(7,125,(3,9))
use_shovel(2,1)
use_shovel(2,1)

Prejudge(1,19)
WriteZombies([0,2,2,2],[2,2,2,2],[0.37,0.37,0.37,0.37])

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,0,1,2,2,21],[3,4,2,3,4,2,3,4,2,3,4,2],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.37,0.81])
SetAmbushZombies([(3,8),(4,8),(2,8)])
use_shovel(3,9)
use_shovel(4,9)
PlantWhenAvailable(2,25,(3,8))
Delay(550)
PlantWhenAvailable(6,150,(3,8))

while(game_ui() == 3):
   Sleep(1)
print(time.time()-start_time)