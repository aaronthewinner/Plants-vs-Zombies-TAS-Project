from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
import os

while(game_ui() != 2):
    Sleep(1)
start_time = time.time()
world_start_time = time.time()
WriteMemory("int",1,0x522598)
WriteMemory("int",1,0x522CB5)
os.system("python 4-1v4.py")
print("4-1 " + str(time.time()-start_time))
print("4-1 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 4-2v2.py")
print("4-2 " + str(time.time()-start_time))
print("4-2 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 4-3v2.py")
print("4-3 " + str(time.time()-start_time))
print("4-3 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 4-4v2.py")
print("4-4 " + str(time.time()-start_time))
print("4-4 Split " + str(time.time()-world_start_time))
press_enter()
while(ReadMemory("int",0x6A9EC0,0x844) != 4):
      Sleep(0.1)
press_enter()
press_enter()
press_enter()
press_enter()
press_enter()
press_enter()
left_click(520,280)
Sleep(150)
left_click(450,560)
Sleep(5)
start_time = time.time()
os.system("python 4-5tas.py")
print("4-5 " + str(time.time()-start_time))
print("4-5 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 4-6v4.py")
print("4-6 " + str(time.time()-start_time))
print("4-6 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 4-7v2.py")
print("4-7 " + str(time.time()-start_time))
print("4-7 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 4-8v4.py")
print("4-8 " + str(time.time()-start_time))
print("4-8 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 4-9v2.py")
print("4-9 " + str(time.time()-start_time))
print("4-9 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 4-10tas.py")
print("4-10 " + str(time.time()-start_time))
print("4-10 Split! " + str(time.time()-world_start_time))