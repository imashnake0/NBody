import numpy as np

class System:
    def update_net_forces(self):
        for body in self.bodies:
            for other_body in self.bodies:
                body.net_force += self.law(body.mass, 
                                      other_body.mass, 
                                      # Updates for the most recent position.
                                      body.position[-1], 
                                      other_body.position[-1])

    def __init__(self,
                 bodies=[],
                 law=None):
        self.bodies = np.array(bodies)
        self.law = law

        for body in bodies:
            for other_body in bodies:
                body.net_force += law(body.mass, 
                                      other_body.mass, 
                                      body.position[0], 
                                      other_body.position[0])

    def simulate(self,
                 until=0.0,
                 dt=0.001):
        t = 0.0
        while t < until:
            for body in self.bodies:
                np.append(body.position, [[0, 0]], axis=0)
            t += dt
