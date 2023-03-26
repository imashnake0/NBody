import numpy as np
import numpy.linalg as lin
import astropy.constants.iau2015 as aconst
import astropy.constants.codata2018 as coconst
import matplotlib.pyplot as plt

from Body import Body
from System import System


def main():
    earth = Body(name="Earth",
                 mass=aconst.M_earth.value, 
                 position=[[aconst.au.value, 0]], 
                 velocity=[[0, 29784.8]])
    
    sun = Body(name="Sun",
               mass=aconst.M_sun.value)
    
    system = System(bodies=[earth, sun], 
                    law=lambda m1, m2, x1, x2: ((coconst.G.value*m1*m2)/((lin.norm(x1 - x2))**3)) * (x1 - x2))

    system.simulate(until=10.0)

    fig, ax = plt.subplots()
    ax.scatter(sun.position,  linewidth=2.0)
    plt.show()

main()
