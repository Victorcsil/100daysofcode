# DAY 5

# EXERCISE 6 Fizz buzz

'''
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
'''
            
# DAY 5 PROJECT

abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

import random
password_lenght = int(input("How many characters would you like in your password? (Minimum 6, can use letters, numbers and symbols) "))
if password_lenght < 6:
    print("The password must have at least 6 characters.")
    quit()
nr_letters = int(input("How many letters would you like in your password? "))
if nr_letters > password_lenght:
    print("The number of letters must be less than the total number of characters in the password.")
    quit()
password_lenght -=  nr_letters
nr_numbers = int(input("How many numbers would you like in your password? "))
if nr_numbers > password_lenght:
    print("The number of numbers must be less than the total number of characters in the password.")
    quit()

nr_symbols = password_lenght - nr_numbers
password = []

for num in range(1, nr_letters + 1):
    password.append(random.choice(abc))
for num in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))
for num in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))

print("".join(random.sample(password, len(password))))
