from pvz import *
from pvz.extra import *
import time
from speedrunmethods import *
import os

start_time = time.time()
world_start_time = time.time()
os.system("python 1-1v2.py")
print("1-1 " + str(time.time()-start_time))
print("1-1 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 1-2v2.py")
press_enter()
print("1-2 " + str(time.time()-start_time))
print("1-2 Split " + str(time.time()-world_start_time))
start_time = time.time()
os.system("python 1-3v3.py")
print("1-3 " + str(time.time()-start_time))
print("1-3 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 1-4v7.py")
print("1-4 " + str(time.time()-start_time))
print("1-4 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("1-5v2noRNGmanip.py")
print("1-5 " + str(time.time()-start_time))
print("1-5 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 1-6v4.py")
print("1-6 " + str(time.time()-start_time))
print("1-6 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 1-7v5.py")
print("1-7 " + str(time.time()-start_time))
print("1-7 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 1-8v3.py")
print("1-8 " + str(time.time()-start_time))
print("1-8 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 1-9v3.py")
print("1-9 " + str(time.time()-start_time))
print("1-9 Split " + str(time.time()-world_start_time))
press_enter()
start_time = time.time()
os.system("python 1-10.py")
print("1-10 " + str(time.time()-start_time))
print("1-10 Split! " + str(time.time()-world_start_time))
