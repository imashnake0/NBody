def RK4_algorithm(f, t_i, y_i, dt):
    '''
    For steps involved, refer to: https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods.
    '''
    # Know k_1y:
    k_1y = f(t_i, y_i)

    # Find k_2y:
    k_2y = f(t_i + dt/2, y_i + dt*k_1y/2)

    # Find k_3y:
    k_3y = f(t_i + dt/2, y_i + dt*k_2y/2)

    # Find k_4y:
    k_4y = f(t_i + dt, y_i + dt*k_3y)

    # Find y_{i + 1}:
    y_i_plus_1 = y_i + (dt/6)*(k_1y + 2*k_2y + 2*k_3y + k_4y)

    return y_i_plus_1
