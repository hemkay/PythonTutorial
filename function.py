# function with no returns
from tkinter import W


def to_upper(word):
    word = word.upper()
    print(word)
    

def to_upper2(word):
    global name
    name = word.upper()
    print(name)

name = "ibrahim"
to_upper(name)

print(f"The name outside the function 1 is {name}")


to_upper2(name)

print(f"The name outside the function 2 is {name}")


def sum(x, y):
    w = x + y
    return w

sum_x = sum(2, 4)

print(f"Sum of 2 and 4 is {sum_x} ")


a = [1,2,3,4]

def change_list(a):
    a[0] = 6
    print(a)
    
change_list(a)


print(f"The list a outside the function is {a}")


x = 1
y = 0
while x <= 100:
    y = sum(y, x)
    x += 1
    
print(y)


def all_numbers(x,y):
    sum = 0
    for i in range(x, y + 1):
        sum += i
    return sum
print(all_numbers(0, 100))