from os import access


num1 = 42 #variable declaration, initialize int
num2 = 2.3 #variable declaration, initialize float
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize directory
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #log statement, access value
person['name'] = 'George' #access value, change value
person['eye_color'] = 'blue' #access value, change value, NameError: name 'eye_color' is not defined
print(fruit[2]) #log statement, access value

if num1 > 45: #if
    print("It's greater") #log statement
else: #else
    print("It's lower") #log statment

if len(string) < 5: #if, length check
    print("It's a short word!") #log statement
elif len(string) > 15: #else if, length check
    print("It's a long word!") #log statement
else: #else
    print("Just right!") #log statement

for x in range(5): #for loop start
    print(x) #log statement
for x in range(2,5): #for loop increment
    print(x) #log statement
for x in range(2,10,3): #for loop increment
    print(x) #log statement
x = 0 #variable declaration, initialize int
while(x < 5): #while loop start
    print(x) #log statement
    x += 1 #while loop increment

pizza_toppings.pop() #list delete value, IndexError: list indext out of range
pizza_toppings.pop(1) #list delete value

print(person) #log statement 
person.pop('eye_color') #AttributeError: 'tuple' object has no attribute 'pop'
print(person) #log statement

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #if
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if
        break #for loop break

def print_hello_ten_times(): #parameter
    for num in range(10): #argument
        print('Hello') #return, log statement

print_hello_ten_times() #call function

def print_hello_x_times(x): #parameter
    for num in range(x): #argument
        print('Hello') #return, log statement

print_hello_x_times(4) #call function

def print_hello_x_or_ten_times(x = 10): #parameter
    for num in range(x): #argument
        print('Hello') #return, log statement

print_hello_x_or_ten_times() #call function
print_hello_x_or_ten_times(4) #call function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)