def index_power(array, n):
    """
        Find Nth power of the element with index N.
		If N bigger than quantity of elements in massive function returns -1
    """
    if n < len(array):
        return array[n] ** n
    return -1

	"""
	Other goo solution:
	
	def index_power(array, n):
    return array[n] ** n if n < len(array) else -1
	
	"""