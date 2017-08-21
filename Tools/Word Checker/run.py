import re
import utils_child

def menu2():
    print("##################################################################")
    print("#                                                                #")
    print("#    Data selection:                                             #")
    print("#                                                                #")
    print("##################################################################")
    print("#                                                                #")
    print("#    Please type in the number of the option                     #")
    print("#                                                                #")
    print("#    [1] Show aaall words with                                     #")
    print("#    [2] Show key words only                                     #")
    print("#                                                                #")
    print("#                                                                #")
    print("##################################################################")

global ckw_list

ckw_list = []

# Load input data from Person.txt
with open("Person.txt", "r") as _f:
        text = _f.read()

# Count words
word_dict = utils_child.raw_word_counter(text, case_sensitive=False)

# Print all words in sections
def showAllWords():
    for k, v in word_dict.items():
        print(k, "occoured", v, "time(s)")

# Save all words in sections
def saveAllWords():
    per_line_format = "{} occoured: {} times\n"
    with open("Condition-1-Wordcount.txt", "w+") as ff:
        for k, v in word_dict.items():
            ff.write(per_line_format.format(k, v))

# Print and save key words

print("##################")

with open("data.txt", "w+") as f:
        for kw in ckw_list:
            x = str(kw) + " occoured: " + word_dict.get(kw.lower(), "0") + " time(s)"
            #x = str(x)
            print(x + "\n")
            f.write(x + "\n")
        kw_list = ["River", "Seals", "Hunt", "Shore", "Log", "Canoes", "Arrows", "Fellows", "Paddles",
                   "War", "Warriors", "Egulac", "Contorted", "Ecolar", "River", "Seals", "Hunt", "Shore", "Log"]
        for kw in kw_list:
            sun = str(word_dict.get(kw.lower()))
            x = str(kw) + " occoured: " + sun, "0" + " time(s)"
            output = x, "\n"
            print(output)
            f.write(str(x, "\n"))
