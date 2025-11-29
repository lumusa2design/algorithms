def port_or(*values):
    for value in values:
        if value:
            return True

    return False

def simplify_and(*values):
    return any(values)