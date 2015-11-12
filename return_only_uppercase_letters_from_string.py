
# Here we receive some text and return only uppercase letters

some_string = "Foxtrot Uniform Charlie Kilo"

def find_message(text):
    """Find a secret message"""
    
    up_letters = ""
    
    for letter in text:
        if letter.isupper():
            up_letters += letter
    return up_letters
	
print(find_message(some_string))
	
	
# Below is example with generator function

def find_message(text):
    return ''.join(c for c in text if c.isupper())


