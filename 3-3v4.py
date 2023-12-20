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
select_seeds_and_lets_rock((1,16,17,4,6,0,2))
waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000)
waves = list(waves)
waves[150:152] = [0,0,-1]
waves[200:201] = [0,0,-1]
waves[250:252] = [2,-1]
waves[300:303] = [0,2,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:459] = [0,0,0,0,0,0,0,1,2,-1]
waves[500:502] = [0,11,-1]
waves[550:552] = [2,2,-1]
waves[600:603] = [0,2,2,-1]
waves[650:654] = [0,0,0,2,-1]
waves[700:703] = [0,2,2,-1]
waves[750:753] = [2,2,2,-1]
waves[800:805] = [0,0,0,0,2,-1]
waves[850:853] = [2,2,2,-1]
waves[900:904] = [0,2,2,2,-1]
waves[950:960] = [0,0,0,0,0,0,0,1,2,11,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(20)

PlantWhenAvailable(1,50,(6,1))
PlantWhenAvailable(1,50,(6,2))

Prejudge(1,1)
WriteZombies([0],[6],[0.37])
Delay(70)
PlantWhenAvailable(6,100,(6,7))

Prejudge(0,2)
WriteZombies([0],[6],[0.23])
PlantWhenAvailable(1,50,(6,3))
PlantWhenAvailable(6,100,(6,8))
PlantWhenAvailable(4,25,(2,9))

Prejudge(0,3)
WriteZombies([0],[6],[0.37])

Prejudge(0,4)
WriteZombies([0,0],[6,1],[0.37,0.32])
PlantWhenAvailable(1,50,(6,4))
PlantWhenAvailable(3,50,(5,9))
PlantWhenAvailable(1,50,(6,5))

Prejudge(0,5)
WriteZombies([0,0],[6,1],[0.37,0.37])
PlantWhenAvailable(1,50,(6,6))

Prejudge(0,6)
WriteZombies([2],[5],[0.37])
PlantWhenAvailable(4,25,(1,9))

Prejudge(0,7)
WriteZombies([0,2],[2,2],[0.37,0.37])

Prejudge(0,8)
WriteZombies([0,2],[6,5],[0.37,0.37])
PlantWhenAvailable(5,150,(5,9))
PlantWhenAvailable(2,25,(4,9))
PlantWhenAvailable(3,50,(4,9))

Prejudge(0,9)
WriteZombies([0,2],[1,1],[0.37,0.37])
PlantWhenAvailable(1,50,(1,8))
PlantWhenAvailable(1,50,(1,7))

Prejudge(0,10)
WriteZombies([0,0,0,0,0,0,0,1,2],[5,1,1,1,1,1,1,2,1],[0.315,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.37])
use_shovel(5,9)
PlantWhenAvailable(4,25,(1,9))
PlantWhenAvailable(1,50,(1,6))

Prejudge(1,11)
WriteZombies([0,11],[4,3],[0.37,0.68])

Prejudge(1,12)
WriteZombies([2,2],[6,5],[0.37,0.37])
PlantWhenAvailable(5,150,(6,9))
PlantWhenAvailable(3,50,(4,9))

Prejudge(1,13)
WriteZombies([0,2,2],[1,1,1],[0.37,0.37,0.37])

Prejudge(1,14)
WriteZombies([0,0,0,2],[5,5,5,2],[0.37,0.37,0.37,0.37])
PlantWhenAvailable(5,150,(2,9))

Prejudge(1,15)
WriteZombies([0,2,2],[4,4,4],[0.37,0.37,0.37])
PlantWhenAvailable(4,25,(1,9))

Prejudge(1,16)
WriteZombies([2,2,2],[2,2,2],[0.37,0.37,0.37])

Prejudge(1,17)
WriteZombies([0,0,0,0,2],[5,5,5,5,2],[0.37,0.37,0.37,0.37,0.37])
use_shovel(2,9)
PlantWhenAvailable(5,150,(2,9))

Prejudge(1,18)
WriteZombies([2,2,2],[1,1,1],[0.37,0.37,0.37])

Prejudge(1,19)
WriteZombies([0,2,2,2],[5,5,5,5],[0.37,0.37,0.37,0.37])

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,1,2,11],[3,4,5,3,4,5,3,4,5,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.68])
SetAmbushZombies([(3,8),(4,8),(3,9)])
Prejudge(205,20)
PlantWhenAvailable(7,150,(4,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)