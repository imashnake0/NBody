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
    
    sun = Body(name="Sun",
               mass=aconst.M_sun.value)
    
    system = System(bodies=[earth, sun], 
                    # TODO: Natural units!
                    law=lambda m1, m2, x1, x2: ((coconst.G.value*m1*m2)/((lin.norm(x1 - x2))**3)) * (x2 - x1))

    system.simulate(until=3.154e7)

    PlotUtils.plot((earth.position[:, 0], sun.position[:, 0], "x"), (earth.position[:, 1], sun.position[:, 1], "y"), "Earth")

main()
