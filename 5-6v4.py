from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(0.1)
start_time = time.time()
update_game_scene()

waves = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1500)
waves = list(waves)
waves[150:153] = [2,-1] #4
waves[200:203] = [0,0,-1] #5
waves[250:253] = [0,0,-1] #6
waves[300:303] = [0,0,0,-1] #7
waves[350:352] = [0,0,0,-1] #8
waves[400:402] = [0,2,-1] #9
waves[450:458] = [0,0,0,0,0,1,22,-1] #10
waves[500:502] = [22,-1] #11
waves[550:552] = [0,0,0,0,-1] #12
waves[600:602] = [0,0,0,0,0,-1] #13
waves[650:652] = [0,0,0,0,0,-1] #14
waves[700:702] = [0,0,0,0,0,-1] #15
waves[750:752] = [0,0,0,0,0,0,-1] #16
waves[800:802] = [0,0,0,0,0,0,-1] #17
waves[850:852] = [0,0,0,0,0,0,-1]#18
waves[900:902] = [2,2,2,0,-1] #19
waves[950:961] = [0,0,0,0,0,0,0,1,0,2,22,-1] #20

waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
WriteMemory("int", 1, 0x52B537)
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock((1,33,17,4,10,35,42,20,34,14))
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(20)
Card(1,(1,1))
Sleep(1)
PlantWhenAvailable(1,50,(1,2))

PlantWhenAvailable(1,50,(1,3))
Prejudge(1,1)
WriteZombies([0])
PlantWhenAvailable(1,50,(2,1))
Prejudge(1,2)
WriteZombies([0],[3],[0.37])
Delay(85)
PlantWhenAvailable(9,100,(3,3))
PlantWhenAvailable(1,50,(2,2))

PlantWhenAvailable(2,25,(3,9))

Prejudge(1,3)
WriteZombies([0],[3],[0.23])
Delay(150)
PlantWhenAvailable(4,25,(3,9))

Prejudge(1,4)
WriteZombies([2],[3])
Delay(475)
PlantWhenAvailable(5,75,(3,9))
PlantWhenAvailable(6,75,(3,9))
Prejudge(1,5)
WriteZombies([0,0],[3,3],[0.37,0.37])
WriteMemory("int", 100, 0x52B537)
PlantWhenAvailable(7,150,(3,9))

Prejudge(1,6)
WriteZombies([0,0],[4,2])
Prejudge(1,7)
WriteZombies([0,0,0],[2,3,4],[0.37,0.23,0.37])
PlantWhenAvailable(1,50,(2,3))
use_shovel(3,3)
Prejudge(1,8)
WriteZombies([0,0,0],[2,3,4],[0.37,0.23,0.37])
PlantWhenAvailable(2,25,(5,9))
Prejudge(1,9)
WriteZombies([0,2],[1,1])
PlantWhenAvailable(1,50,(3,1))
PlantWhenAvailable(2,25,(1,9))
PlantWhenAvailable(3,50,(1,9))
PlantWhenAvailable(4,25,(5,9))
Prejudge(1,10)
WriteZombies([1,22,0,0,0,0,0],[5,4,5,5,5,5,5],[0.45,0.37,0.37,0.37,0.37,0.37,0.37])
Delay(215)
Card(8,(5,3))
Prejudge(1,11)
WriteZombies([22],[5])
Prejudge(1,12)
WriteZombies([0,0,0,0],[2,2,3,4],[0.37,0.23,0.23,0.37])

Prejudge(1,13)
WriteZombies([0,0,0,0,0],[2,3,3,4,4],[0.37,0.23,0.23,0.37,0.37])
PlantWhenAvailable(3,50,(1,9))
Prejudge(1,14)
WriteZombies([0,0,0,0,0],[2,3,3,4,4],[0.37,0.23,0.23,0.37,0.37])
Prejudge(1,15)
WriteZombies([0,0,0,0,0],[2,2,3,4,4],[0.37,0.37,0.23,0.37,0.37])
PlantWhenAvailable(2,25,(2,9))
PlantWhenAvailable(5,75,(2,9))
PlantWhenAvailable(6,75,(2,9))
PlantWhenAvailable(7,150,(2,9))
Prejudge(1,16)
WriteZombies([0,0,0,0,0,0],[2,2,3,3,4,4],[0.37,0.37,0.23,0.37,0.37,0.37])
Prejudge(1,17)
WriteZombies([0,0,0,0,0,0],[2,2,3,4,4,1],[0.37,0.37,0.23,0.37,0.37,0.37])
Prejudge(1,18)
WriteZombies([0,0,0,0,0,0],[2,2,3,4,4,1],[0.37,0.37,0.23,0.37,0.37,0.37])
Prejudge(1,19)
WriteZombies([2,2,2,0],[1,1,1,1],[0.37,0.37,0.37,0.37])
Card(2,(1,9))
Card(3,(1,9))
Delay(1000)
PlantWhenAvailable(10,75,(4,3))
PlantWhenAvailable(6,75,(4,3))
Prejudge(1,20)
WriteZombies([1,22,2,0,0,0,0,0,0,0,0],[4,4,4,4,4,4,4,4,4,4,4])
SetAmbushZombies([(4,5),(4,6),(4,7)])
Delay(210)
Card(8,(4,3))
while(game_ui() == 3):
    Sleep(0.1)
print(time.time()-start_time)
