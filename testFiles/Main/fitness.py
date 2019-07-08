import csv
reproductionRate = dict()
with open('reproRate.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    reproductionRate[int(row[0])] = row[1]
print(reproductionRate)

survivalRate = dict()
with open('survRate.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    survivalRate[int(row[0])] = row[1]
print(survivalRate)

rRate = []
sRate = []

for row in reproductionRate:
    rRate.append(reproductionRate[row[0]])
print(rRate)

for row in survivalRate:
    sRate.append(survivalRate[row[0]])
print(sRate)
