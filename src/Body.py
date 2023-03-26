import numpy as np


class Body:
    def __init__(self,
                 name,
                 mass=0.0,
                 position=[[0, 0]],
                 velocity=[[0, 0]],
                 net_force=[0.0, 0.0]):
        self.name = name
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.net_force = net_force
