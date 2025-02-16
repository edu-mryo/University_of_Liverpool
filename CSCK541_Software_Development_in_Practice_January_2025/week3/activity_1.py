import random

# 1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).


def div_7_5():
    nl = []
    for i in range(1500, 2701):
        if i % 7 == 0 and i % 5 == 0:
            nl.append(i)
    print(nl)


# div_7_5()

# 2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
# [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius
# Click me to see the sample solution


def temperature_conversion(temperature):
    unit = input(
        f'Enter the temperature unit you would like to convert {temperature} into (c or f): ')
    if unit == 'f':
        converted_value = round((temperature * 9/5)+32)
        print(f"{temperature} degree Celsius is {converted_value} degree Farenheit")
        return
    if unit == 'c':
        converted_value = round((temperature - 32)*5/9)
        print(f"{temperature} degree Farenheit is {converted_value} degree Celsius")
        return
    else:
        print("Problem with the input. Conversion system ending")


# temperature_conversion(60)


# 3. Write a Python program to guess a number between 1 and 9.
# Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
# Click me to see the sample solution

def number_guess():
    answer = random.randint(1, 9)
    while True:
        print(answer)
        guess = input("Choose number between 1 and 9: ")
        if int(guess) == answer:
            print(f"Well guessed ! the answer is {answer}")
            break
        else:
            print(f"No. The answer is not {guess}")
    print("Guessing game terminated")


# number_guess()

# 4. Write a Python program to construct the following pattern, using a nested for loop.

def create_pattern():
    n = 10

    for i in range(n):
        for j in range(i):
            print("*", end="")
        print("")
        if i == n-1:
            for i in range(n, 0, -1):
                for j in range(i):
                    print("*", end="")
                print("")


# create_pattern()

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# Click me to see the sample solution

# 5. Write a Python program that accepts a word from the user and reverses it.
# Click me to see the sample solution


def word_reverse():
    word = input("Say something: ")
    print(word[::-1])


# word_reverse()

# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
# Click me to see the sample solution

def count_even_odd_num():
    even_numbers = []
    odd_numbers = []
    starting_range = input("Choose a range of numbers. Pick Starting Range: ")
    ending_range = input("Choose a range of numbers. Pick Ending Range: ")
    for i in range(int(starting_range), int(ending_range)+1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    print(f"Number of Even Numbers: {len(even_numbers)} {even_numbers}")
    print(f"Number of Odd Numbers: {len(odd_numbers)} {odd_numbers}")


# count_even_odd_num()

# 7. Write a Python program that prints each item and its corresponding type from the following list.
# Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
# Click me to see the sample solution


def check_item_type():
    datalist = [1452, 11.23, 1+2j, True, 'w3resource',
                (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

    for i in datalist:
        print(f"The type of {i} is {type(i)}")


# check_item_type

# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# Note : Use 'continue' statement.
# Expected Output : 0 1 2 4 5
# Click me to see the sample solution


def skip_3_6():
    final_output = []
    for i in range(6):
        if i == 3 or i == 6:
            continue
        final_output.append(i)
    print(f"Here is the final output {final_output}")


# skip_3_6()

# 9. Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34
# Click me to see the sample solution

def fibonacci():
    f0, f1 = 0, 1
    while f1 < 50:
        print(f1, end=' ')
        f0, f1 = f1, f0+f1

# fibonacci()

# 10. Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz
# Click me to see the sample solution


def fizz_buzz():
    for i in range(1, 51):
        if (i % 3 == 0 and i % 5 == 0):
            print(i, "FIZZBUZZ")
        elif i % 3 == 0:
            print(i, "fizz")
        elif i % 5 == 0:
            print(i, "buzz")
        else:
            print(i)


# fizz_buzz()
