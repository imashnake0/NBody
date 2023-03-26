import numpy as np


class Body:
    def __init__(self,
                 mass=0,
                 position=[[0, 0]],
                 velocity=[[0, 0]]):
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
