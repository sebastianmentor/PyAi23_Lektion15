def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def check_if_possible_positiv_int(input):
    if isinstance(input, int):
        return True if input > -1 else False
    
    try:
        num = int(input)
        return True if num > -1 else True
    
    except ValueError:
        return False
    except TypeError:
        return False