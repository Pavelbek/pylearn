
# Function returns odds between the biggest and the smallest numbers in a list

# This is my solution, may be it is not so good

num_list = [-4, -5, 5, 4.2, 5.1]

def min_max(numbers):
    if not len(numbers):
        return 0
    min = num_list[0]
    max = num_list[0]
 
    for i in numbers:
        if i < min:
            min = i
        elif i > max:
            max = i
    return max - min
    
print(min_max(num_list))


# This is better solution taken from Checkio

def checkio(*args):
    return max(args) - min(args) if args else 0
	
	

    
