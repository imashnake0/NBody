import numpy as np

class System:
    def update_net_forces(self):
        for i, body in enumerate(self.bodies):
            body.net_force = 0
            for j, other_body in enumerate(self.bodies):
                if i != j:
                    k_1 = self.law(body.mass, 
                                    other_body.mass, 
                                    body.position[-1], 
                                    other_body.position[-1])
                    
                    k_2 = self.law(body.mass, 
                                    other_body.mass, 
                                    body.position[-1] + k_1*self.dt/2, 
                                    other_body.position[-1])
                    
                    k_3 = self.law(body.mass, 
                                    other_body.mass, 
                                    body.position[-1] + k_2*self.dt/2, 
                                    other_body.position[-1])
                    
                    k_4 = self.law(body.mass, 
                                    other_body.mass, 
                                    body.position[-1] + k_3*self.dt, 
                                    other_body.position[-1])


                    body.net_force += (self.dt/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)

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
