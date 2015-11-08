def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) > 0:
        num = 0
        for item in array:
            if item % 2 == 0:
                num += item
        return num * array[len(array) - 1]
    return 0
