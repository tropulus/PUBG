import math
import numpy as np
E = 24*1000/math.sqrt(3)
V = 15*1000/math.sqrt(3)
I = 2622.6132873544516

X = 2.1
d = math.radians(27.4)

ft = (V+I*X)

st = (E*math.sin(d)/X)**2


I = math.sqrt(ft + st)

print(0.75*I)

