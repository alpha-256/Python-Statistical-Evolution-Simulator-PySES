import math
start = 1
mid = 50
end = 100
number = int(input("Number pls >>> "))
tryCount = 0
loop = 0
while loop < 1:
    if number >= start and number <= mid:
        tryCount = tryCount + 1
        print(tryCount)
        if mid == number:
            print("Number is", mid)
        else:
            mid = mid / 2
            loop = loop + 1
    elif number >= mid and number <= end:
        end = end / 2
        tryCount = tryCount + 1
        print(tryCount)
    else :
        print("NUmber is", end)
        loop = loop + 1
