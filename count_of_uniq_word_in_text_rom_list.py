
def count_words(text, words):
    counter = 0
    uniq_words = []
    for word in words:
        if word in text:
            if word not in uniq_words:
                uniq_words.append(word)
                counter += 1       
    return counter
    
