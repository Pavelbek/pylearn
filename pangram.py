# Here we check if there all characters from alphabet in a string and return True if so.
# This is my not so good solution

text = "The quick brown fox jumps over the lazy dog."

def check_pangram(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = []
    for letter in text.lower():
        if letter not in res and letter in alphabet:
            res.append(letter)
    return True if len(res) == 26 else False
        
print(check_pangram(text))

# This is not mine and smart solution

from string import ascii_lowercase

def check_pangram(text):
    return set(ascii_lowercase).issubset(set(text.lower()))