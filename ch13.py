# Python Basics Chapter 13:
# =========================

# 1. Enumerate Function

# We use enumerate function with for loop to track position of our
# item in iterable.

# How we can do this without enumerate function -

# names = ['anshul', 'manya', 'atul', 'ritu']

# pos = 0
# for name in names:
#     print(f"{pos} : {name}")
#     pos += 1

# for i in range(len(names)):
#     print(f"{i} : {names[i]}")

# With enumerate function -

# names = ['anshul', 'manya', 'atul', 'ritu']

# for name in enumerate(names):
    # print(name)

# for index, name in enumerate(names):
#     print(f"{index} : {name}")

# Exercise -

# Define a function that take two arguments -
# 1.) list containing strings
# 2.) string that want to find in your list and this function will
# return the index of string in your list and if string is not present
# then return not found.

# Exercise Solution -

# def index_finder(astr, alist):
#     if astr in alist:
#         for i, s in enumerate(alist):
#             if s == astr:
#                 return i
#     return 'not found'

# print(index_finder("Anshul", ["Anurag", "Anshul"]))

# My Own Enumerate Function -

# def my_enumerate(iterable):
# 	return [(i, iterable[i]) for i in range(len(iterable))]

# 2. Map Function

# nums = [1, 2, 3]

# def square(a):
    # return a ** 2

# def is_even(a):
#     return a%2==0

# print(square(1))
# print(square(2))
# print(square(3))

# squares = square(1), square(2), square(3)

# print(squares)
# print(list(squares))

# new = []
# for num in nums:
# new.append(square(num))
# print(new)

# Using list comprehension -

# print([a * a for a in nums])

# Using map() -

# print(map(square, nums))

# sqaures = map(square, nums)

# print(tuple(sqaures))
# print(list(sqaures))

# Using map() and lambda function -

# print(tuple(map(lambda a : a * a, nums)))
# print(list(map(lambda a : a * a, nums)))

# names = ['anshul', 'manya', 'anurag', 'neha']

# length = map(len, names)

# for i in length:
#     print(i)

# print(list(map(len, names)))

# for i in range(len(names)):
#     print(f"{i} : {names[i]}")

# My Own Map  Function -

# def my_map(function, iterable):
# 	return [function(item) for item in iterable]

# 3. Filter Function

# def is_even(a):
#     return a % 2 == 0

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# evens = []
# for num in nums:
#     evens.append(is_even(num))
# print(evens)

# evens = [i for i in nums if i % 2 == 0]
# print(evens)

# evens = list(filter(is_even, nums))
# print(evens)

# evens = tuple(filter (is_even, nums))
# print(evens)

# evens = list(filter(lambda a : a % 2 == 0, nums))
# print(evens)

# evens = tuple(filter(lambda a : a % 2 == 0, nums))
# print(evens)

# evens = filter(lambda a : a % 2 == 0, nums)

# for i in evens:
#     print(i)

# My Own Filter Function -

# def my_filter(function, iterable):
#     return [item for item in iterable if function(item) == True]

# print(my_filter(is_even, nums))

# 4. Iterator Vs Iterable

# nums = [1, 2, 3, 4] # list, tuples, string ---> iterables

# squares = map(lambda a : a ** 2, nums) # iterator

# print(nums)
# print(squares)

# for i in squares:
#     print(i)

# for i in nums:  
#     print(i)
 
# for loop internally calls iter function
# iter(nums) # ---> iterator
# next(iter(nums))

# num_iter = iter(nums)

# print(num_iter)

# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))
# print(next(num_iter))

# for i in squares:
#     print(i)

# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))

# 5. Zip Function Part - 1

# user_id = ['user1', 'user2', 'user3']
# names = ['anshul', 'anurag', 'afzal']

# print(zip(user_id, names))
# print(list(zip(user_id, names)))
# print(tuple(zip(user_id, names)))
# print(dict(zip(user_id, names)))

# for i in zip(user_id, names):
#     print(i)

# user_id = ['user1', 'user2']
# names = ['anshul', 'anurag', 'afzal']

# for i in zip(user_id, names):
#     print(i)

# 6. Zip Function Part - 2

# l1 = [1, 3, 5, 7]
# l2 = [2, 4, 6, 8]

# print(list(zip(l1, l2)))

# l = [(1, 2), (3, 4), (5, 6), (7, 8)]

# * operator with zip

# print(list(zip(*l)))

# l1, l2 = list(zip(*l))

# print(list(l1))
# print(list(l2))

# greater = []
# for pair in zip(l1, l2):
#     greater.append(max(pair))
# print(greater)

# greater = [max(pair) for pair in zip(l1, l2)]
# print(greater)

# def my_zip(l1, l2):
# 	return[(l1[i], l2[i]) for i in range(len(l1))]

# print(my_zip([1, 2, 3], [4, 5, 6]))

# 7. Advance Function Practice - 1

 # Define a function take any number of lists containing number
# [1, 2, 3], [4, 5, 6], [7, 8, 9]
# Return Average
# (1 + 4 + 7) / 3, (2, 5, 8) / 3, (3, 6, 9) / 3

