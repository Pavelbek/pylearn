# here we sorting list by absolute value from the lowest number


# my solution

def checkio(numbers_array):
    return list(sorted(numbers_array, key=lambda x: abs(x)))
	
# not mine solution/ We can use buil-in functions without any arguments and the function will be applied to all items in iterable

def checkio(numbers_array):
    """
    The magic of the key :)
    """
    return tuple(sorted(numbers_array, key=abs))