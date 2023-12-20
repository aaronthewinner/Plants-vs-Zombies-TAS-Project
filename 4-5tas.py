from pvz import *
from pvz.extra import *
@RunningInThread
def FastPlants():
    """
    Call once game_ui == 3
    This makes all sunflowers have the fastest possible proudction.  
    It also makes all peashooters have the best possible cycles. 
    To add other plants, add extra numbers to the first plant type check. 
    """
    plants = []
    while(game_ui() == 3 and ReadMemory("bool", 0x6A9EC0, 0x768, 0x5603)):
        plants_count_max = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0xB0)
        plants_offset = ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0xAC)
        for i in range(plants_count_max):
            plant_dead = ReadMemory("bool", plants_offset + 0x141 + i * 0x14c)
            plant_squished = ReadMemory("bool", plants_offset + 0x142 + i * 0x14c)
            plant_type = ReadMemory("int", plants_offset + 0x24 + i * 0x14c)
            plant_row = ReadMemory("int", plants_offset + 0x1c + i * 0x14c)
            plant_col = ReadMemory("int", plants_offset + 0x28 + i * 0x14c)
            if not plant_dead and not plant_squished and plant_type == 1 or plant_type == 9:
                
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
                    WriteMemory("int",300, plants_offset + 0x58 + i * 0x14c)
                else:
                    if(ReadMemory("int", plants_offset + 0x58 + i * 0x14c) > 2350 and ReadMemory("int", plants_offset + 0x58 + i * 0x14c) <= 2500):
                       WriteMemory("int", 2350,plants_offset + 0x58 + i * 0x14c) 
            elif not plant_dead and not plant_squished and (ReadMemory("int", 0x69F2C8 + plant_type * 0x24) == 1):
                if(not((plant_row,plant_col) in plants)):
                    plants.append((plant_row,plant_col))
                    if(plant_type == 8 or plant_type == 24):
                        if(plant_col == 8):
                            WriteMemory("int",675, plants_offset + 0x8 + i * 0x14c)
                        else:
                            WriteMemory("int",44 + plant_col*80, plants_offset + 0x8 + i * 0x14c)
                    WriteMemory("int",0, plants_offset + 0x58 + i * 0x14c)
                if(ReadMemory("int", plants_offset + 0x58 + i * 0x14c) > ReadMemory("int", 0x69F2CC + plant_type * 0x24) - 15):
                    WriteMemory("int",ReadMemory("int", 0x69F2CC + plant_type * 0x24) - 15, plants_offset + 0x58 + i * 0x14c)
def plant_seed(seed,coords):
    items_offset = ReadMemory("unsigned int",0x6A9EC0,0x768,0xE4)
    items_count_max = read_memory("int", 0x6A9EC0, 0x768, 0xE8)
    for i in range(items_count_max):
            disappeared = read_memory("bool", items_offset + 0x38 + 0xD8 * i)
            collected = read_memory("bool", items_offset + 0x50 + 0xD8 * i)
            item_type = read_memory("int", items_offset + 0x58 + 0xD8 * i)
            seed_type = read_memory("int", items_offset + 0x68 + 0xD8 * i)
            if(not disappeared and not collected and item_type == 16 and seed_type == seed):
                item_x = read_memory("float", items_offset + 0x24 + 0xD8 * i)
                item_y = read_memory("float", items_offset + 0x28 + 0xD8 * i)
                x, y = int(item_x + 30), int(item_y + 30)
                safe_click()
                left_click(x, y)
                click_grid(coords)
                break

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
vase_offset = ReadMemory("unsigned int",0x6A9EC0,0x768,0x11C)
zombie_coords = [(1,7),(2,7),(3,7),(5,7)]
bucket_coords = [(4,7)]
squash_coords = [(1,8),(2,8),(3,8),(4,8),(1,9)]
pea_coords = [(5,9),(2,9),(3,9),(4,9),(5,8)]
for i in range(15):
    vase_coords = (ReadMemory("int",vase_offset + 0x14 + i*0xEC)+1,ReadMemory("int",vase_offset + 0x10 + i*0xEC)+1)
    if(vase_coords in zombie_coords):
        WriteMemory("int",0,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC)
    elif(vase_coords in bucket_coords):
        WriteMemory("int",4,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC) 
    elif(vase_coords in squash_coords):
        WriteMemory("int",17,vase_offset + 0x40 + i*0xEC)
        WriteMemory("int",1,vase_offset + 0x44 + i*0xEC) 
    elif(vase_coords in pea_coords):
        WriteMemory("int",0,vase_offset + 0x40 + i*0xEC)
        WriteMemory("int",1,vase_offset + 0x44 + i*0xEC)
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
      Sleep(0.1)
