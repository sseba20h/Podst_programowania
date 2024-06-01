#1
# import array
# for name in array.__dict__:
#     print(name)
#2
# class py_solution:
#     def sub_sets(self, sset):
#         return self.subsetsRecur([], sorted(sset))    
#     def subsetsRecur(self, current, sset):
#         if sset:
#             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
#         return [current]
# for name in py_solution.__dict__:
#     print(name)
#3
# class Student: 
#     def __init__(self, student_id, student_name, class_name):
#         self.student_id = student_id
#         self.student_name = student_name
#         self.class_name = class_name 
# student = Student('V12', 'Frank Gibson', 'V')
# print(student.__dict__)
#4
# import builtins 
# help(builtins.abs)
# print(builtins.abs(-155))
#5
# def student(student_id, student_name, student_class):
#     return f'Student ID: {student_id}\nStudent Name: {student_name}\nClass: {student_class}'
# print(student('S122', 'Wilson Medina', 'VI'))
#6
# def student_data(student_id, **kwargs):
#     print(f'\nStudent ID: {student_id}')
#     if 'student_name' in kwargs:
#         print(f"Student Name: $ {kwargs['student_name']}")
    
#     if 'student_name' and 'student_class' in kwargs:
#             print(f"\nStudent Name: $ {kwargs['student_name']}")
#             print(f"Student Class: $ {kwargs['student_class']}")

 
# student_data(student_id='SV12', student_name='Jean Garner')

# student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')
#7
# class Student:
#     pass  
# print(type(Student))
# print(Student.__dict__.keys())
# print(Student.__module__)
#8
# class Student:
#     pass 
# class Marks:
#     pass 
# student1 = Student()
# marks1 = Marks()
# print(isinstance(student1, Student))
# print(isinstance(marks1, Student))
# print(isinstance(marks1, Marks)) 
# print(isinstance(student1, Marks))
# print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
# print(issubclass(Student, object))
# print(issubclass(Marks, object)) 
#9
# class Student:
#     student_name = 'Terrance Morales'
#     marks = 93  
# print(f"Student Name: {getattr(Student, 'student_name')}")
# print(f"Marks: {getattr(Student, 'marks')}")
# setattr(Student, 'student_name', 'Angel Brooks')
# setattr(Student, 'marks', 95) 
# print(f"Student Name: {getattr(Student, 'student_name')}")
# print(f"Marks: {getattr(Student, 'marks')}")
#10
# class Student:
#     student_id = 'V10'
#     student_name = 'Jacqueline Barnett'  
# print("Original attributes and their values of the Student class:")
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f'{attr} -> {value}')
# print("\nAfter adding the student_class, attributes and their values with the said class:")
# Student.student_class  = 'V'
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f'{attr} -> {value}')
# print("\nAfter removing the student_name, attributes and their values from the said class:")
# del Student.student_name
# #delattr(Student, 'student_name')
# for attr, value in Student.__dict__.items():
#     if not attr.startswith('_'):
#         print(f'{attr} -> {value}')
#11
# class Student:
#     student_id = 'V10'
#     student_name = 'Jacqueline Barnett'
#     def display():
#         print(f'Student id: {Student.student_id}\nStudent Name: {Student.student_name}')
# print("Original attributes and their values of the Student class:")
# Student.display()
#12
# class Student:
#     school = 'Forward Thinking'
#     address = '2626/Z Overlook Drive, COLUMBUS' 
# student1 = Student()
# student2 = Student() 
# student1.student_id = "V12"
# student1.student_name = "Ernesto Mendez"
# student2.student_id = "V12"
# student2.marks_language = 85
# student2.marks_science = 93
# student2.marks_math = 95 
# students = [student1, student2]
# for student in students:
#     print('\n')
#     for attr in student.__dict__:
#         print(f'{attr} -> {getattr(student, attr)}')
#1
# class py_solution:
#     def int_to_Roman(self, num):
#         val = [
#             1000, 900, 500, 400,
#             100, 90, 50, 40,
#             10, 9, 5, 4,
#             1
#             ]
#         syb = [
#             "M", "CM", "D", "CD",
#             "C", "XC", "L", "XL",
#             "X", "IX", "V", "IV",
#             "I"
#             ]
#         roman_num = ''
#         i = 0
#         while  num > 0:
#             for _ in range(num // val[i]):
#                 roman_num += syb[i]
#                 num -= val[i]
#             i += 1
#         return roman_num


# print(py_solution().int_to_Roman(1))
# print(py_solution().int_to_Roman(4000))
#2
# class py_solution:
#     def roman_to_int(self, s):
#         rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         int_val = 0
#         for i in range(len(s)):
#             if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
#                 int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
#             else:
#                 int_val += rom_val[s[i]]
#         return int_val

# print(py_solution().roman_to_int('MMMCMLXXXVI'))
# print(py_solution().roman_to_int('MMMM'))
# print(py_solution().roman_to_int('C'))
#3
# class py_solution:
#    def is_valid_parenthese(self, str1):
#         stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
#         for parenthese in str1:
#             if parenthese in pchar:
#                 stack.append(parenthese)
#             elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
#                 return False
#         return len(stack) == 0

# print(py_solution().is_valid_parenthese("(){}[]"))
# print(py_solution().is_valid_parenthese("()[{)}"))
# print(py_solution().is_valid_parenthese("()"))
#4
# class py_solution:
#     def sub_sets(self, sset):
#         return self.subsetsRecur([], sorted(sset))
    
#     def subsetsRecur(self, current, sset):
#         if sset:
#             return self.subsetsRecur(current, sset[1:]) + self.subsetsRecur(current + [sset[0]], sset[1:])
#         return [current]

# print(py_solution().sub_sets([4,5,6]))
#5
# class py_solution:
#   def twoSum(self, nums, target):
#        lookup = {}
#        for i, num in enumerate(nums):
#            if target - num in lookup:
#                return (lookup[target - num], i )
#            lookup[num] = i
# print("index1=%d, index2=%d" % py_solution().twoSum((10,20,10,40,50,60,70),50))
#6
# class py_solution:
#  def threeSum(self, nums):
#         nums, result, i = sorted(nums), [], 0
#         while i < len(nums) - 2:
#             j, k = i + 1, len(nums) - 1
#             while j < k:
#                 if nums[i] + nums[j] + nums[k] < 0:
#                     j += 1
#                 elif nums[i] + nums[j] + nums[k] > 0:
#                     k -= 1
#                 else:
#                     result.append([nums[i], nums[j], nums[k]])
#                     j, k = j + 1, k - 1
#                     while j < k and nums[j] == nums[j - 1]:
#                         j += 1
#                     while j < k and nums[k] == nums[k + 1]:
#                         k -= 1
#             i += 1
#             while i < len(nums) - 2 and nums[i] == nums[i - 1]:
#                 i += 1
#         return result

# print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))
#7
# class py_solution:
#    def pow(self, x, n):
#         if x==0 or x==1 or n==1:
#             return x 

#         if x==-1:
#             if n%2 ==0:
#                 return 1
#             else:
#                 return -1
#         if n==0:
#             return 1
#         if n<0:
#             return 1/self.pow(x,-n)
#         val = self.pow(x,n//2)
#         if n%2 ==0:
#             return val*val
#         return val*val*x

# print(py_solution().pow(2, -3));
# print(py_solution().pow(3, 5));
# print(py_solution().pow(100, 0));
#8
# class py_solution:
#     def reverse_words(self, s):
#         return ' '.join(reversed(s.split()))


# print(py_solution().reverse_words('hello .py'))
#9
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()
#10

#11

#12

#1

#2

#3

#4