def one(x, y, z):
    a = 1
    if x >= y and x >= z:
        a = x
    elif z >= y and z >= x:
        a = z
    else:
        a = y
    return a

#print(one(5, 7, 12))

def suma(numbers):
    total = 0
    
    for x in numbers:
        total += x
    
    return total

#print(suma((8, 2, 3, 0, 7)))

def iloczyn(numbers):
    total = 1
    
    for x in numbers:
        total *= x
    
    return total

#print(iloczyn((2, 3, 5, 4)))

def string_reverse(str1):
    rstr1 = ''  
    index = len(str1)
    
    while index > 0:
        rstr1 += str1[index - 1]       
        index = index - 1
    
    return rstr1

#print(string_reverse('1234abcd'))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#n = int(input("Input a number to compute the factorial: "))

#print(factorial(n))

def test_range(n):
    if n in range(3, 9):
        print("%s is in the range" % str(n))
    else:
        print("The number is outside the given range.")

#test_range(4)

def distinct_elements(*args):
    seen = {}
    result = []
    for element in args:
        if element not in seen:
            result.append(element)
            seen[element] = True
    return result

#print(distinct_elements(1 ,1 ,2 , 55, 55, 4, 2))

def prime(*numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [n for n in numbers if is_prime(n)]

#print(prime(1, 15, 22, 13, 5))

def is_even_num(l):
    enum = []
    
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    
    return enum

#print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def palindrome(s):
    return s == s[::-1]

#print(palindrome('qweewq'))

def pascal(n):
    triangle = [[1 for _ in range(i+1)] for i in range(n)]
    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    for row in triangle:
        print(' ' * (n - len(row)), end='')
        print(' '.join(str(num) for num in row))

#pascal(5)

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if set(s.lower()) >= set(alphabet):
        return "Pangram!"
    else:
        return "Not a pangram."

#print(is_pangram("The quick brown fox jumps over the lazy dog"))
#print(is_pangram("Hello world"))

#
# items = [n for n in input().split('-')]
# items.sort()

# print('-'.join(items))

def printValues():
    l = list()
    
    for i in range(1, 21):
        l.append(i**2)   
    print(l)

#printValues()

mycode = 'print("hello world")'

code = """
def sum(x,y):
    return x+y

print('Sum of 2 and 3 is: ',sum(2,3))
"""

#exec(mycode)
#exec(code)

def test(a):
    def add(b):
        nonlocal a
        a += 1
        return a + b
    return add
func = test(4)

#print(func(4))

# from time import sleep
# import math

def delay(fn, ms, *args):
    sleep(ms / 1000)
    
    return fn(*args)

# print("Square root after specific milliseconds:") 

# print(delay(lambda x: math.sqrt(x), 100, 16))

# print(delay(lambda x: math.sqrt(x), 1000, 100))

# print(delay(lambda x: math.sqrt(x), 2000, 25100))

def abc():
    x = 1
    y = 2
    str1 = "w3resource"
    
    print("Python Exercises")

#print(abc.__code__.co_nlocals) 

def string_test(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    
    for c in s:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
        else:
            pass
    
#     print("Original String: ", s)
    
#     print("Number of Upper case characters: ", d["UPPER_CASE"])
    
#     print("Number of Lower case Characters: ", d["LOWER_CASE"])

# string_test('The quick Brown Fox')

def perfect_number(n):
    sum = 0
    
    for x in range(1, n):
        if n % x == 0:
            sum += x
    
    return sum == n

#print(perfect_number(6))

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped

@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"


print(hello())