for i in range(5):
    safe_click()
    LeftClick(300,300)  
while(game_ui() != 3):
    Sleep(1)
click_grid(1,8)
Delay(20)
click_grid(2,8)
Delay(20) 
click_grid(3,8)
Delay(20)
click_grid(4,8)
Delay(20) 
click_grid(1,9)
Delay(20)
click_grid(1,7)
plant_seed(17,(1,6))
Delay(1)
plant_seed(17,(2,6))
Delay(1)
plant_seed(17,(3,6))
Delay(1)
plant_seed(17,(4,6))
Delay(1)
plant_seed(17,(5,6))
Delay(16)
click_grid(2,7)
Delay(20)
click_grid(3,7)
Delay(20)
click_grid(4,7)
Delay(20)
click_grid(5,7)
Delay(20)
click_grid(5,8)

Delay(20)
click_grid(2,9)
Delay(20)
click_grid(3,9)
Delay(20)
click_grid(4,9)
Delay(20)
click_grid(5,9)
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(5):
    safe_click()
    LeftClick(300,300) 
Sleep(1)
vase_offset = ReadMemory("unsigned int",0x6A9EC0,0x768,0x11C)
zombie_coords = [(1,7),(2,6),(3,6),(4,7),(1,6)]
bucket_coords = [(4,6)]
football_coords = [(3,7)]
squash_coords = [(1,8),(2,8),(3,8),(4,8)]
pea_coords = [(5,9),(2,9),(3,9),(4,9)]
snow_coords = [(5,6),(5,7),(5,8),(1,9),(2,7)]
for i in range(20):
    vase_coords = (ReadMemory("int",vase_offset + 0x14 + i*0xEC)+1,ReadMemory("int",vase_offset + 0x10 + i*0xEC)+1)
    if(vase_coords in zombie_coords):
        WriteMemory("int",0,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC)
    elif(vase_coords in bucket_coords):
        WriteMemory("int",4,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC)
    elif(vase_coords in football_coords):
        WriteMemory("int",7,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC) 
    elif(vase_coords in squash_coords):
        WriteMemory("int",17,vase_offset + 0x40 + i*0xEC)
        WriteMemory("int",1,vase_offset + 0x44 + i*0xEC) 
    elif(vase_coords in pea_coords):
        WriteMemory("int",0,vase_offset + 0x40 + i*0xEC)
        WriteMemory("int",1,vase_offset + 0x44 + i*0xEC)
    elif(vase_coords in snow_coords):
        WriteMemory("int",5,vase_offset + 0x40 + i*0xEC)
        WriteMemory("int",1,vase_offset + 0x44 + i*0xEC)
while(ReadMemory("int",0x6A9EC0,0x844) != 0):
    Sleep(0.1)
click_grid(1,7)
Delay(20)
click_grid(4,7)
Delay(20)
click_grid(3,7)
Delay(20)
click_grid(1,8)
Delay(20)
click_grid(2,8)
Delay(20)
click_grid(3,8)
Delay(20)
click_grid(4,8)
Delay(20)
click_grid(4,6)
Delay(20)
click_grid(1,6)
Delay(1)
plant_seed(17,(4,6))
Delay(19)
click_grid(3,6)
Delay(1)
plant_seed(17,(1,6))
Delay(19)
click_grid(2,6)
Delay(1)
plant_seed(17,(3,6))
Delay(19)
click_grid(1,9)
Delay(1)
plant_seed(17,(2,6))
Delay(19)
click_grid(2,9)
Delay(20)
click_grid(3,9)
Delay(20)
click_grid(4,9)
Delay(20)
click_grid(5,9)
Delay(20)
click_grid(5,6)
Delay(20)
click_grid(5,7)
Delay(20)
click_grid(5,8)
Delay(20)
click_grid(2,7)
Delay(20)
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
    Sleep(0.1)
