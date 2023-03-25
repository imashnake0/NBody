import numpy as np
import astropy.constants as const

from Body import Body
from System import System


def main():
    earth = Body(mass=0,
                 position=np.array([0, 0]),
                 velocity=np.array([0, 0]))
    system = System(earth)
    print(const.G)


main()
