import re

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
print("#                                                                #")
print("#                                                                #")
print("##################################################################")

optionn = int(input("Which Option? >>> "))

if optionn == 1:
    with open("Condition-1-All.txt", "r") as _f:
        text = _f.read()
elif optionn == 2:
    with open("Person.txt", "r") as _f:
        text = _f.read()
else:
    raise Exception("Unknown option provided")

# --- Text clean up ---

# split lines and sentence to words
text2 = text.lower().split("\n")
text = []
for line in text2:
    text.extend(line.split(" "))
text2 = [w for w in text if w]

# remove special symbol from the lists
text = []
for wrd in text2:
    text.append(re.sub(r"[:/\,.?!@#$%^&*()]", "", wrd))

text2 = text

#
word_dict = dict()
for wrd in text2:
    val = word_dict.get(wrd, None)
    if val: # exists
        word_dict[wrd] = val+1
    else:
        word_dict[wrd] = 1


#Print all words in sections
def showAllWords():
    or k, v in word_dict.items():
    print(k,"occoured",v, "time(s)")

#Save all words in sections
per_line_format = "{} occoured: {} times\n"
with open("Condition-1-Wordcount.txt", "w+") as ff:
    for k, v in word_dict.items():
        ff.write(per_line_format.format(k, v))

#Print and save key words
print("##################")
kw_list = ["River", "Seals", "Hunt", "Shore", "Log", "Canoes", "Arrows", "Fellows", "Paddles", "War", "Warriors", "Egulac", "Contorted", "Ecolar", "River", "Seals", "Hunt", "Shore", "Log", "canoes", "arrows", "fellows", "paddles", "war", "warriors", "egulac", "contorted", "ecolar" ]
with open("patty.txt", "w+") as f:
    for kw in kw_list:
        x = kw, "occoured:", word_dict.get(kw, "0 "), "time(s)"
        x = str(x)
        print(x + "\n")
        f.write(x + "\n")

#
