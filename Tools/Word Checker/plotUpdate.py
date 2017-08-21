import re

global ckw_list

ckw_list = []

def raw_word_counter(raw_loaded_text, case_sensitive=False):

    # split into lines
    raw_text = raw_loaded_text
    raw_text = raw_text.split("\n")

    # split into words
    text = []
    for item in text:
        item = item.lower()
        print(item)
    for line in raw_text:
        for word in line.split(" "):

            # word clean up, remove whitespace and special characters
            word = word.strip()
            word = re.sub(r"[:/\,.?!@#$%^&*()]", "", word)
            
            text.append(word)

    word_dict = dict()

    if bool(case_sensitive) is True:

        for word in text:

            val = word_dict.get(word, None)

            if val:  # exists
                word_dict[word] = val + 1
            else:
                word_dict[word] = 1

    else:  # Case insensitive

        for word in text:

            word_key = word.lower()

            val = word_dict.get(word_key, None)

            if val:  # exists
                word_dict[word_key] = val + 1
            else:
                word_dict[word_key] = 1

    return word_dict


with open("The Martian.txt", "r") as _f:
        text = _f.read()
word_dict = raw_word_counter(text, case_sensitive=False)

for kw in ckw_list:
    x = str(kw) + " occoured: " + word_dict.get(kw.lower(), "0") + " time(s)"
    #x = str(x)
    print(x + "\n")