import numpy as np


class System:
    def __init__(self,
                 bodies=np.array([]),
                 law=None):
        self.bodies = bodies
        self.law = law
