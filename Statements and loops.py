#1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

nl = []

for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))

#print(','.join(nl))

#2. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.

# #temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
# degree = int(temp[:-1])
# i_convention = temp[-1]

# if i_convention.upper() == "C":
#     result = int(round((9 * degree) / 5 + 32))
#     o_convention = "Fahrenheit"  # Set the output convention as Fahrenheit
# elif i_convention.upper() == "F":
#     result = int(round((degree - 32) * 5 / 9))
#     o_convention = "Celsius"  # Set the output convention as Celsius
# else:
#     print("Input proper convention.")
#     quit()

# #print("The temperature in", o_convention, "is", result, "degrees.") 

#3. Write a Python program to guess a number between 1 and 9.

# import random
# target_num, guess_num = random.randint(1, 10), 0

# while target_num != guess_num:
#     guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))

# print('Well guessed!') 

#4. Write a Python program to construct the following pattern, using a nested for loop.

# n = 5
# for i in range(n):
#     for j in range(i):
#         print('* ', end="")
#     print('')

# for i in range(n, 0, -1):
#     for j in range(i):
#         print('* ', end="")
#     print('') 

#5. Write a Python program that accepts a word from the user and reverses it.

# word = input("Input a word to reverse: ")

# for char in range(len(word) - 1, -1, -1):
#     print(word[char], end="")

# print("\n")

#6. Write a Python program to count the number of even and odd numbers in a series of numbers

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# count_odd = 0
# count_even = 0

# for x in numbers:
#     if not x % 2:  # If 'x' modulo 2 equals 0, it's even
#         count_even += 1
#     else:
#         count_odd += 1

# print("Number of even numbers:", count_even)
# print("Number of odd numbers:", count_odd) 

#7. Write a Python program that prints each item and its corresponding type from the following list.

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

# for item in datalist:
#     print("Type of", item, "is", type(item)) 

#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

# for x in range(6):
#     if (x == 3 or x == 6):
#         # If 'x' is 3 or 6, skip to the next iteration without executing the code below
#         continue
#     print(x, end=' ')

# print("\n")

#9. Write a Python program to get the Fibonacci series between 0 and 50.

# x, y = 0, 1

# while y < 50:
#     print(y)
    
#     x, y = y, x + y

#10. Write a Python program that iterates the integers from 1 to 50.

# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz) 

#11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array.

# row_num = int(input("Input number of rows: "))

# col_num = int(input("Input number of columns: "))

# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col] = row * col

# print(multi_list) 

#12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

# lines = []

# while True:
#     l = input()
    
#     if l:
#         lines.append(l.upper())
#     else:
#         break;

# for l in lines:
#     print(l) 

#13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input.

# items = []

# num = [x for x in input().split(',')]

# for p in num:
#     x = int(p, 2)
    
#     if not x % 5:
#         items.append(p)

# print(','.join(items))

#14. Write a Python program that accepts a string and calculates the number of digits and letters.

# s = input("Input a string")
# d = l = 0

# for c in s:
#     if c.isdigit():
#         d = d + 1
#     elif c.isalpha():
#         l = l + 1
#     else:
#         pass

# print("Letters", l)
# print("Digits", d)

#15. Write a Python program to check the validity of passwords input by users.

# import re
# p = input("Input your password")
# x = True

# while x:  
#     if (len(p) < 6 or len(p) > 12):
#         break
#     elif not re.search("[a-z]", p):
#         break
#     elif not re.search("[0-9]", p):
#         break
#     elif not re.search("[A-Z]", p):
#         break
#     elif not re.search("[$#@]", p):
#         break
#     elif re.search("\s", p):
#         break
#     else:
#         print("Valid Password")
#         x = False
#         break

# if x:
#     print("Not a Valid Password")

#16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number.

# items = []
# for i in range(100, 401):
#     s = str(i)
    
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
#         items.append(s)

# print(",".join(items)) 

#17. Write a Python program to print the alphabet pattern 'A'.

# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
        
#         if (((column == 1 or column == 5) and row != 0) or ((row == 0 or row == 3) and (column > 1 and column < 5))):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "

#     result_str = result_str + "\n"

# print(result_str)

#18. Write a Python program to print the alphabet pattern 'D'.

# result_str = ""
# for row in range(0, 7):
#     for column in range(0, 7):
        
#         if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 5)) or (column == 5 and row != 0 and row != 6)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "

#     result_str = result_str + "\n"

# print(result_str)

#19. Write a Python program to print the alphabet pattern 'E'.

# result_str = ""

# for row in range(0, 7):
#     for column in range(0, 7):
        
#         if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "

#     result_str = result_str + "\n"

# print(result_str)

#20. Write a Python program to print the alphabet pattern 'G'.

# result_str = ""

# for row in range(0, 7):
#     for column in range(0, 7):
        
#         if ((column == 1 and row != 0 and row != 6) or ((row == 0 or row == 6) and column > 1 and column < 5) or (row == 3 and column > 2 and column < 6) or (column == 5 and row != 0 and row != 2 and row != 6)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "

#     result_str = result_str + "\n"

# print(result_str) 