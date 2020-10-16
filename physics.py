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
    variables['a'] = a
    return str(a)

def get_t_missing_s(variables):
    u = variables['u']
    v = variables['v']
    a = variables['a']
    t = (v-u)/a
    variables['t'] = t
    return str(t)

def get_u_missing_s(variables):
    v = variables['v']
    a = variables['a']
    t = variables['t']
    u = v - a * t
    variables['u'] = u
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
    variables['u'] = u
    return str(u)

def get_t_missing_v(variables):
    s = variables['s']
    u = variables['u']
    a = variables['a']
    common = math.sqrt((2*s*a + u**2) / a**2 )
    t1 = common - u * a / 4
    t2 = -1 * common - u * a / 4
    variables['t'] = t1
    return str(t1) + ', ' + str(t2)

def get_a_missing_v(variables):
    s = variables['s']
    u = variables['u']
    t = variables['t']
    a = (2 * s - t * u) / t**2
    variables['a'] = a
    return str(a)
     
# third equation

def get_s_missing_u(variables):
    v = variables['v']
    t = variables['t']
    a = variables['a']
    s = v * t - 0.5 * a * t**2
    get_u_missing_s(variables)
    return str(s)

def get_v_missing_u(variables):
    s = variables['s']
    t = variables['t']
    a = variables['a']
    v = (s + 0.5 * a * t**2)/t
    get_u_missing_v(variables)
    return str(v)

def get_t_missing_u(variables):
    s = variables['s']
    a = variables['a']
    v = variables['v']
    same = math.sqrt(v**2 - 2 * a *s)
    t1 = (v - same)/a
    t2 = (v + same)/a
    variables['t'] = t2
    if 'u' not in variables:
        get_u_missing_t(variables)
    return str(t1) + ',' + str(t2)

def get_a_missing_u(variables):
    s = variables['s']
    v = variables['v']
    t = variables['t']
    a = (2 * v * t - 2 * s)/t**2
    variables['a'] = a
    if 'u' not in variables:
        get_u_missing_a(variables)
    return str(a)

# fourth equation

def get_s_missing_a(variables):
    u = variables['u']
    v = variables['v']
    t = variables['t']
    s = 0.5 * (u + v) * t
    get_a_missing_s(variables)
    return str(s)

def get_u_missing_a(variables):
    s = variables['s']
    v = variables['v']
    t = variables['t']
    u = ( 2 * s / t ) - v
    variables['u'] = u
    if 'a' not in variables:
        get_a_missing_u(variables)
    return str(u)

def get_v_missing_a(variables):
    s = variables['s']
    u = variables['u']
    t = variables['t']
    v = ( 2 * s / t ) - u
    get_a_missing_v(variables)
    return str(v)

def get_t_missing_a(variables):
    s = variables['s']
    v = variables['v']
    u = variables['u']
    t = (2 * s)/(u+v)
    variables['t'] = t
    if 'a' not in variables:
        get_a_missing_t(variables)
    return str(t)

# last equation

def get_v_missing_t(variables):
    s = variables['s']
    a = variables['a']
    u = variables['u']
    v = math.sqrt(u**2 + 2 * a * s)
    get_t_missing_v(variables)
    return str(v) + ',' + str(-v)

def get_u_missing_t(variables):
    s = variables['s']
    a = variables['a']
    v = variables['v']
    u = math.sqrt(v**2 - 2 * a * s)
    variables['u'] = u
    if 't' not in variables:
        get_t_missing_u(variables)
    return str(u) + ',' + str(-u)

def get_a_missing_t(variables):
    s = variables['s']
    v = variables['v']
    u = variables['u']
    a = (v**2 - u**2) / 2 * s
    variables['a'] = a
    if 't' not in variables:
        get_t_missing_a(variables)
    return str(a)

def get_s_missing_t(variables):
    v = variables['v']
    a = variables['a']
    u = variables['u']
    s = (v**2 - u**2) / 2 * a
    get_t_missing_s(variables)
    return str(s)

def calculate(unknown_variable, missing_variable, variables):
    if unknown_variable == 'v' and missing_variable == 's':
        return get_v_missing_s(variables)
    elif unknown_variable == 'a' and missing_variable == 's':
        return get_a_missing_s(variables)
    elif unknown_variable == 't' and missing_variable == 's':
        return get_t_missing_s(variables)
    elif unknown_variable == 'u' and missing_variable == 's':
        return get_u_missing_s(variables)
    #second equation
    elif unknown_variable == 's' and missing_variable == 'v':
        return get_s_missing_v(variables)
    elif unknown_variable == 'u' and missing_variable == 'v':
        return get_u_missing_v(variables)
    elif unknown_variable == 't' and missing_variable == 'v':
        return get_t_missing_v(variables)
    elif unknown_variable == 'a' and missing_variable == 'v':
        return get_a_missing_v(variables)
    #third equation
    elif unknown_variable == 's' and missing_variable == 'u':
        return get_s_missing_u(variables)
    elif unknown_variable == 'v' and missing_variable == 'u':
        return get_v_missing_u(variables)
    elif unknown_variable == 't' and missing_variable == 'u':
        return get_t_missing_u(variables)
    elif unknown_variable == 'a' and missing_variable == 'u':
        return get_a_missing_u(variables)
    # fourth equation
    elif unknown_variable == 's' and missing_variable == 'a':
        return get_s_missing_a(variables)
    elif unknown_variable == 'v' and missing_variable == 'a':
        return get_v_missing_a(variables)
    elif unknown_variable == 'u' and missing_variable == 'a':
        return get_u_missing_a(variables)
    elif unknown_variable == 't' and missing_variable == 'a':
        return get_t_missing_a(variables)
    # last equation
    elif unknown_variable == 'v' and missing_variable == 't':
        return get_v_missing_t(variables)
    elif unknown_variable == 'u' and missing_variable == 't':
        return get_u_missing_t(variables)
    elif unknown_variable == 'a' and missing_variable == 't':
        return get_a_missing_t(variables)
    elif unknown_variable == 's' and missing_variable == 't':
        return get_s_missing_t(variables)
    else:
        return 0