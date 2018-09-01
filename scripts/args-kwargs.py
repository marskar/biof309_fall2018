print("HI")
map()

t = "python", "rocks" #define a tuple
d = {"sep":" ", "end":"!"} #define a new dictionary
print(*t, **d)
print(*t)
d ={"x":1,"y":2,"z":3} #define a dictionary
print(*d) #unpack dictionary keys
print(*d.keys()) #unpack dictionary keys
print(*d.values()) #unpack dictionary values
k,v = zip(*d.items()) #get keys and values as tuples
print()