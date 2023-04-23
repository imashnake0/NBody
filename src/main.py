import numpy as np
import numpy.linalg as lin
import astropy.constants.iau2015 as aconst
import astropy.constants.codata2018 as coconst
import matplotlib.pyplot as plt
from utils.PlotUtils import PlotUtils

from core.Body import Body
from core.System import System


def main():
    rock1 = Body(name="Rock1",
                 mass=1,
                 position=[[1, 0]],
                 velocity=[[0, np.sqrt(10000)]])
    
    rock2 = Body(name="Rock2",
                 mass=10000,
                 position=[[0, 0]],
                 velocity=[[0, 0]])

    earth = Body(name="Earth",
                 mass=aconst.M_earth.value, 
                 position=[[aconst.au.value, 0]], 
                 velocity=[[0, 29784.8]])
    
    sun = Body(name="Sun",
               mass=aconst.M_sun.value)
    
    system = System(bodies=[rock1, rock2], 
                    law=lambda m1, m2, x1, x2: m1*m2*(x2 - x1))
                    # TODO: Natural units!
                    # law=lambda m1, m2, x1, x2: ((coconst.G.value*m1*m2)/((lin.norm(x1 - x2))**3)) * (x2 - x1))

    system.simulate(until=0.1)

    PlotUtils.plot((rock1.position[:, 0], rock2.position[:, 0], "x"), (rock1.position[:, 1], rock2.position[:, 1], "y"), "Earth")

main()
