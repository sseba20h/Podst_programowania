#1. Write a Python program to calculate the length of a string.

#abc = input("Podaj frazę do sprawdzenia:  ")
#print (len(abc))

#2. Write a Python program to count the number of characters (character frequency) in a string.

#abc = input("Podaj frazę do sprawdzenia:  ")

#print (abc))

#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

#z = input("Podaj frazę do sprawdzenia:  ")
#if len(z) < 2:
#    x = "Podane słowo jest nieprawidłowe"
#    print(x)
#else:
#    x = z[:2] + z[-2:]
#    print(x)

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

#x = input("Podaj wyraz:  ")
#char_1 = x[0]
#x = x.replace(char_1, '$')
#x = char_1 + x[1:]
#print (x)

#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

#a = input("Podaj 1 wyraz:  ")
#b = input("Podaj drugi wyraz:  ")
#new_a = b[:2] + a[2:]
#new_b = a[:2] + b[2:]
#print (new_a+'   '+new_b)

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

a = input("Podaj frazę:  ")
if len(a)<4:
    a=a
elif a[-3:]=="ing":
    a=a+"ly"
elif len(a)>4:
    a=a+"ing"

print(a)