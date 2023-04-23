import numpy as np
import numpy.linalg as lin
import astropy.constants.iau2015 as aconst
import astropy.constants.codata2018 as coconst
import matplotlib.pyplot as plt

from utils.PlotUtils import PlotUtils
from utils.NaturalUnits import l_p, t_p, m_p
from core.Body import Body
from core.System import System


def main():
    earth = Body(name="Earth",
                 mass=aconst.M_earth.value, 
                 position=[[aconst.au.value, 0]], 
                 velocity=[[0, 29784.8]])

    halley = Body(name="Halley",
                 mass=2.2e14, 
                 position=[[0.5871*aconst.au.value, 0]], 
                 velocity=[[0, 53545]])
    
    
    sun = Body(name="Sun",
               mass=aconst.M_sun.value)
    
    bodies=[halley, earth, sun]

    system = System(bodies=bodies, 
                    # TODO: Natural units!
                    law=lambda m1, m2, x1, x2: ((coconst.G.value*m1*m2)/((lin.norm(x2 - x1))**3)) * (x2 - x1))

    system.simulate(until=3.154e7*75)

    PlotUtils.plot(bodies=bodies)

main()
