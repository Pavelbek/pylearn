first_tuple = ("left", "right", "left", "stop")

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    string = ""
    for word in phrases:
        string += word + ","
    if "right" in string:
        return string.replace("right", "left")
    return string
    
print(left_join(first_tuple))
