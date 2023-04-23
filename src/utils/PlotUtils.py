import matplotlib.pyplot as plt

class PlotUtils:
    '''
    Class to make plotting easier (or harder).
    '''
    def plot(x, y, title):
        '''
        Plot two lists agaist each other, the arguments are tuples.

        Arguments
        ---------
        `x`: Tuple containing a list of points on the x-axis followed by the title of the x-axis.
        `y`: Tuple containing a list of points to plot followed by the title of the y-axis.
        `title`: Title of the plot.
        '''
        fig, ax = plt.subplots()
        for graph in zip(x[:-1], y[:-1]):
            ax.plot(graph[0], graph[1])

        ax.set(xlabel=x[-1], ylabel=y[-1], title=title)
        ax.set_aspect('equal')
        plt.show()
