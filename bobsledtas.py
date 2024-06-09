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
waves[0:1] = [12,-1] 
waves[50:51] = [12,-1]
waves[100:101] = [13,-1] 
waves[150:151] = [13,-1] 
waves[200:201] = [13,-1] 
waves[250:253] = [13,-1] 
waves[300:303] = [13,-1]
waves[350:352] = [13,-1]
waves[400:402] = [13,-1]
waves[450:458] = [0,0,0,0,0,1,12,-1]
waves[500:502] = [12,-1] 
waves[550:552] = [12,-1] 
waves[600:602] = [13,13,-1] 
waves[650:652] = [13,13,-1] 
waves[700:702] = [13,13,-1] 
waves[750:752] = [13,13,-1] 
waves[800:802] = [13,13,-1] 
waves[850:852] = [13,13,-1] 
waves[900:902] = [12,-1] 
waves[950:961] = [0,0,0,0,0,0,0,1,12,12,-1] 
waves[1000:1008] = [13,13,13,-1]
waves[1050:1058] = [13,13,13,-1]
waves[1100:1109] = [13,13,13,-1]
waves[1150:1159] = [13,13,13,-1]
waves[1200:1209] = [13,13,13,-1]
waves[1250:1256] = [13,13,13,-1]
waves[1300:1306] = [13,13,13,-1] 
waves[1350:1360] = [13,13,13,13,-1]
waves[1400:1405] = [12,12,-1] 
waves[1450:1463] = [0,0,0,0,0,0,0,0,1,12,12,13,-1]
waves[1500:1501] = [13,13,13,13,-1] 
waves[1550:1551] = [13,13,13,13,-1] 
waves[1600:1601] = [13,13,13,13,-1] 
waves[1650:1651] = [13,13,13,13,-1] 
waves[1700:1701] = [13,13,13,13,-1] 
waves[1750:1751] = [13,13,13,13,-1] 
waves[1800:1801] = [13,13,13,13,13,-1] 
waves[1850:1851] = [13,13,13,13,13,-1] 
waves[1900:1901] = [13,13,13,13,13,-1] 
waves[1950:1951] = [0,0,0,0,0,0,0,0,1,12,12,12,12,-1]
waves = tuple(waves)
WriteMemory("int",waves,0x6a9ec0, 0x768, 0x6b4)
WriteMemory("int", 1, 0x52B537)
while(read_memory("int", 0x6A9EC0, 0x768,0x144,0xC) != 0):
    Sleep(0.1)
select_seeds_and_lets_rock((1,16,17,21,46,20,68,2,4,35))
while(game_ui() != 3):
    Sleep(1)
update_game_scene()
AutoCollect(interval_cs=1)
FastSun()
FastPlants()
thirtyFiveRule(40)
PlantWhenAvailable(1,50,(2,1))
PlantWhenAvailable(1,50,(2,2))
PlantWhenAvailable(1,50,(2,3))
PlantWhenAvailable(1,50,(5,1))
PlantWhenAvailable(1,50,(5,2))
PlantWhenAvailable(1,50,(5,3))
Prejudge(1,1)
WriteZombies([12],[1])
PlantWhenAvailable(6,125,(1,4))
PlantWhenAvailable(1,50,(6,3))
Prejudge(1,2)
WriteZombies([12],[1])
Prejudge(399,2)
PlantWhenAvailable(4,100,(1,9))
Prejudge(1,3)
WriteZombies([13],[1])
Prejudge(1,4)
WriteZombies([13],[1])
PlantWhenAvailable(7,125,(2,4))
Prejudge(1,5)
WriteZombies([13],[1])
Prejudge(1,6)
WriteZombies([13],[1])
Prejudge(1,7)
WriteZombies([13],[1])

