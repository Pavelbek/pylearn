# Our goal is to check if one word finishes by other full word. Example: duckwalk , walk  . And if we see this function returns True. 

words_set = {"hello", "lo", "he"}
def check(words_set):
    for word in words_set:
        for end_w in words_set:
            if end_w == word:
                continue
            elif word.endswith(end_w):
                return True
    return False
    
check(words_set)


# Not mine solution
def checkio(words):
    """
    You can iterate throught set.
    """
    for w1 in words:
        for w2 in words:
            if w1 != w2 and (w1.endswith(w2) or w2.endswith(w1)):
                return True
    return False