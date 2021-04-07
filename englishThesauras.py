import json
from difflib import SequenceMatcher,get_close_matches



def read_word(word):
    if word in data:
        return "".join(data_structure.get(word))
    elif word.title() in data:
        return "".join(data_structure.get(word.title()))
    elif word.upper() in data:
        return "".join(data_structure.get(word.upper()))
    elif len(get_close_matches(word,data_structure.keys()))>0:
        similar_word = get_close_matches(word,data_structure.keys())[0]
        answer = input(f'Did you mean, \"{similar_word}\" instead? Press Yes(Y) or No(N) :')
        if answer.lower() in ['y','yes']:
            return "".join(data_structure.get(similar_word))
        elif answer.lower() in ['n','no']:
            return "The word doesn't exist. Please double check it."
        else:
            return "Did not understand your entry."

    else:
        return "The word doesn't exist. Please double check it."
if __name__== "__main__":
    data = json.load(open('data.json'))
    data_structure = dict(data)
    word = input('Enter a word:').lower()
    print(read_word(word))