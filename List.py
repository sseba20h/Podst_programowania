#1. Write a Python program to sum all the items in a list.

def one(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers

#print(one([1, 2, -8]))

#2. Write a Python program to multiply all the items in a list.

def two(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

#print(two([1, 2, -8]))

#3. Write a Python program to get the largest number from a list.

def three(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max

#print(three([1, 2, -8, 0]))

#4. Write a Python program to get the smallest number from a list.

def four(list):
    min = list[0]
    for a in list:
        if a < min:
            min = a
    return min

#print(four([1, 2, -8, 0])) 

#5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.

def five(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
    return ctr

#print(five(['abc', 'xyz', 'aba', '1221']))

#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

def last(n):
    return n[-1]

def sort_list_last(tuples):
    return sorted(tuples, key=last)

#print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#7. Write a Python program to remove duplicates from a list.

a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

dup_items = set()
uniq_items = []

for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

#print(dup_items)

#8. Write a Python program to check if a list is empty or not.

""""
l = []
if not l:
    print('List is empty')
else:
    print('List is not empty')
"""

#9. Write a Python program to clone or copy a list.

original_list = [10, 22, 44, 23, 4]

new_list = list(original_list)

#print(f'Old list is: {original_list}\nNew list is: {new_list}')

#10. Write a Python program to find the list of words that are longer than n from a given list of words.

def long_words(n, str):
    word_len = []
    txt = str.split(" ")

    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len

#print(long_words(3, "The quick brown fox jumps over the lazy dog"))

#11. Write a Python function that takes two lists and returns True if they have at least one common member.

def common_data(list1, list2):
    result = False

    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

# print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
# print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9])) 

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]

#print(color)

#13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]
#print(array)

#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

num = [7, 8, 120, 25, 44, 20, 27]
num = [x for x in num if x % 2 != 0]

#print(num)

#15. Write a Python program to shuffle and print a specified list.

from random import shuffle

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)

#print(color)

#16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included).

def printElements():
    l = list()
    for i in range(1, 31):
        l.append(i**2)
    print(l[:5])
    print(l[-5:])

#printElements()

#18. Write a Python program to generate all permutations of a list in Python.

import itertools

#print(list(itertools.permutations([1, 2, 3])))

#59. Write a Python program to check whether the n-th element exists in a given list.

def find_nth_element(lst, n):
    if n < len(lst):
        return lst[n]
    else:
        return None

my_list = [1, 2, 3, 4, 5]
n = my_list.index(max(my_list))

nth_element = find_nth_element(my_list, n)
if nth_element is not None:
    print(f"The {n}-th element in the list is: {nth_element}")
else:
    print(f"The {n}-th element does not exist in the list")

#60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.

x = [(4, 1), (1, 2), (6, 0)]

#print(min(x, key=lambda n: (n[1], -n[0])))

