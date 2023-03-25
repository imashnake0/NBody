import numpy as np


class Body:
    def __init__(self,
                 mass=0,
                 position=np.array([0, 0]),
                 velocity=np.array([0, 0])):
        self.mass = mass
        self.position = position
        self.velocity = velocity
