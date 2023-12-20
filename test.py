from pvz import ReadMemory, WriteMemory, SetZombies, Prejudge, game_ui, Sleep, AutoCollect, Card,RunningInThread
from pvz.core import seeds_string
from pvz.core import zombies_string
import time
a = ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=2500)
print(a[1964])



