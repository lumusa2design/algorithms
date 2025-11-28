def port_and(*values):
    for value in values:
        if not value:
            return False

    return True

def simplify_and(*values):
    return all(values)
