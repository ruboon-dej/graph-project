import math

def get_v_missing_s(variables):
    u = variables['u']
    a = variables['a']
    t = variables['t']
    v = u + a * t
    return v

def get_a_missing_s(variables):
    u = variables['u']
    v = variables['v']
    t = variables['t']
    a = (v-u)/t
    return a

def get_t_missing_s(variables):
    u = variables['u']
    v = variables['v']
    a = variables['a']
    t = (v-u)/a
    return t

def get_u_missing_s(variables):
    v = variables['v']
    a = variables['a']
    t = variables['t']
    u = v - a * t
    return u

# the second equation

def get_s_missing_v(variables):
    u = variables['u']
    t = variables['t']
    a = variables['a']
    s = u * t + 0.5 * a * t**2
    return s

def get_u_missing_v(variables):
    s = variables['s']
    t = variables['t']
    a = variables['a']
    u = s/t - 0.5 * a * t
    return u

 #def get_t_missing_v(variables):
    # s = variables['s']
    # u = variables['u']
    # a = variables['a']
    # t1 = math.sqrt()
    # return t1

def get_a_missing_v(variables):
    s = variables['s']
    u = variables['u']
    t = variables['t']
    a = 2 * s / ( t**3 * u )
    return a
     
def calculate(unknown_variable, missing_variable, variables):
    if unknown_variable == 'v' and missing_variable == 's':
        return get_v_missing_s(variables)
    elif unknown_variable == 'a' and missing_variable == 's':
        return get_a_missing_s(variables)
    elif unknown_variable == 't' and missing_variable == 's':
        return get_t_missing_s(variables)
    elif unknown_variable == 'u' and missing_variable == 's':
        return get_u_missing_s(variables)
    elif unknown_variable == 's' and missing_variable == 'v':
        return get_s_missing_v(variables)
    elif unknown_variable == 'u' and missing_variable == 'v':
        return get_u_missing_v(variables)
    elif unknown_variable == 't' and missing_variable == 'v':
        return get_t_missing_v(variables)
    elif unknown_variable == 'a' and missing_variable == 'v':
        return get_a_missing_v(variables)
    else:
        return 0