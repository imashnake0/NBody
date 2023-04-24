import numpy as np
import astropy.constants.codata2018 as coconst
import utils.RKUtils as rk

class System:
    def __init__(self,
                 dt,
                 bodies=[],
                 law=None):
        self.dt = dt
        self.bodies = np.array(bodies)
        self.law = law

        print(self.latest_vector())
        print(self.initial_vector())
        print(self.masses())

    # Now, for RK4 to work, we need to tell it how to conver y = (x_1, x'_1, x_2, x'_2, ...) to y' = (x'_1, x''_1, x'_2, x''_2, ...).
    # That is, we need to tell it how to differentiate each coordinate. This will enable it to calculate the next step of y, which is what we need.

    def latest_vector(self):
        tuples = np.array(list(map(lambda body: (body.position[-1], body.velocity[-1]), self.bodies)))
        return np.array([item for sublist in tuples for item in sublist])

    def initial_vector(self):
        tuples = np.array(list(map(lambda body: (body.position[0], body.velocity[0]), self.bodies)))
        return np.array([item for sublist in tuples for item in sublist])
    
    def masses(self):
        return np.array(list(map(lambda body: body.mass, self.bodies)))
    
    def derivator(self, t, y):
        # Here, we need to tell RK4 how to differentiate y, and then return it.
        y_prime = np.zeros_like(y)
        # Even indices of `y_prime` are just equal to the next index in y. 
        for i, _y in enumerate(y):
            if i % 2 == 0:
                y_prime[i] = _y

        G = coconst.G.value
        # The next part is extremely complicated since we need to find the *sum of the accelerations*. We need to hence change the odd indices.
        # TODO: Can we get rid of the enumerate?
        for j, _y2 in enumerate(y):
            if j % 2 != 0:
                for other_body in self.bodies:
                    # Prevent division by zero.
                    if np.linalg.norm(y[j - 1] - other_body.position[-1]) != 0:
                        # TODO: Might have to change signs.
                        y_prime[j] += G*other_body.mass*(y[j - 1] - other_body.position[-1])/(np.linalg.norm(y[j - 1] - other_body.position[-1]))**3

        # Now that we filled in all the blanks, we can return `y_prime`.
        return y_prime

    def simulate(self, until=0.0):
        t = 0.0
        while t < until:
            # This is the next step of our special vector
            step = rk.RK4_algorithm(f=self.derivator,
                                    t_i=0.,
                                    y_i=self.latest_vector(),
                                    dt=self.dt)
            
            for i, body in enumerate(self.bodies):
                body.position = np.append(body.position, [step[i*2]], axis=0)
                body.velocity = np.append(body.velocity, [step[i*2 + 1]], axis=0)
            t += self.dt
