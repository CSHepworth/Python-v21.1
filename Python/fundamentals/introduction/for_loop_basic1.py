# Basics

for i in range(151):
    print(i)

# Multiples of Five

for i in range(5, 1001, 5):
    print(i)


#Counting, the Dojo Way

i = 1;
while i <= 100:
    if i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)
    i += 1


# Whoa. That Sucker's Huge

i = 0
sum = 0
while i <= 500000:
    if i % 2 != 0:
        sum += i
    i += 1
print(sum)


# Countdown by 4s

i = 2018
while i > 0:
    print(i)
    i -= 4


#Flexible Counter

lowNum = 2
highNum = 9
mult = 3
while lowNum <= highNum:
    if (lowNum % 3 == 0):
        print(lowNum)
    lowNum += 1