for i in range(5):
    safe_click()
    LeftClick(300,300) 
Sleep(1)
vase_offset = ReadMemory("unsigned int",0x6A9EC0,0x768,0x11C)
zombie_coords = [(1,6),(2,5),(4,5),(5,5),(4,6),(5,6)]
bucket_coords = [(1,5),(3,5)]
dancer_coords = [(3,6)]
hypno_coords = [(1,7),(2,7),(3,7),(4,7),(5,7)]
pea_coords = [(1,8),(2,8),(3,8),(4,8),(5,8)]
snow_coords = [(1,9),(2,9),(3,9),(4,9),(5,9)]
jack_coords = [(2,6)]
for i in range(25):
    vase_coords = (ReadMemory("int",vase_offset + 0x14 + i*0xEC)+1,ReadMemory("int",vase_offset + 0x10 + i*0xEC)+1)
    if(vase_coords in zombie_coords):
        WriteMemory("int",0,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC)
    elif(vase_coords in bucket_coords):
        WriteMemory("int",4,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC)
    elif(vase_coords in dancer_coords):
        WriteMemory("int",8,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC) 
    elif(vase_coords in hypno_coords):
        WriteMemory("int",12,vase_offset + 0x40 + i*0xEC)
        WriteMemory("int",1,vase_offset + 0x44 + i*0xEC) 
    elif(vase_coords in pea_coords):
        WriteMemory("int",0,vase_offset + 0x40 + i*0xEC)
        WriteMemory("int",1,vase_offset + 0x44 + i*0xEC)
    elif(vase_coords in snow_coords):
        WriteMemory("int",5,vase_offset + 0x40 + i*0xEC)
        WriteMemory("int",1,vase_offset + 0x44 + i*0xEC)
    elif(vase_coords in jack_coords):
        WriteMemory("int",15,vase_offset + 0x3C + i*0xEC)
        WriteMemory("int",2,vase_offset + 0x44 + i*0xEC)         
while(ReadMemory("int",0x6A9EC0,0x844) != 0):
    Sleep(0.1)
FastPlants()
AutoCollect(interval_cs=1)
click_grid(2,6)
Delay(20)
click_grid(5,7)
Delay(20)
click_grid(4,7)
Delay(20)
click_grid(5,6)
Delay(20)
click_grid(4,6)
Delay(20)
click_grid(5,5)
Delay(20)
click_grid(4,5)
Delay(20)
plant_seed(12,(1,5))
Delay(1)
plant_seed(12,(2,5))
Delay(1)
plant_seed(12,(3,5))
Delay(1)
plant_seed(12,(4,5))
Delay(1)
plant_seed(12,(5,5))
Delay(16)
click_grid(1,8)
Delay(20)
click_grid(2,8)
plant_seed(0,(3,5))
Delay(20)
click_grid(3,8)
plant_seed(0,(3,4))
Delay(20)
click_grid(4,8)
plant_seed(0,(3,3))
Delay(20)
click_grid(5,8)
plant_seed(0,(4,5))
Delay(20)
click_grid(1,9)
plant_seed(0,(5,5))
Delay(20)
click_grid(2,9)
plant_seed(5,(1,5))
Delay(20)
click_grid(3,9)
plant_seed(5,(4,4))
Delay(20)
click_grid(4,9)
plant_seed(5,(5,4))
Delay(20)
click_grid(5,9)
plant_seed(5,(1,4))
Delay(20)
plant_seed(5,(3,2))
while(game_ui() == 3):
    Sleep(1)
print(time.time()-start_time)




