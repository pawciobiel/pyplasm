from pyplasm import *
c = CUBE(2)
s = CYLINDER(1.5, 3, 64)
VIEW(STRUCT([c, s]))

o = UNION([c, s])
VIEW(o)