import numpy as np
import astropy.constants.codata2018 as coconst
import utils.EulerUtils as eu
import utils.RK4Utils as rk

class System:
    '''
    Class to define a system of bodies.

    Arguments
    ---------
    `dt`: Time is granular and the differential is defined.
    `algorithm`: The Algorithm used to solve for the motion of the bodies can be changed.
    `bodies`: List of `Body` objects that exist in the system.
    `law`: Law that governs the physics of the system.
    '''
    def __init__(self,
                 dt,
                 algorithm,
                 bodies=[],
                 law=None):
        self.dt = dt
        self.algorithm = algorithm
        self.bodies = np.array(bodies)
        self.law = law

    # Convinience method to get the latest vector for the algorithm(s) to use.
    def latest_vector(self):
        vec = np.array([self.bodies[0].position[-1], self.bodies[0].velocity[-1]])
        for body in self.bodies[1:]:
            vec = np.append(vec, [body.position[-1], body.velocity[-1]], axis=0)
        return vec

    def initial_vector(self):
        vec = np.array([self.bodies[0].position[0], self.bodies[0].velocity[0]])
        for body in self.bodies[1:]:
            vec = np.append(vec, [body.position[0], body.velocity[0]], axis=0)
        return vec
    
    # Builds a list of masses of the bodies that make up the system.
    def masses(self):
        return np.array(list(map(lambda body: body.mass, self.bodies)))

    def derivator(self, t, y):
        '''
        Tells the `algorithm` how to differentiate the input vector.
        The algorithm may use this to find the next vector (step into the future).

        Arguments
        ---------
        `t`: Time for time dependent derivative(s).
        `y`: The vector of the system that may be passed in the algorithm's implementation.
        '''
        G = coconst.G.value
        # Here, we need to tell RK4 how to differentiate y, and then return it.
        y_prime = np.zeros_like(y)
        # Even indices of `y_prime` are just equal to the next index in y. 
        for i, _y in enumerate(y):
            if i % 2 == 0:
                y_prime[i] = y[i + 1]

        for j, _y2 in enumerate(y):
            if j % 2 != 0:
                for other_body in np.delete(self.bodies, int((j - 1)/2)):
                    y_prime[j] += -G*other_body.mass*(y[j - 1] - other_body.position[-1])/(np.linalg.norm(y[j - 1] - other_body.position[-1]))**3


        # Now that we filled in all the blanks, we can return `y_prime`.
        return y_prime

    def simulate(self, until=0.0):
        '''
        Run the system for `until`.
        '''
        t = 0.0
        while t < until:
            # This is the next step of our special vector.
            step = self.algorithm(f=self.derivator,
                                      t_i=0.,
                                      y_i=self.latest_vector(),
                                      dt=self.dt)
            
            for i, body in enumerate(self.bodies):
                body.position = np.append(body.position, [step[i*2]], axis=0)
                body.velocity = np.append(body.velocity, [step[i*2 + 1]], axis=0)
            t += self.dt
