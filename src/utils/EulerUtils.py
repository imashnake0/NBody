def Euler_algorithm(f, t_i, y_i, dt):
    y_i_plus_1 = y_i + dt*f(t_i, y_i)
    return y_i_plus_1
