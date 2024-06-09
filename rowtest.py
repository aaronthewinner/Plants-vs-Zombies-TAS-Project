import pvz
def lane_weight(aweight, last_picked, second_last_picked):
    if aweight < 1E-06:
        return 0

    num = 2
    num2 = 1 / aweight
    num3 = num2 * 2

    num4 = last_picked + 1 - num2
    num5 = second_last_picked + 1 - num3

    num6 = 1 + num4 / num2 * num
    num7 = 1 + num5 / num3 * num

    num8 = clampfloat(num6 * 0.75 + num7 * 0.25, 0.01, 100)

    return aweight * num8

def clampfloat(value, min, max):
    if value < min:
        return min
    elif value > max:
        return max
    else:
        return value
print(pvz.ReadMemory("float",0x6A9EC0,0x768,0x654,array=50))
print(pvz.ReadMemory("int",0x6A9EC0,0x768,0x654,array=50))
print(lane_weight(1/4,1.0,1.0))
print(lane_weight(1/4,2.0,2.0))