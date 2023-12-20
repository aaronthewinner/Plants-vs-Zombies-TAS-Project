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
waves[150:152] = [0,0,-1]
waves[200:202] = [0,0,-1]
waves[250:252] = [0,0,-1]
waves[300:303] = [0,0,0,-1]
waves[350:352] = [0,2,-1]
waves[400:402] = [0,2,-1]
waves[450:458] = [0,0,0,0,0,1,2,3,-1]
waves[500:502] = [0,0,3,-1]
waves[550:552] = [0,0,3,-1]
waves[600:603] = [0,2,2,-1]
waves[650:654] = [0,0,0,3,-1]
waves[700:703] = [0,2,2,-1]
waves[750:755] = [0,0,0,0,3,-1]
waves[800:805] = [0,0,0,0,3,-1]
waves[850:853] = [2,2,2,-1]
waves[900:904] = [0,2,2,2,-1]
waves[950:963] = [0,0,0,0,0,0,0,0,1,2,2,3,3,-1]

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(20)

PlantWhenAvailable(2,50,(1,1))
PlantWhenAvailable(2,50,(1,2))

Prejudge(1,1)
WriteZombies([0],[1],[0.37])
Delay(75)
PlantWhenAvailable(1,100,(1,7))

Prejudge(0,2)
WriteZombies([0],[1],[0.23])
PlantWhenAvailable(2,50,(1,3))
PlantWhenAvailable(1,100,(1,8))
PlantWhenAvailable(5,25,(4,9))

Prejudge(0,3)
WriteZombies([0],[1],[0.37])

Prejudge(0,4)
WriteZombies([0,0],[1,3],[0.37,0.315])
PlantWhenAvailable(2,50,(1,4))

Prejudge(0,5)
WriteZombies([0,0],[1,3],[0.37,0.37])
Delay(75)
PlantWhenAvailable(1,100,(1,6))
PlantWhenAvailable(2,50,(2,1))

Prejudge(0,6)
WriteZombies([0,0],[1,3],[0.37,0.37])
PlantWhenAvailable(5,25,(5,9))
PlantWhenAvailable(2,50,(2,2))

Prejudge(0,7)
WriteZombies([0,0,0],[1,2,3],[0.37,0.33,0.37])
PlantWhenAvailable(1,100,(2,7))

Prejudge(0,8)
WriteZombies([0,2],[4,4],[0.37,0.37])
PlantWhenAvailable(2,50,(2,3))

Prejudge(0,9)
WriteZombies([0,2],[5,5],[0.37,0.37])
PlantWhenAvailable(2,50,(2,4))
PlantWhenAvailable(1,100,(2,8))
PlantWhenAvailable(5,25,(5,9))

Prejudge(0,10)
WriteZombies([0,0,0,0,0,1,2,3],[3,3,3,3,3,3,3,5],[0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.68])
PlantWhenAvailable(1,100,(2,6))

Prejudge(0,11)
WriteZombies([0,0,3],[1,2,4],[0.37,0.37,0.68])
PlantWhenAvailable(1,100,(2,5))

Prejudge(0,12)
WriteZombies([0,0,3],[1,2,4],[0.37,0.37,0.68])
PlantWhenAvailable(2,50,(4,3))

Prejudge(0,13)
WriteZombies([0,2,2],[5,5,5],[0.37,0.37,0.37])
PlantWhenAvailable(1,100,(3,7))

Prejudge(0,14)
WriteZombies([0,0,0,3],[1,2,3,4],[0.37,0.37,0.37,0.68])
PlantWhenAvailable(5,25,(4,9))

Prejudge(0,15)
WriteZombies([0,2,2],[4,4,4],[0.35,0.35,0.35])
PlantWhenAvailable(4,50,(5,1))
PlantWhenAvailable(1,100,(3,8))

Prejudge(0,16)
WriteZombies([0,0,0,0,3],[1,2,2,3,5],[0.37,0.37,0.37,0.37,0.68])
PlantWhenAvailable(1,100,(1,5))

Prejudge(0,17)
WriteZombies([0,0,0,0,3],[1,1,2,3,5],[0.37,0.37,0.37,0.37,0.68])
PlantWhenAvailable(1,100,(3,9))
use_shovel(5,1)

Prejudge(0,18)
WriteZombies([2,2,2],[5,5,5],[0.37,0.37,0.37])

Prejudge(0,19)
WriteZombies([0,2,2,2],[4,4,4,4],[0.37,0.37,0.37,0.37])

Prejudge(1,20)
WriteZombies([0,0,0,0,0,0,0,0,1,2,2,3,3],[3,4,5,3,4,5,3,4,5,3,4,5,3],[0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.37,0.45,0.37,0.37,0.68,0.68])
Prejudge(220,20)
PlantWhenAvailable(3,150,(4,9))

while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)