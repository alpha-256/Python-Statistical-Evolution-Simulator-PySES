sentence = str(input("Sentence >>> "))
space_count = 0
for words in sentence:
    if words == "Fuck":
        space_count = space_count + 1
    if words == "fuck":
        space_count = space_count + 1
number_of_words = space_count + 1
print("The user entered:", sentence)
print("The number of words in the sentence is:", number_of_words)
