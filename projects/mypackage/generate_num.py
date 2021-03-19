import numpy as np

def generate_rand_int(start=0, stop=10):
    """This function returns a random integer.
    
    Args:
        start (int): the lower limit of the generated integer
        stop  (int): the upper limit of the generated integer
    Returns:
        rand_integer (int): the generated integer
    """
    rand_integer = np.random.randint(start, stop)
    return rand_integer


def generate_rand_float(start=0, stop=1):
    """This function returns a random integer.
    
    Args:
        start (int): the lower limit of the generated float number
        stop  (int): the upper limit of the generated float number
    Returns:
        rand_float (int): the generated float number
    """
    rand_float = np.random.uniform(start, stop)
    return rand_float