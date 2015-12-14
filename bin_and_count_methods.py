# Here we receives int number, makes binary number from it and returns count of '1'

number = 25

def checkio(number):
    return bin(number).count('1')

# Not mine solution	
	
checkio=lambda n:bin(n).count('1')