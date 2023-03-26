import numpy as np
import numpy.linalg as lin
import astropy.constants.iau2015 as aconst
import astropy.constants.codata2018 as coconst

from Body import Body
from System import System


def main():
    earth = Body(mass=aconst.M_earth.value, 
                 position=[[aconst.au.value, 0]], 
                 velocity=[[0, 29784.8]])
    
    sun = Body(mass=aconst.M_sun.value)
    
    system = System(bodies=[earth, sun], 
                    law=lambda m1, m2, x1, x2: ((coconst.G.value*m1*m2)/((lin.norm(x1 - x2))**3)) * (x1 - x2))

    system.simulate()

main()