# Try to make this anonymous function in one line using lambda

# def average_finder(l1, l2):
#     average = []
#     for pair in zip(l1, l2):
#         average.append(sum(pair) / len(pair))
#     return average

# print(average_finder([1, 2, 3], [4, 5, 6]))

# def average_finder(*args):
#     average = []
#     for pair in zip(*args):
#         average.append(sum(pair) / len(pair))
#     return average

# print(average_finder([1, 2, 3], [4, 5, 6], [7, 8, 9]))

# average_finder = lambda *args : [sum(pair) / len(pair) for pair in zip(*args)]
# print(average_finder([1, 2, 3], [4, 5, 6], [7, 8, 9]))

# 8. Any And All Functions

# nums1 = [2, 4, 6, 8, 10]
# nums2 = [1, 2, 3, 4, 5, 6]

# evens1 = [True if num1 % 2 == 0 else False for num1 in nums1]
# evens2 = [True if num2 % 2 == 0 else False for num2 in nums2]

# print(evens1)
# print(evens2)

# print(all([True, True, True, True, True]))
# print(all([False, True, False, True, False, True]))

# print(any([True, True, True, True, True]))
# print(any([False, True, False, True, False, True]))

# evens1 = [num1 % 2 == 0 for num1 in nums1]
# evens2 = [num2 % 2 == 0 for num2 in nums2]

# print(evens1)
# print(evens2)

# evens1 = all([num1 % 2 == 0 for num1 in nums1])
# evens2 = all([num2 % 2 == 0 for num2 in nums2])

# print(evens1)
# print(evens2)

# evens1 = any([num1 % 2 == 0 for num1 in nums1])
# evens2 = any([num2 % 2 == 0 for num2 in nums2])

# print(evens1)
# print(evens2)

# 9. Any And All Practice

# def my_sum(*args):
#     try:
#         if all([(type(eval(arg)) == int or type(eval(arg)) == float) for arg in args]):
#             total = 0
#             for num in args:
#                 total += eval(num)
#             return total
#         else:
#             return 'Wrong Input !!'
#     except Exception as e:
#         return "Wrong Input !!"

# print(my_sum(2, 4, 6, 3.5, 'Anshul', [1, 5, 'Garg']))
# print(my_sum(2, 4, 6, 3.5, 1, 5))

# l = input("Enter any numbers : ").split()
# print(my_sum(*l))

# 10. Advance Min() And Max() Function

# nums = [1, 2, 4, 5, 7]

# print(max(nums))
# print(min(nums))

# def func(item):
#     return len(item)

# names = ['Anshul', 'manya']

# print(max(names))

# print(max(names, key=func))
# print(min(names, key=func))
# print(max(names, key=lambda item : len(item)))

# students1 = {
#     'anshul' : {'score' : 90, 'age' : 24},
#     'anurag' : {'score' : 85, 'age' : 22},
#     'afzal' : {'score' : 75, 'age' : 20}
# }

# print(max(students1, key=lambda item : students1[item]['score']))
# print(max(students1, key=lambda item : students1[item]['age']))

# print(min(students1, key=lambda item : students1[item]['score']))
# print(min(students1, key=lambda item : students1[item]['age']))

# students2 = [
#     {'name' : 'anshul', 'score' : 90, 'age' : 24},
#     {'name' : 'anurag', 'score' : 85, 'age' : 22},
#     {'name' : 'afzal', 'score' : 75, 'age' : 20}
# ]

# print(max(students2, key=lambda item : item.get('score)))
# print(min(students2, key=lambda item : item.get('score')))

# print(max(students2, key=lambda item : item.get('score'))['name'])
# print(max(students2, key=lambda item : item.get('age'))['name'])

# print(min(students2, key=lambda item : item.get('score'))['name'])
# print(min(students2, key=lambda item : item.get('age'))['name'])

# 11. Advance Sorted Function

# fruits1 = ['grapes', 'mango', 'apple']

# fruits1.sort()
# print(fruits1)

fruits2 = ('grapes', 'mango', 'apple')

sorted_fruits2 = sorted(fruits2)
print(sorted_fruits2)

# fruits3 = {'grapes', 'mango', 'apple'}

# sorted_fruits3 = sorted(fruits3)
# print(sorted_fruits3)

# smartphones = [
#     {'model' : 'Samsung Galaxy Note 20 Ultra', 'price': 100000},
#     {'model' : 'Apple 11 Pro Max', 'price': 150000},
#     {'model' : 'Oneplus 8 Pro', 'price': 60000}
# ]

# print(sorted(smartphones, key=lambda item : item['model']))
# print(sorted(smartphones, key=lambda item : item['price']))

# print(sorted(smartphones, key=lambda item : item['model'], reverse=True))
# print(sorted(smartphones, key=lambda item : item['price'], reverse=True))

# 12. More About Functions

# what are doc strings
# how to write docstrings
# how to see docstrings
# what is help function

# def add(a, b):
#     '''this function takes 2 numbers and return their sum'''
#     return a + b

# # print(add(2, 3))

# print(add.__doc__)
# help(add)
