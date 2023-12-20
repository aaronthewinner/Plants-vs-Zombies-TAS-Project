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
waves[500:502] = [0,20,-1]
waves[550:552] = [0,20,-1]
waves[600:602] = [2,20,-1]
waves[650:652] = [2,20,-1]
waves[700:702] = [2,20,-1]
waves[750:752] = [20,20,-1]
waves[800:802] = [20,20,-1]
waves[850:852] = [20,20,-1]
waves[900:902] = [4,20,-1]
waves[950:961] = [0,0,0,0,0,0,0,1,2,3,4,20,-1]

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
use_shovel(5,4)
use_shovel(4,1)
use_shovel(4,2)
use_shovel(4,3)
use_shovel(4,4)
use_shovel(3,3)
use_shovel(3,4)
PlantWhenAvailable(1,50,(1,2))
PlantWhenAvailable(1,50,(1,3))

Prejudge(1,1)
WriteZombies([0],[3],[0.37])
PlantWhenAvailable(1,50,(1,4))

Prejudge(1,2)
WriteZombies([0],[2],[0.37])
PlantWhenAvailable(8,100,(2,3))
PlantWhenAvailable(2,25,(4,9))
PlantWhenAvailable(4,25,(4,9))

Prejudge(1,3)
WriteZombies([0],[2],[0.37])
PlantWhenAvailable(8,100,(2,4))
PlantWhenAvailable(2,25,(3,9))

Prejudge(1,4)
WriteZombies([0,0],[2,5],[0.37,0.33])
PlantWhenAvailable(3,50,(3,9))
PlantWhenAvailable(1,50,(2,1))
PlantWhenAvailable(2,25,(1,9))
PlantWhenAvailable(4,25,(1,9))

Prejudge(1,5)
WriteZombies([2],[4],[0.37])
PlantWhenAvailable(1,50,(2,2))

Prejudge(1,6)
WriteZombies([2],[3],[0.37])
PlantWhenAvailable(1,50,(3,1))

Prejudge(1,7)
WriteZombies([0,2],[1,1],[0.37,0.37])

Prejudge(1,8)
WriteZombies([0,2],[3,3],[0.37,0.37])
PlantWhenAvailable(3,50,(3,9))

Prejudge(1,9)
WriteZombies([0,2],[3,3],[0.37,0.37])
PlantWhenAvailable(7,125,(3,9))
PlantWhenAvailable(4,25,(1,9))

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,2,2],[5,5,5,5,5,5,5,5],[0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.37])

Prejudge(1,11)
SetBungees([(3,5)])
WriteZombies([0],[3],[0.37])
PlantWhenAvailable(5,150,(3,9))
PlantWhenAvailable(3,50,(4,9))

Prejudge(1,12)
SetBungees([(3,6)])
WriteZombies([0],[4],[0.37])

Prejudge(1,13)
SetBungees([(5,7)])
WriteZombies([2],[1],[0.37])
PlantWhenAvailable(4,25,(4,9))

Prejudge(1,14)
SetBungees([(3,5)])
WriteZombies([2],[3],[0.37])
use_shovel(3,9)
PlantWhenAvailable(5,150,(3,9))

Prejudge(1,15)
SetBungees([(3,6)])
WriteZombies([2],[1],[0.37])
PlantWhenAvailable(5,150,(1,9))

Prejudge(1,16)
SetBungees([(2,5),(5,7)])

Prejudge(1,17)
SetBungees([(3,6),(4,8)])

Prejudge(1,18)
SetBungees([(5,6),(1,7)])

Prejudge(1,19)
SetBungees([(3,5)])
WriteZombies([4],[4],[0.37])

Prejudge(1,20)
SetBungees([(3,4)])
WriteZombies([0,0,0,0,0,0,0,1,2,3,4],[3,3,3,3,3,3,3,3,3,3,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.68,0.37])
SetAmbushZombies([(3,6),(3,7)])
Delay(550)
PlantWhenAvailable(7,125,(3,2))

while(game_ui() == 3):
   Sleep(1)
print(time.time()-start_time)
