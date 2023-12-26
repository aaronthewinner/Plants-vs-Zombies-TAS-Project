from pvz import *
from pvz.extra import *
import random
def makelevelslist(n):
    levels = []
    for i in range(n):
        levels.append(i+1)
    return levels
levels = makelevelslist(50)
for i in range(50):
    if(i == 0):
        while(ReadMemory("int",0x6A9EC0,0x82C, 0x24) != 1): # current level
            Sleep(0.1)
    WriteMemory("int",0,0x6A9EC0,0x82C, 0x28)
    newlevel = random.choice(levels)
    levels.remove(newlevel)
    print(levels)
    WriteMemory("int",newlevel,0x6A9EC0,0x82C, 0x24)
    if(i != 0): 
        WriteMemory("int",newlevel-1,0x6A9EC0,0x768, 0x5550)
    if(newlevel >= 44): # gloom shroom
        WriteMemory("bool",True,0x6A9EC0,0x82C,0x1C8)
    else:
        WriteMemory("bool",False,0x6A9EC0,0x82C,0x1C8)
    if(newlevel >= 24): # slots
        WriteMemory("int",2,0x6A9EC0,0x82C,0x214)
    elif(newlevel >= 14):
        WriteMemory("int",1,0x6A9EC0,0x82C,0x214)
    else:
        WriteMemory("int",0,0x6A9EC0,0x82C,0x214)
    if(i == 0):
        while(game_ui() != 3):
            Sleep(0.1)
    Sleep(1000)
    while(game_ui() != 3 or ReadMemory("bool",0x6A9EC0,0x768, 0x5603)):
        Sleep(0.1)