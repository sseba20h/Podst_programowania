#1. Write a Python program to calculate the length of a string.

#abc = input("Podaj frazę do sprawdzenia:  ")
#print (len(abc))

#2. Write a Python program to count the number of characters (character frequency) in a string.

#abc = input("Podaj frazę do sprawdzenia:  ")

#print (abc))

#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

z = input("Podaj frazę do sprawdzenia:  ")

if len(z) < 2:
    x = "Podane słowo jest nieprawidłowe"
    print(x)
else:
    x = z[:2] + z[-2:]
    print(x)