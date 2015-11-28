# Our goal here is to check if at least one word finish with starting suffix on next word

words_set = {"hello", "la", "hellow", "cow"}
def checkio(words_set):
    for word in sorted(words_set):
        for index in range(len(word) + 1):
            slc = 1
            suffix = word[len(word)- slc: ]
            if any([x.startswith(suffix) for x in sorted(words_set)]):
                return True
            slc += 1
    return False
    
print(checkio(words_set))