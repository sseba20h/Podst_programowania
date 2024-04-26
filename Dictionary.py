#1. Write a Python program to sort (ascending and descending) a dictionary by value.
"""
def sort_dict_ascending(d):
    sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
    return sorted_dict

def sort_dict_descending(d):
    sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict

d = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
ascending_dict = sort_dict_ascending(d)
descending_dict = sort_dict_descending(d)

print("Ascending order:", ascending_dict)
print("Descending order:", descending_dict)
"""

#2. Write a Python program to add a key to a dictionary.
"""
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

student["country"] = "USA"

print(student)
"""

#3. Write a Python program to add a key to a dictionary.

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

new_dict = {}
for d in [dict1, dict2, dict3]:
    new_dict.update(d)

#print(new_dict)

#4. Write a Python script to check whether a given key already exists in a dictionary.

def check_key(key):
    students = {
    'Theodore': 19,
    'Roxanne': 22,
    'Mathew': 21,
    'Betty': 20
}

    if key in students:
        return print(f'The key {key} exists in the dictionary.')
    else:
        return print(f'The key {key} does not exist in the dictionary.')

#check_key('Betty')

#5. Write a Python program to iterate over dictionaries using for loops.

d = {'x': 10, 'y': 20, 'z': 30} 

# for dict_key, dict_value in d.items():
#     print(dict_key, '->', dict_value)

#6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

#n = int(input("Input a number "))
d = dict()

for x in range(1, n + 1):
    d[x] = x * x

#print(d)

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

d = dict()
for x in range(1, 16):
#    d[x] = x ** 2

#print(d)

#8. Write a Python script to merge two Python dictionaries.

#d1 = {'a': 100, 'b': 200}
#d2 = {'x': 300, 'y': 200}
#d = d1.copy()

#d.update(d2)

#print(d)

#9. Write a Python program to iterate over dictionaries using for loops.

# d = {'Red': 1, 'Green': 2, 'Blue': 3}

# for color_key, value in d.items():
#     print(color_key, 'corresponds to ', d[color_key])

#10. Write a Python program to sum all the items in a dictionary.

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = sum(my_dict.values())
#print(result)

#11. Write a Python program to multiply all the items in a dictionary.

my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
result = 1

for key in my_dict:
    result = result * my_dict[key]

print(result) 