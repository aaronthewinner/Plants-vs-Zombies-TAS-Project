import pandas as pd
import pvz
pvz.WriteMemory("int",1000000,0x69DA94 + 0x1C*22)
df = pd.DataFrame(index=range(5000),columns=["Zombies","Coneheads","Catapults","Preview Normals","Preview Cones","Preview Catapults"],dtype=float)
for i in range(5000):
    if(i % 100 == 0):
        print(i)
    try:
        pvz.set_internal_spawn([0,2,22])
        zombies = list(pvz.ReadMemory("int",0x6a9ec0, 0x768, 0x6b4,array=1000))
        for k in range(20):
            ignore_rest = False
            for j in range(50):
                if (zombies[k * 50 + j] == -1):
                    ignore_rest = True
                    continue
                if (ignore_rest):
                    zombies[k * 50 + j] = -1
        df["Zombies"][i] = zombies.count(0)
        df["Coneheads"][i] = zombies.count(2)
        df["Catapults"][i] = zombies.count(22)
        preview = []
        zombies_count_max = pvz.ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x94)
        zombies_offset = pvz.ReadMemory("unsigned int", 0x6A9EC0, 0x768, 0x90)
        for j in range(zombies_count_max):
            zombie_dead = pvz.ReadMemory("bool", zombies_offset + 0xec + j * 0x15c)
            if not zombie_dead:
                zombie_type = pvz.ReadMemory("int", zombies_offset + 0x24 + j * 0x15c)
                preview.append((int)(zombie_type))
        df["Preview Normals"][i] = preview.count(0)
        df["Preview Cones"][i] = preview.count(2)
        df["Preview Catapults"][i] = preview.count(22)
    except:
        break

print(i)
a = df.groupby(["Preview Cones","Preview Normals","Preview Catapults"])
print(a.size())
print(a.aggregate("mean"))
