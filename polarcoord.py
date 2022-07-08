# z = x + yj
# polar coord is (r,phi)
# r = sqrt(x^2 + y^2)
# phi = phase angle
import cmath

coord = input()

# put the complex num string into this
phase = cmath.phase(complex(coord))
r = abs(complex(coord))
print(round(r,3))
print(round(phase,3))
