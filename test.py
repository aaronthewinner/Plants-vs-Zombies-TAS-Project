from pvz import ReadMemory, WriteMemory, SetZombies, Prejudge, game_ui, Sleep, AutoCollect, Card,RunningInThread
from pvz.core import seeds_string
from pvz.core import zombies_string
import time
isAnimation = input("Do you want to print animation data? Yes or no?")
zombies_count = ReadMemory("int",0x6a9ec0, 0x768, 0x94)
print("Total number of zombies in memory: " + zombies_count)
zombies_offset = (ReadMemory("int",0x6a9ec0, 0x768, 0x90))
for i in range(zombies_count):
    print("Zombie Row: " + (ReadMemory("int",zombies_offset + 0x1c + i *0x15C)+1))
    print("Zombie Type: " +  ReadMemory("int",zombies_offset + 0x24 + i *0x15C))
    zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
    print("Is Zombie Dead: " + zombie_dead)
    zombie_number =  ReadMemory("unsigned int", zombies_offset + 0x158 + i * 0x15c)
    print("Zombie number: " + zombie_number)
    print("Zombie ID: " + zombie_number & 65535)
    if(isAnimation == "Yes"):
        animation = ReadMemory("unsigned int",zombies_offset + 0x118 + i *0x15C)
        print("Animation number: " + animation)
        print("Animation ID: " + animation & 65535)
        special_animation = ReadMemory("unsigned int",zombies_offset + 0x144 + i *0x15C)
        print("Flag/Special Animation number: " + special_animation)
        print("Flag/Special Animation ID" + special_animation & 65535)
plants_count = ReadMemory("int",0x6a9ec0, 0x768, 0xB0)
print("Total number of plants in memory: " + plants_count)
plants_offset = ReadMemory("int",0x6a9ec0, 0x768, 0xAC)
for i in range(plants_count):
    print("Plant Row: " + ReadMemory("int",plants_offset + 0x1c + i *0x14C) + 1)
    print("Plant Column: " +  ReadMemory("int",plants_offset + 0x28 + i *0x14C) + 1)
    print("Plant Type: " +  ReadMemory("int",plants_offset + 0x24 + i *0x14C))
    plant_dead = ReadMemory("bool", plants_offset + 0x141 + i * 0x14c)
    print("Is Plant Dead: " + plant_dead)
    plant_number =  ReadMemory("unsigned int", plants_offset + 0x148 + i * 0x14c)
    print("Plant number: " + plant_number)
    print("Plant ID: " + plant_number & 65535)
    if(isAnimation == "Yes"):
        animation = ReadMemory("unsigned int",plants_offset + 0x94 + i *0x14C,array=2)
        print("Animation number: " + animation[0])
        print("Animation ID" + animation[0] & 65535)
        if(animation[1] != 0):
            print("Second Animation number: " + animation[1])
            print("Second Animation ID" + animation[1] & 65535)

