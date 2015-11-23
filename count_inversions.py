# Here count quantity of inversions.
# I made double loop to compare every item with all other, but second loop starts from new item because we don't need to compare with previous # items. only with farther.


# This is my solution. Maybe it doesn't perfect.

def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    counter = 0
    el = 0
    for i in sequence:
        for num in sequence[el:]:
            if i > num:
                counter += 1
        el += 1
    return counter
	
	
# Not mine solution.

def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
	
# Here we take index and element of the index.
# Here we don't check element with itself we check it with all elements followed by it. We take index of current element and add to it 1 .
	
    count = 0
    for i, x in enumerate(sequence[:-1]):
        for y in sequence[i+1:]:
            if x > y: count += 1
    return count

