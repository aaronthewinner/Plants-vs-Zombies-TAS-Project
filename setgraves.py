from pvz import *
def SetGraves(grave_locations):
    """
    Sets the grave locations for a level as desired.  
    Note: currently will not work if there are other grid items, such as a rake
    grave_locations: List of tuples, 
    Ex: [(2,5),(3,6)] sets 2 graves to row 2 col 5 and row 3 col 6
    """
    grave_offset = ReadMemory("unsigned int",0x6A9EC0,0x768,0x11C)
    for i in range(len(grave_locations)):
        WriteMemory("int",grave_locations[i][0]-1,grave_offset+0x14+i*0xEC)
        WriteMemory("int",grave_locations[i][1]-1,grave_offset+0x10+i*0xEC)

