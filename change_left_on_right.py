
# Here we need to change all "right" words in string to word "left"
# We created separator "," and join sequence separated by our separator
# Finally we checked if the word exist in sequence change it on other word and return string


first_tuple = ("left", "right", "left", "stop")

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    sequence = []
    s = ","
    for word in phrases:
        sequence.append(word)
    string = s.join(sequence)
    if "right" in string:
        return string.replace("right", "left")
    return string
    
print(left_join(first_tuple))


# Not mine solution but better than mine. 

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return (",".join(phrases)).replace("right","left")