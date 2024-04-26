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

n = int(input("Input a number "))
d = dict()

for x in range(1, n + 1):
    d[x] = x * x

print(d)

#7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.

#d = dict()
#for x in range(1, 16):
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

#my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
#result = sum(my_dict.values())
#print(result)

#11. Write a Python program to multiply all the items in a dictionary.

m_dct = {'data1': 100, 'data2': -54, 'data3': 247}
result = 1

for key in m_dct:
    result = result * m_dct[key]

#print(result)

#12. Write a Python program to remove a key from a dictionary.

myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#print(myDict)

if 'a' in myDict:
    del myDict['a']

#print(myDict)

#13. Write a Python program to map two lists into a dictionary.

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
color_dictionary = dict(zip(keys, values))

#print(color_dictionary)

#14. Write a Python program to sort a given dictionary by key

color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}

#for key in sorted(color_dict):
#    print("%s: %s" % (key, color_dict[key]))

#15. Write a Python program to get the maximum and minimum values of a dictionary.

my_dict = {'x': 500, 'y': 5874, 'z': 560}
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

#print('Maximum Value: ', my_dict[key_max])
#print('Minimum Value: ', my_dict[key_min])

#16. Write a Python program to get a dictionary from an object's fields.

class dictObj(object):
    def __init__(self):
        self.x = 'red'
        self.y = 'Yellow'
        self.z = 'Green'
    
    def do_nothing(self):
        pass

test = dictObj()

#print(test.__dict__) 

#17. Write a Python program to remove duplicates from the dictionary.

student_data = {
    'id1': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id2': {
        'name': ['David'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id3': {
        'name': ['Sara'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    },
    'id4': {
        'name': ['Surya'],
        'class': ['V'],
        'subject_integration': ['english, math, science']
    }
}

result = {}

for key, value in student_data.items():
    if value not in result.values():
        result[key] = value

#print(result)

#18. Write a Python program to check if a dictionary is empty or not.

my_dict = {}

# if not bool(my_dict):
#     print("Dictionary is empty")

#19. Write a Python program to combine two dictionary by adding values for common keys.

from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
d = Counter(d1) + Counter(d2)

#print(d)

#20. Write a Python program to print all distinct values in a dictionary.

L = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
#print("Original List: ", L)

u_value = set(val for dic in L for val in dic.values())
#print("Unique Values: ", u_value)
