"""
#Init Pop
#Fitness Def
#Selection Def


#Crossover Def
#Mutation
"""
"""
Reaction time affects survival rate
survivalRateA = bodyMass + reactionTime
survivalRateB = lifeTime + populationRate(acrossTime)

how to calculate populationRate acrossTime:
    set counter in ms
    for every count in the counter
        count population
"""

gene = ["A","T","C","G"]
chromosome = []
population = 100
class initPop:

#Environment Variables

mode = input(">>> Game Mode >>>")
startGenes = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9"]
mapSize = 500
#1 Million base pairs limit
pairLimit = 1000000

#NEW DEV
"""
Create 500 X 500 white image
As 1 object
    Create 10x9 black pixels
    create 10x1 yellow pixels
    0 = black
    1 = yellow
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
    0 0 0 0 0 0 0 0 0 1
"""
