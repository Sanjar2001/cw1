# def get_squares_sum(*args) -> int:
#     our_listik = []
#     for i in args:
#         squared = int(i)**2
#         our_listik.append(squared)
#     return sum(our_listik)

# inputik = input()
# numbers = inputik.split()
# print(get_squares_sum(*numbers))


# import math

# def calculate_yearly_grade(n, grades):
#     # Отфильтровать четные оценки
#     even_grades = [grade for grade in grades if grade % 2 == 0]
    
#     # Вычислить среднее арифметическое четных оценок
#     average = sum(even_grades) / len(even_grades)
    
#     # Округлить результат до ближайшего целого числа, не превышающего его
#     rounded_average = math.floor(average)
    
#     return rounded_average

# # Чтение входных данных
# n = int(input())
# grades = list(map(int, input().split()))

# # Вычисление годовой оценки
# yearly_grade = calculate_yearly_grade(n, grades)

# # Вывод результата
# print(yearly_grade)


# from collections import Counter

# def top5_letters(words): 
#     combined_string = ''.join(words).replace(' ', '')
#     letters_counter = Counter(combined_string)

#     top_5 = letters_counter.most_common(5)
#     return top_5

# inputik = input()
# print(top5_letters(inputik))


# class FunnyList:
#     def __init__(self):
#         self.listik = []

#     def append(self, item):
#         self.listik.insert(0, item)

#     def __iter__(self):
#         return iter(self.listik)

# # Создание экземпляра класса FunnyList
# funnylist = FunnyList()

# # Добавление элементов в список
# funnylist.append(10)
# funnylist.append(12)
# funnylist.append(13)

# # Печать всех элементов списка
# print(*funnylist)  # Ожидаемый вывод: 13 12 10


# def is_palindrome(num):
#     num_str = str(num)
#     return num_str == num_str[::-1]

# def finding_the_palindrome(num):
#     if is_palindrome(num):
#         return num 
    
#     lower_num = num - 1 
#     while True: 
#         if is_palindrome(lower_num):
#             return lower_num
        
#         lower_num -= 1 

# input_number = int(input("Enter a number: "))
# nearest_palindrome = finding_the_palindrome(input_number)
# print(f"The nearest palindrome to {input_number} is {nearest_palindrome}.")
    

