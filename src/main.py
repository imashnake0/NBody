import numpy as np
import astropy.constants.iau2015 as const

from Body import Body
from System import System


def main():
    earth = Body(mass=const.M_earth.value, 
                 position=[[const.au.value, 0]], 
                 velocity=[[0, 29784.8]])
    
    sun = Body(mass=const.M_sun.value)
    
    system = System(bodies=[earth, sun])

    system.simulate()

main()
