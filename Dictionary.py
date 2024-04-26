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

#4. 