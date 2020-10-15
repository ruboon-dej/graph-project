import math

def get_v_missing_s(variables):
    u = variables['u']
    a = variables['a']
    t = variables['t']
    v = u + a * t
    return str(v)

def get_a_missing_s(variables):
    u = variables['u']
    v = variables['v']
    t = variables['t']
    a = (v-u)/t
    return str(a)

def get_t_missing_s(variables):
    u = variables['u']
    v = variables['v']
    a = variables['a']
    t = (v-u)/a
    return str(t)

def get_u_missing_s(variables):
    v = variables['v']
    a = variables['a']
    t = variables['t']
    u = v - a * t
    return str(u)

# the second equation

def get_s_missing_v(variables):
    u = variables['u']
    t = variables['t']
    a = variables['a']
    s = u * t + 0.5 * a * t**2
    return str(s)

def get_u_missing_v(variables):
    s = variables['s']
    t = variables['t']
    a = variables['a']
    u = s/t - 0.5 * a * t
    return str(u)

def get_t_missing_v(variables):
    s = variables['s']
    u = variables['u']
    a = variables['a']
    t1 = math.sqrt((sa + u**2) / a**2 ) - u * a / 4
    t2 = - 1 * math.sqrt((s * a + u**2) / a**2 ) - (u * a / 4)
    return str(t1) + ', ' + str(t2)

def get_a_missing_v(variables):
    s = variables['s']
    u = variables['u']
    t = variables['t']
    a = 2 * s / ( t**3 * u )
    return str(a)
     
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