####Hello World#######

print('Hello, World!')

#######Variables#########

first_number = 1
second_number = 2
result = first_number + second_number

print(result)


######Strings#######

x = 'Hello, World!'
print(x[1])
print(len(x))

y = 'Hello'
z = 'World'
print(y + z)

######Boolean######
print(1 > 0)
print(1 == 2)
print(1 < 2)

######if-else######
a = 2
b = 3

if a < b:
    print('b is greater than a')
elif a == b:
    print('a is equal to b')
else:
    print('b is not greather than a')

###Loops###
fruits = ['apple', 'banana', 'orange']

for x in fruits:
    print(x)

for x in 'apple':
    print(x)

for x in fruits:
    if x == 'apple':
        print(x)

for x in fruits:
    print(x)
    if x == 'banana':
        break

i = 1
while i < 4:
    print(i)
    i += 1

def my_function():
    print('Hello, World! This is from my function.')

my_function()

def my_function2(my_argument):
    print(my_argument)

my_function2('Hello')

def add(a, b):
    return a + b

add(1, 1)