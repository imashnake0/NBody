import numpy as np

class System:
    def __init__(self,
                 dt,
                 bodies=[],
                 law=None):
        self.dt = dt
        self.bodies = np.array(bodies)
        self.law = law


    def simulate(self,
                 until=0.0):
        t = 0.0
        while t < until:
            
            t += self.dt
            self.update_net_forces()
