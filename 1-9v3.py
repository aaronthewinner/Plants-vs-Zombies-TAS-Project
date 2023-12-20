from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
update_game_scene()
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock((1,4,6,3,0,2))
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:252] = [0,0,-1]
waves[300:303] = [0,0,0,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:458] = [0,0,0,0,0,1,3,3,-1]
waves[500:501] = [4,-1]
waves[550:551] = [4,-1]
waves[600:602] = [0,4,-1]
waves[650:652] = [0,4,-1]
waves[700:702] = [0,4,-1]
waves[750:752] = [2,4,-1]
waves[800:803] = [0,0,4,-1]
waves[850:852] = [2,4,-1]
waves[900:903] = [0,2,4,-1]
waves[950:962] = [0,0,0,0,0,0,0,0,1,2,3,4,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(20)

PlantWhenAvailable(1,50,(1,1))
PlantWhenAvailable(1,50,(1,2))

Prejudge(1,1)
WriteZombies([0],[1],[0.37])
Delay(75)
PlantWhenAvailable(5,100,(1,7))

Prejudge(0,2)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(1,50,(1,3))
PlantWhenAvailable(5,100,(1,8))
PlantWhenAvailable(2,25,(4,9))

Prejudge(0,3)
WriteZombies([0],[1],[0.37])

Prejudge(0,4)
WriteZombies([0,0],[1,3],[0.37,0.315])
PlantWhenAvailable(1,50,(1,4))

Prejudge(0,5)
WriteZombies([0,0],[1,3],[0.37,0.37])
Delay(75)
PlantWhenAvailable(5,100,(1,6))
PlantWhenAvailable(1,50,(1,5))

Prejudge(0,6)
WriteZombies([0,0],[1,3],[0.37,0.37])
PlantWhenAvailable(2,25,(5,9))
PlantWhenAvailable(1,50,(2,1))

Prejudge(0,7)
WriteZombies([0,0,0],[1,2,3],[0.37,0.33,0.37])
PlantWhenAvailable(5,100,(2,7))

Prejudge(0,8)
WriteZombies([0,2],[4,4],[0.37,0.37])
PlantWhenAvailable(1,50,(3,9))

Prejudge(0,9)
WriteZombies([0,2],[5,5],[0.37,0.37])
PlantWhenAvailable(1,50,(3,8))
PlantWhenAvailable(1,50,(3,7))
PlantWhenAvailable(2,25,(5,9))

Prejudge(1,10)
WriteZombies([0,0,0,0,0,1,3,3],[3,3,3,3,3,4,2,5],[0.37,0.37,0.37,0.37,0.37,0.45,0.68,0.68])
use_shovel(2,7)
PlantWhenAvailable(1,50,(3,6))

Prejudge(1,11)
WriteZombies([4],[2],[0.37])
Delay(150)
PlantWhenAvailable(3,150,(2,9))

Prejudge(1,12)
WriteZombies([4],[5],[0.37])

Prejudge(1,13)
WriteZombies([0,4],[1,1],[0.3,0.37])
PlantWhenAvailable(3,150,(1,9))

Prejudge(1,14)
WriteZombies([0,4],[2,2],[0.37,0.37])
PlantWhenAvailable(2,25,(4,9))

Prejudge(1,15)
WriteZombies([0,4],[1,1],[0.3,0.37])
use_shovel(1,9)
PlantWhenAvailable(3,150,(1,9))
PlantWhenAvailable(4,50,(5,1))

Prejudge(1,16)
WriteZombies([2,4],[4,4],[0.37,0.37])

Prejudge(1,17)
WriteZombies([0,0,4],[1,1,1],[0.3,0.3,0.37])
use_shovel(1,9)
PlantWhenAvailable(3,150,(1,9))

Prejudge(1,18)
WriteZombies([2,4],[4,4],[0.37,0.37])
Delay(310)
use_shovel(5,1)

Prejudge(1,19)
WriteZombies([0,2,4],[5,5,5],[0.37,0.37,0.37])

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,0,1,2,3,4],[3,4,5,3,4,5,3,4,5,3,4,5],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.68,0.37])
Prejudge(220,20)
PlantWhenAvailable(6,150,(4,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)