import random
import re

def raw_word_counter(raw_loaded_text):
    # split into lines
    raw_text = raw_loaded_text
    raw_text = raw_text.split("\n")

    # split into words
    text = []
    for line in raw_text:
        for word in line.split(" "):

            # word clean up, remove whitespace and special characters
            word = word.strip()
            word = re.sub(r"[:/\,.?!@#$%^&*()]", "", word)

            text.append(word)

    word_dict = text
    return word_dict

    for word in word_dict:
        checkMem = word_dict[word][0]
        

text0 = input(">>> ")
text = text0.lower()
word_dict = raw_word_counter(text)
print(type(word_dict))
