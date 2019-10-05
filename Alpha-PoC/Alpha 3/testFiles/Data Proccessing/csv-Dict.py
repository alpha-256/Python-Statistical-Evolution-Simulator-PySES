import csv
stuff = dict()
with open('reproRate.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
    stuff[int(row[0])] = row[1]
print(stuff[1])
