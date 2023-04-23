import numpy as np

class System:
    def update_net_forces(self):
        for i, body in enumerate(self.bodies):
            for j, other_body in enumerate(self.bodies):
                if i != j:
                    body.net_force = self.law(body.mass, 
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
                    np.append(body.net_force, law(body.mass, 
                                        other_body.mass, 
                                        body.position[0], 
                                        other_body.position[0]))

    def simulate(self,
                 until=0.0,
                 dt=100000):
        t = 0.0
        while t < until:
            for body in self.bodies:
                # dv = a * dt = (F_net/m) * dt
                dv = body.net_force * (dt/body.mass)
                body.velocity = np.append(body.velocity, [body.velocity[-1] + dv], axis=0)
                # dx = v * dt
                dx = body.velocity[-2] * dt
                body.position = np.append(body.position, [body.position[-1] + dx], axis=0)
            
            t += dt
            self.update_net_forces()
