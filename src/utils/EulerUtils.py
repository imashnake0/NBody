def Euler_algorithm(f, t_i, y_i, dt):
    '''
    For steps involved, refer to: https://en.wikipedia.org/wiki/Euler_method#First-order_process.
    '''
    y_i_plus_1 = y_i + dt*f(t_i, y_i)
    return y_i_plus_1
