str1 = "hey ho 8 let's go"
str2 = "hey ho let's 6 go"
str3 = "hey ho 3 let's fucking go"
str4 = "8 8 8 8"
str5 = "GH FGH fgh dfhg"
str6 = "dsf"
str7 = "1"

# Here we check if there 3 words in row in string if it is True we return True and False otherwise. 

def three_words(text):
    sentence = text.split()
    counter = 0
    for i in range(0, len(sentence)):
        if not sentence[i].isdigit():
            counter += 1
            if counter == 3:
                return True
        else:
            counter = 0
    return False


print(three_words(str7))


# This is not mine solution. But it is better than mine.

def checkio(words):
    count = 0
    
    for word in words.split():
        if word.isalpha():
            if count == 2:
                return True
            count += 1
        else:
            count = 0
    
    return False