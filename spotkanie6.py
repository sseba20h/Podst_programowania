# a = float(input("Podaj pierwszą liczbę: "))
# b = float(input("Podaj drugą liczbę: "))

# c = (a + b) / 2

# print("Wynik: ", c)

# ///////////////////////////////////////////////////////////////////////////

# a = float(input("Podaj bok: "))

# c = a * a

# print("Pole kwadratu to: ",c)

# /////////////////////////////////////////////////////////////////////////

# import random

# a = random.randint(1, 6)

# print(a)

#///////////////////////////////////////////////////////////////////////

# def even(*numbers):
#     a = []
#     for i in numbers:
#         if i % 2 == 0:
#             a.append(i)
#     return a

# print(even(1, 2, 3, 4))

#///////////////////////////////////////////////////////////////////////////

# a = 0

# while a < 100:
#     b = input("Podaj liczbę: ")
#     a += int(b)
#     print(a)
# else:
#     print("Liczba przekracza sumę równą 100")

#///////////////////////////////////////////////////////////////////////

# a = []

# for i in range(10):
#     b = input("Podaj liczbę: ")
#     a.append(int(b))

# print("List is made of number:",a)

# def even(numbers):
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers

# print("The even number inside are: ",even(a))

#/////////////////////////////////////////////////////////////////////

# import random

# n = int(input("Podaj długość listy: "))

# random_list = [random.randint(1, 50) for _ in range(n)]
# print("Lista losowa:")
# print(random_list)

# filtered_list = [x for x in random_list if x < 11 or x > 20]
# print("Lista po usunięciu elementów:")
# print(filtered_list)