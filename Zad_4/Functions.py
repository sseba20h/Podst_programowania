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

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello world"))