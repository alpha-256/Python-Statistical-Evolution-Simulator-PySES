frequencyBook = {"0": "GABA",
                 "1": "NORA",
                 "2": "SERO",
                 "3": "GLUT",
                 "4": "ACET",
                 "5": "DOPA",
                 "6": "ENDO",
                 "7": "ADRE", }

"""
quantify data then measure it
"""
goal = "Hello World"
x = []
def neuronV0():
    x.append(len(goal))
    for character in goal:
        frequencyBook.append(character)
