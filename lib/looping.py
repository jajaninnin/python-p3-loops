#!/usr/bin/env python3

def happy_new_year():
    num = 10
    while True:
        print(num)
        num = num - 1
        if num == 0:
            break
    print("Happy New Year!")

def square_integers(int_list):
    square_list = []
    for item in int_list:
        square = item ** 2
        square_list.append(square)
    return square_list

def fizzbuzz():
    num = 1
    while True:
        if (num % 3 == 0) and (num % 5 ==0):
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        num += 1
        if num > 100:
            break

fizzbuzz()