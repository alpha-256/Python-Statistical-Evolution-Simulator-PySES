import re
import utils_child


def menu1():
    print("##################################################################")
    print("#                                                                #")
    print("#    Would you like to:                                          #")
    print("#                                                                #")
    print("##################################################################")
    print("#                                                                #")
    print("#    Please type in the number of the option                     #")
    print("#                                                                #")
    print("#    [1] Check for all test subjects                             #")
    print("#    [2] Check for only specified subject                        #")
    print("#    [3] Custom file?                                            #")
    print("#                                                                #")
    print("#                                                                #")
    print("##################################################################")


def menu2():
    print("##################################################################")
    print("#                                                                #")
    print("#    Data selection:                                             #")
    print("#                                                                #")
    print("##################################################################")
    print("#                                                                #")
    print("#    Please type in the number of the option                     #")
    print("#                                                                #")
    print("#    [1] Show all words with                                     #")
    print("#    [2] Show key words only                                     #")
    print("#                                                                #")
    print("#                                                                #")
    print("##################################################################")


def menu3():
    print("##################################################################")
    print("#                                                                #")
    print("#    Key Words:                                                  #")
    print("#                                                                #")
    print("##################################################################")
    print("#                                                                #")
    print("#    Please type in the number of the option                     #")
    print("#                                                                #")
    print("#    [1] Defealt key words                                       #")
    print("#    [2] Custom key words                                        #")
    print("#                                                                #")
    print("#                                                                #")
    print("##################################################################")


global ckw_list
ckw_list = []
# Questions for menu1
menu1()
option1 = int(input("Which Option? >>> "))
if option1 == 1:
    with open("Condition-1-All.txt", "r") as _f:
        text = _f.read()
elif option1 == 2:
    with open("Person.txt", "r") as _f:
        text = _f.read()
else:
    raise Exception("Unknown option provided")

# Questions for menu2
menu2()
option2 = int(input("Which Option? >>> "))
if option1 == 1:
    showWords = 0
elif option2 == 2:
    showWords = 1
else:
    raise Exception("Unknown option provided")

# Questions for menu3
menu3()
option3 = int(input("Which Option? >>> "))
if option3 == 1:
    keyDef = 0
    ckwLoop = 0
    while ckwLoop == 0:
        print("########################################################################")
        print("#                                                                      #")
        print("# If you are done, please type in 'qwerty' and press *Enter* two times #")
        print("#                                                                      #")
        print("########################################################################")
        ckw = str(input("Please press *Enter* after each word >>> : "))
        if ckw == "qwerty":
            pass
        else:
            pass
elif option3 == 2:
    keyDef = 1
else:
    raise Exception("Unknown option provided")

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

# Check DataSelection
if showWords == 0:
    showAllWords()
else:
    pass


# Print and save key words
print("##################")
with open("data.txt", "w+") as f:
    if keyDef == 0:
        for kw in ckw_list:
            x = str(kw) + " occoured: " + word_dict.get(kw.lower(), "0") + " time(s)"
            #x = str(x)
            print(x + "\n")
            f.write(x + "\n")
    else:
        kw_list = ["River", "Seals", "Hunt", "Shore", "Log", "Canoes", "Arrows", "Fellows", "Paddles",
                   "War", "Warriors", "Egulac", "Contorted", "Ecolar", "River", "Seals", "Hunt", "Shore", "Log"]
        for kw in kw_list:
            x = str(kw) + " occoured: " + word_dict.get(kw.lower(), "0") + " time(s)"
            #x = str(x)
            print(x + "\n")
            f.write(x + "\n")

#
