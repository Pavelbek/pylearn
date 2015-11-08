def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) > 0:
        num = 0
        loop_len = len(array)
        for item in range(0,loop_len,2):
            num += array[item]
        return num * array[len(array) - 1]
    return 0