import numpy as np

class System:
    '''
    System with bodies and a gravitational law.
    '''
    def solve(self, t, y):
        '''
        Note that the gravitational law at hand doesn't depend on `t`!
        '''
        y_prime = np.zeros(y.size)
        for i, body in enumerate(self.bodies):
            i_at = i * 6
            for j, other_body in enumerate(self.bodies):
                j_at = j * 6
                y_prime[j_at] = y[i_at + 3]
                y_prime[j_at + 1] = y[i_at + 4]
                y_prime[j_at + 2] = y[i_at + 5]
                if i != j:
                    dx = y[i_at] - y[j_at]
                    dy = y[i_at + 1] - y[j_at + 1]
                    dz = y[i_at + 2] - y[j_at + 2]

                    r = np.linalg.norm([dx, dy, dz])
                    y_prime[i_at + 3] += dx * self.law(other_body.mass, body.mass)
                    y_prime[i_at + 4] += dy * self.law(other_body.mass, body.mass)
                    y_prime[i_at + 5] += dz * self.law(other_body.mass, body.mass)
        return y_prime 
    
    def __init__(self,
                 dt,
                 bodies=[],
                 law=None):
        self.dt = dt
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
                 until=0.0):
        # TODO: Build a `y` vector to make this code work for the `solve` method.
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
