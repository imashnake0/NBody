import numpy as np

from src.Body import Body
from src.System import System


def main():
    earth = Body(mass=0,
                 position=np.array([0, 0]),
                 velocity=np.array([0, 0]))
    system = System(earth)

main()
