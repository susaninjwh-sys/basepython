from itertools import product, repeat

print("x y z w")
for x,y,z in product([0,1], repeat=3):
    if (x==y<=z): print(x,y,z)
