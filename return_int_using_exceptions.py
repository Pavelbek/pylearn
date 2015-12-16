# Here we are receiving two arguments: number as string in different radix and returns int number or -1
# We are using exceptions handling here

def checkio(str_number, radix):
    try:
        return int(str_number,radix)
    except ValueError:
        return -1
		
checkio("AF", 16) 
checkio("101", 2) 
checkio("101", 5) 
checkio("Z", 36)
checkio("AB", 10) 

# Not mine variant

def checkio(*a):
    try: return int(*a)
    except ValueError: return -1