def RK4_algorithm(f, t_i, y_i, dt):
    # Know k_1y:
    k_1y = f(t_i, y_i)

    # Find k_2y:
    k_2y = f(t_i + dt/2, y_i + k_1y/2)

    # Find k_3y:
    k_3y = f(t_i + dt/2, y_i + k_2y/2)

    # Find k_4y:
    k_4y = f(t_i + dt, y_i + k_3y)

    # Find y_{i + 1}:
    y_i_plus_1 = y_i + (dt/6)*(k_1y + 2*k_2y + 2*k_3y + k_4y)

    return y_i_plus_1
