import numpy as np

class System:
    def update_net_forces(self):
        for i, body in enumerate(self.bodies):
            for j, other_body in enumerate(self.bodies):
                if i != j:
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

        for i1, body in enumerate(bodies):
            for i2, other_body in enumerate(bodies):
                if i1 != i2:
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
                # TODO: Update `position` and `velocity`!
                body.velocity = np.append(body.velocity, [[0, 0]], axis=0)
                body.position = np.append(body.position, [[0, 0]], axis=0)
            t += dt

        for body in self.bodies:
            print(body.position)
