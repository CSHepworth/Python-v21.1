#Countdown

def countdown(num):
    num = 5
    countdownArray = []
    while num >= 0:
        countdownArray.append(num)
        num = num - 1
    return countdownArray

print(countdown(5))


#Print and Return

def printReturn(a, b):
    array = [a, b]
    print(array[0])
    return(array[1])

print(printReturn(1, 2))


#First Plus Length

def firstPlusLength(list):
    firstval = list[0]
    length = len(list)
    fpl = firstval + length
    return fpl

print(firstPlusLength([1, 2, 3, 4]))


#Value greater than second

def greaterThan2nd(list):
    newlist = []
    for i in range(0, len(list)):
        if(list[i] > list[1]):
            newlist.append(list[i])
        i += 1
    print(list[1])
    return newlist

print(greaterThan2nd([5, 3, 7, 2, 40]))


#This Length, That Value
def tltv(size, value):
    list = []
    i = 0
    while (i < size):
        list.append(value)
        i += 1
    return list

print(tltv(3,7))