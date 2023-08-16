#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown >= 1:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")
happy_new_year()

    

def square_integers(int_list):
    squared_list = [x ** 2 for x in int_list]
    return squared_list

# Call the function with an example list
result = square_integers([1, 2, 3, 4, 5])
print(result) 


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

# Call the function to see the output
fizzbuzz()

