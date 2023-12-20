# coding=utf-8

from pvz import *
from pvz.extra import game_ui
from pvz.core import seeds_string
from pvz.core import zombies_string
total = 0
nothing = 0
for j in range(1,1000):
    while(game_ui() != 2):
        Sleep(100)
    Sleep(100)
    SelectCards([0, "寒冰菇", "咖啡豆", "南瓜", "坚果", "窝瓜", "花盆", "胆小", "阳光", "小喷"])
    SetZombies([0,20])

    for wave in range(1, 21):
        Prejudge(100, wave)
        zombies_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)
        zombies_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
        for i in range(zombies_count_max):
            zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
            if not zombie_dead:
                zombie_type = ReadMemory("int", zombies_offset + 0x24 + i * 0x15c)
                zombie_row = ReadMemory("int", zombies_offset + 0x1c + i * 0x15c)
                zombie_x = ReadMemory("int", zombies_offset + 0x8 + i * 0x15c)
                zombie_hp = ReadMemory("int", zombies_offset + 0xc8 + i * 0x15c)
                if(zombies_string[zombie_type][1] == "蹦极"):
                    total += 1
                    if(zombie_x < 280 or zombie_x > 600):
                        nothing += 1

    print(nothing)
    print(total)