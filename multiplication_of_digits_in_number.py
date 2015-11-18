# As input we have some number, for example 12030456 . As output we must receive multiplication of all digits of number except 0.

# This is my solution. Maybe not so good.

some_number = 4609870

def checkio(number):
    new_num = 1
    for num in str(number):
        if int(num) == 0:
            continue
        else:
            new_num *= int(num)

    return new_num  
	
print(checkio(some_number))


# Not mine solution

def checkio(number):
    """
    Convert into the string and iterate.
    """
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res
	
