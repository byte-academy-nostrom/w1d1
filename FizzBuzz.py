#!/usr/bin/env python3

def Fizzbuzz(number):

    for number in range(0, number+1):
        if number%3==0 and number%5==0:
            print("FizzBuzz")
        elif number%3==0:
            print("Fizz")
        elif number%5==0:
            print("Buzz")
        else:
            print(number)

if __name__ == "__main__":
    print(Fizzbuzz(30))
