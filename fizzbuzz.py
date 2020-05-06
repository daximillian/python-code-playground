#!/usr/bin/env python3

def fizzbuzz(max_number):
    """
    A function that outputs the string representation of numbers from 1 to n. For multiples of three 
    it outputs “Fizz”, for multiples of five it outputs “Buzz”, and for multiples of both it outputs
    “FizzBuzz”.

    Args:
        Number to count to. 
    """
    FIZZ = 3
    BUZZ = 5
    FIZZBUZZ = 15
    if isinstance(max_number, int):
        if max_number > 0:
            number = 1
            while number <= max_number:
                if number % FIZZBUZZ == 0:
                    print("FizzBuzz")
                elif number % FIZZ == 0:
                    print("Fizz")
                elif number % BUZZ == 0:
                    print("Buzz")
                else:
                    print(str(number))
                number += 1
        else:
            print("Error: Number must be positive '{}'.".format(max_number))   
    else:
        print("Error: Number must be an integer '{}'.".format(max_number))

if __name__ == "__main__":
   print("====23=====")
   fizzbuzz(23)
   print("=====-1====")
   fizzbuzz(-1)
   print("=====0=====")
   fizzbuzz(0)
   print("===apple===")
   fizzbuzz('apple')
   print("=====3=====")
   fizzbuzz(3)
   print("=====5=====")
   fizzbuzz(5)
   print("====30=====")
   fizzbuzz(30)