
# Here we receive two strings and returns string as sorted intersection of two sets

def checkio(first, second):
        new = sorted(set(first.split(",")).intersection(set(second.split(","))))
        return ",".join(new)
	

# Not mine solution
	
def checkio(first, second):
    """
    set data type has useful methods.
    """
    first_set, second_set = set(first.split(",")), set(second.split(","))
    common = first_set.intersection(second_set)
    return ",".join(sorted(common))
	
# Either not mine solution
	
def checkio(first, second):
    first_set = set(first.split(","))
    second_set = set(second.split(","))
?
    return ",".join(sorted(first_set & second_set))