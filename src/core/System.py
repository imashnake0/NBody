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
            for body in self.bodies:
                # dv = a * dt = (F_net/m) * dt
                dv = body.net_force * (self.dt/body.mass)
                body.velocity = np.append(body.velocity, [body.velocity[-1] + dv], axis=0)
                # dx = v * dt
                dx = body.velocity[-2] * self.dt
                body.position = np.append(body.position, [body.position[-1] + dx], axis=0)
            
            t += self.dt
            self.update_net_forces()
