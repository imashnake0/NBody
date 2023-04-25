import matplotlib.pyplot as plt

class PlotUtils:
    '''
    Class to make plotting easier (or harder).
    '''
    def plot(bodies):
        '''
        Plot two multiple lists agaist each other, the argument is a list of bodies.

        Arguments
        ---------
        `bodies`: List of `Body`s, the positions of which are plotted.
        '''
        fig, ax = plt.subplots()
        for body in bodies:
            ax.plot(body.position[:, 0], body.position[:, 1])
        
        ax.legend(list(map(lambda body: body.name, bodies)))
        ax.set(xlabel="x", ylabel="y")
        
        ax.set_aspect('equal')
        plt.savefig('plot.pdf')
        plt.show()
