num_list = [-4, -5, 5, 4.2, 5.1]

def min_max(numbers):

    min = 0
    max = 0

    for i in numbers:
        if i < min:
            min = i
        elif i > max:
            max = i
    return abs(min) + abs(max)
    
print(min_max(num_list))
    
