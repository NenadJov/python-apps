import json
from difflib import get_close_matches

data = json.load(open("original.json"))

def dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]#for words that start with capital letter
    elif word.upper() in data:
        return data[word.upper()]#for acronyms
    elif len(get_close_matches(word, data.keys())) > 0:
        #return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please check it."
        
word = input("Enter word: ")

#print(dictionary(word))
output = dictionary(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)