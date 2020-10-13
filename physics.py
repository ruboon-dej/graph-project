
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

def calculate(unknown_variable, missing_variable, variables):
    if unknown_variable == 'v' and missing_variable == 's':
        return get_v_missing_s(variables)
    elif unknown_variable == 'a' and missing_variable == 's':
        return get_a_missing_s(variables)
    elif unknown_variable == 't' and missing_variable == 's':
        return get_t_missing_s(variables)
    else:
        return 0