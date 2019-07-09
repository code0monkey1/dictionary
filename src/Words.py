import csv


my_word=""
unique_words=set()

while(True):
    word= (input("If no more words , enter $ else enter word \n "))
    if word=='$':
        break
    if word.isalpha():
        my_word += word.lower()

    else:
        print("Please only enter valid alphabets")

def word_is_anagram(new_word):
    return  sorted(new_word)==sorted(my_word)


with open("dictionary.csv") as dictionary:
    my_dict=csv.DictReader(dictionary)
    for line in my_dict:
        new_word=(line['word']).lower()

        if new_word not in unique_words  and word_is_anagram(new_word):
            unique_words.add(new_word)
            print(f"The word is {new_word} ")
        else:
            continue






