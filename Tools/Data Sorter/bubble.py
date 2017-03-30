temp = [37,32,36,35,31,34]
def bubbleSort(temp):
    y = 1
    for check in temp:
        if len(temp) != y:
            if temp[y-1] > temp[y]:
                temp[y-1], temp[y] = temp[y], temp[y-1]
            else:
                pass
        else:
            pass
        y += 1
print(temp, "\n")
for data in temp:
    bubbleSort(temp)
print(temp, "\n")
