from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
while(game_ui() != 2):
    Sleep(0.1)
start_time = time.time()
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for j in range(5):
    safe_click()
    left_click(300,300)
while(game_ui() != 3):
    Sleep(0.1)
AutoCollect(interval_cs=1)
slots_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x144)
zombies_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
grave_offset = ReadMemory("unsigned int",0x6A9EC0,0x768,0x11C)
while(game_ui() == 3 and ReadMemory("bool", 0x6A9EC0, 0x768, 0x5603)):
    if ReadMemory("int", 0x6A9EC0, 0x768, 0x5560) >= 75 and ReadMemory("bool", slots_offset + 0x20+2*0x50):
       for k in range(30):
        if(not ReadMemory("bool",grave_offset+0x20 + k*0xec)):
         Card(2,(ReadMemory("int",grave_offset+0x14 + k*0xec)+1,ReadMemory("int",grave_offset+0x10 + k*0xec)+1))
         Sleep(10)
         break
    Sleep(0.1)
    if(ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94) != 0):
        for i in range(ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)):
            if not ReadMemory("bool", zombies_offset + 0xec + i * 0x15c): 
                safe_click()
                left_click(ReadMemory("float",zombies_offset + 0x2c + i * 0x15C)+40, ReadMemory("float",zombies_offset + 0x30 + i * 0x15C)+85)
while(game_ui() == 3):
    Sleep(0.1)
print(time.time()-start_time)