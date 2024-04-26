#1. Write a Python program to calculate the length of a string.

def one(abc):
    a = len(abc)
    return a

#2. Write a Python program to count the number of characters (character frequency) in a string.

def two(q):
    dict = {}
    for n in q:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

#3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead.

def three(z):
    if len(z) < 2:
       x = "Podane słowo jest nieprawidłowe"
    else:
        x = z[:2] + z[-2:]
    return x 

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def four(x):
    char_1 = x[0]
    x = x.replace(char_1, '$')
    x = char_1 + x[1:]
    return x

#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def five(a, b):
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]
    return new_a+'   '+new_b

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def six(a):
    if len(a)<4:
        a=a
    elif a[-3:]=="ing":
        a=a+"ly"
    elif len(a)>4:
        a=a+"ing"
    return a

#7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def seven(x):
    not_a = x.find('not')
    poor = x.find('poor')
    if poor > not_a and not_a > 0 and poor > 0:
        x = x.replace(x[not_a:(poor+4)], 'good')
    else:
        x = x
        return x

#8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.

def eight(x):
    l = x.split(',')
    l.sort(key=len, reverse=True)
    longest_word = l[0]
    length = len(longest_word)
    return f'Najdłuższy wyraz to: {longest_word}      A jego długość to: {length}'

#9. Write a Python program to remove the nth index character from a nonempty string.

def nine(x, y):
    q = x[:y]
    w = x[y+1:]
    return q + w

#10. Write a Python program to change a given string to a newly string where the first and last chars have been exchanged.

def ten(x):
    return x[-1:] + x[1:-1] + x[:1]

#11. Write a Python program to remove characters that have odd index values in a given string.

def eleven(x):
    result = ""
    for i in range(len(x)):
        if i % 2 == 0:
            result = result + x[i]
    return result

#12. Write a Python program to count the occurrences of each word in a given sentence.

def twelve(x):
    y = dict()
    words = x.split()
    for words in words:
        if words in y:
            y[words] += 1
        else:
            y[words] = 1
    return y

#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

#user_input = input("What's your favorite language? ")
#print("My favorite language is ", user_input.upper())
#print("My favorite language is ", user_input.lower()) 

#14. Write a Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).

items = input("Input comma-separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

#print(twelve('the quick brown fox jumps over the lazy dog.'))