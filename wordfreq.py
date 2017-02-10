

text = ""
with open("wordlist.txt", "r") as _f:
    text = _f.read()

text2 = text.split("\n")
text = []
for line in text2:
    text.extend(line.split(" "))
text2 = [w for w in text if w]

word_dict = dict()
for wrd in text2:
    val = word_dict.get(wrd, None)
    if val: # exists
        word_dict[wrd] = val+1
    else:
        word_dict[wrd] = 1

print(word_dict)



