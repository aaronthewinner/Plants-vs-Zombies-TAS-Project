from pvz import ReadMemory, WriteMemory, SetZombies, Prejudge, game_ui, Sleep, AutoCollect, Card,RunningInThread
from pvz.core import seeds_string
from pvz.core import zombies_string
import pvz.extra
import time
isAnimation = input("Do you want to print animation data? Y or N?")
zombies_count = ReadMemory("int",0x6a9ec0, 0x768, 0x94)
print("Total number of zombies in memory: %d"  % (zombies_count))
print()
zombies_offset = (ReadMemory("int",0x6a9ec0, 0x768, 0x90))
for i in range(zombies_count):
    print("Zombie Row: %d Zombie Type: %d" % (ReadMemory("int",zombies_offset + 0x1c + i *0x15C)+1 , ReadMemory("int",zombies_offset + 0x24 + i *0x15C)))
    zombie_dead = ReadMemory("bool", zombies_offset + 0xec + i * 0x15c)
    print("Is Zombie Dead: %r" % zombie_dead)
    zombie_number =  ReadMemory("unsigned int", zombies_offset + 0x158 + i * 0x15c)
    print("Zombie key: %d" % (0 if zombie_number // 65535 == 0 else (zombie_number - 3748462592) / 65536 if zombie_number >= 3748462592 else  (zombie_number + 65536*65536 - 3748462592)/65536))
    print("Zombie ID: %d" % (zombie_number & 65535))
    if(isAnimation == "Y"):
        animation = ReadMemory("unsigned int",zombies_offset + 0x118 + i *0x15C)
        print("Animation key: %d" % (0 if animation // 65535 == 0 else (animation - 3580624896) / 65536 if animation >= 3580624896 else  (animation + 65536*65536 - 3580624896)/65536))
        print("Animation ID: %d " % (animation & 65535))
        special_animation = ReadMemory("unsigned int",zombies_offset + 0x144 + i *0x15C)
        if(special_animation != 0):
            print("Flag/Special Animation key: %d" % (0 if special_animation // 65535 == 0 else (special_animation - 3580624896) / 65536 if special_animation >= 3580624896 else  (special_animation + 65536*65536 - 3580624896)/65536))
            print("Flag/Special Animation ID: %d" % (special_animation & 65535))
    print()
plants_count = ReadMemory("int",0x6a9ec0, 0x768, 0xB0)
print("Total number of plants in memory: %d" % plants_count)
print()
plants_offset = ReadMemory("int",0x6a9ec0, 0x768, 0xAC)
for i in range(plants_count):
    print("Plant Coords: (%d,%d), Type: %d" % (ReadMemory("int",plants_offset + 0x1c + i *0x14C) + 1, ReadMemory("int",plants_offset + 0x28 + i *0x14C) + 1, ReadMemory("int",plants_offset + 0x24 + i *0x14C)))
    plant_dead = ReadMemory("bool", plants_offset + 0x141 + i * 0x14c)
    print("Is Plant Dead: %r" % plant_dead)
    plant_number =  ReadMemory("unsigned int", plants_offset + 0x148 + i * 0x14c)
    print("Plant key: %d" % (0 if plant_number // 65535 == 0 else (plant_number - 3697344512) / 65536 if plant_number >= 3697344512 else  (plant_number + 65536*65536 - 3697344512)/65536))
    print("Plant ID: %d" % (plant_number & 65535))
    if(isAnimation == "Y"):
        animation = ReadMemory("unsigned int",plants_offset + 0x94 + i *0x14C,array=2)
        print("Animation key: %d" % (0 if animation[0] // 65535 == 0 else (animation[0] - 3580624896) / 65536 if animation[0] >= 3580624896 else  (animation[0] + 65536*65536 - 3580624896)/65536))
        print("Animation ID: %d" % (animation[0] & 65535))
        if(animation[1] != 0):
            print("Second Animation key: %d" % (0 if animation[1] // 65535 == 0 else (animation[1] - 3580624896) / 65536 if animation[1] >= 3580624896 else  (animation[1] + 65536*65536 - 3580624896)/65536))
            print("Second Animation ID: %d" % (animation[1] & 65535))
    print()