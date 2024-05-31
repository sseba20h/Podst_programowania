def one(x, y, z):
    a = 1
    if x >= y and x >= z:
        a = x
    elif z >= y and z >= x:
        a = z
    else:
        a = y
    return a

#print(one(5, 7, 12))

def suma(numbers):
    total = 0
    
    for x in numbers:
        total += x
    
    return total

#print(suma((8, 2, 3, 0, 7)))

def iloczyn(numbers):
    total = 1
    
    for x in numbers:
        total *= x
    
    return total

print(iloczyn((2, 3, 5, 4))) 