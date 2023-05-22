# print("M USMAN")
# print('----')
# print('1'*10)


# first task

# name="John Smith"
# age=20
# is_new=True
# print(name,age,is_new)
# name=input("enter name :")
# print(name,age,is_new)

# 2nd task
#
# name=input('Please enter your name :')
# favColor=input('Please enter your favourite color :')
# print(name,"likes",favColor)

# 3 type convrsion
# weight_in_pounds=input('Enter weight in p0unds :')
# print(type(weight_in_pounds))
# weight_in_kilograms=int(weight_in_pounds)*0.45
# print(type(weight_in_kilograms))
# print('weight :',weight_in_kilograms)
# 45% or 0.45 of weight in pounds is weight in kilogram
#
# weight_in_kilograms=input('Enter weight in kilograms :')
# print(type(weight_in_kilograms))
# weight_in_pounds=int(weight_in_kilograms)/0.45
# print(type(weight_in_pounds))
# print('weight :',weight_in_pounds)


# 4 strings
# print("Usman's First Task of Programming")
# print('Usman First Task of "Programming"')
# print('''
#      This is my first task
#      i am trying to learn "Python"
#      Alhumdulilah I'm a Muslim
#      i will be successed one day
# ''')
# first_day='Enjoying Python'
# print(first_day[0])
# print(first_day[-2])
# # starting text at zero index " : "  ending index of string
# print(first_day[0:15])
# print(first_day[:15])
# print(first_day[9:])
# print(first_day[:])
# print(first_day[9:13])
# #1 and -1 case first and last etter exlcluded
# print(first_day[1:-1])
# print(first_day[9:-1])
# print(first_day[9:-2])

# test='''
#      This is my first task
#      i am trying to learn "Python"
#      Alhumdulilah I'm a Muslim
#      i will be successed one day
# '''
# print(test[1:-1])


# formatted strings

# first='usman'
# last='hafeez'
# messsage=first+' ['+last+'] is a Muslim'
# msg=f'''{first} [{last}] is a muslim'''
# print(messsage+'\n'+msg)


# string methods

# usman ='''Usman's first task and Usman is a "Muslim"'''
# print(len(usman))
# print(usman[-7:-1])
# print(usman)
# print(usman.upper())
# print(usman.lower())
# print(usman.capitalize())
# print(usman.find('U'))
# print(usman.find('u'))
# print(usman.replace('Usman','Programmer'))
# print('Usman' in usman)
# print('usman' in usman)


# Arithmethic operations
#
# print(10+3) #sum
# print(10-3) #substraction
# print(10*3) #multiply
# print(10/3) #divide float
# print(10//3) #divide interger
# print(10%3) #modulus
# print(10**3) #power
# assignment operators += -= *= /= %=


# operator precedence
# x=10*(10-5)%5+2**2-4
# print(x)

# #math functions
# import math
# n=49.87
# print(round(n)) #round off
# m=-49
# print(abs(m)) #absolute positive value
# print(math.ceil(n))
# print(math.floor(n))
#
# # python 3 math module google it


# if statements
# is_hot=False
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# # elif not is_hot:
# else:
#     print("It's a cold day")
#     print("wear warm clothes")
# print("Enjoy your's day")

# task
#
# credit=1000000
# is_good=True
# if is_good:
#     down_payment=credit*0.1
#     credit-=down_payment
# else:
#     down_payment = credit * 0.2
#     credit -= down_payment
# # print("Down payment :",down_payment)
# # print("Payable amount :",credit)
# print(f'Down payment: ${down_payment}')

# 1:07:01
#
# has_high_income = True
# has_good_credit = False
# if has_high_income and not has_good_credit:
#     print('Eligible for loan')
# else:
#     print('Not eligible for loan')
# and & , | or, ! not


# camparison operators

# temperature = 25
#
# if temperature > 30:
#     print('''it's a hot day''')
# else:
#     print('''it's a cold day''')
#
# name = input("enter name :")
# if len(name) < 3:
#     print("Long name must be at least 3 characters")
# elif len(name) > 50:
#     print('name can be maximum of 50 characters')
# else:
#     print('name looks good!')


# project: weight convertor

# weight = int(input("Weight: "))
# standard = input("(L)bs or (K)g: ")
# if standard.__eq__("l") | standard.__eq__("L"):
#     print(f"you are {weight*100/45} pounds")
# elif standard.__eq__("K") | standard.__eq__("k"):
#     print(f"you are {weight*100/45} pounds")
#
# weight = int(input("Weight: "))
# standard = input("(L)bs or (K)g: ")
# if standard.upper() == "L":
#     print(f"you are {weight*0.45} kilos")
# elif standard.upper() == "K":
#     print(f"you are {weight/0.45} pounds")


# while loops

# i = 0
# while i < 5:
#     print(i)
#     i += 1
# print("Done")
#
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("Done")

# secret_num = 9
# guess_count = 1
# guess_limit = 3
# while guess_count <= guess_limit:
#     guess = int(input(f"Guess {guess_count}: "))
#     if guess == secret_num:
#         print("You won!")
#         break
#     guess_count += 1
# else:
#     print("Sorry you failed to guess")
# print("Done")


# Car Game
# help = input('type help...\n>')
# if help.upper() == "HELP":
#     print('''start - to start the car
# stop - to stop the car
# quit - to to exit \n''')
# else:
#     exit("Irrelevant code... you have to type 'help'")
# while True:
#     command=input(">")
#     if command.upper() == "START" :
#         print("Car started...Ready to go!")
#     elif command.upper() == "STOP" :
#         print("Car stopped.")
#     elif command.upper() == "QUIT" :
#         break
#     else:
#         print("I don't understand that...")

# help = input('type help...\n>')
# while True:
#     if help.upper() == "HELP":
#         print('''start - to start the car
# stop - to stop the car
# quit - to to exit \n''')
#         break
#     else:
#         print("Irrelevant code... you have to type 'help'")
#         help = input('type help...\n>')
# command = input(">")
# while command.upper() != "QUIT":
#     if command.upper() == "START":
#         print("Car started...Ready to go!")
#     elif command.upper() == "STOP":
#         print("Car stopped.")
#     else:
#         print("I don't understand that...")
#     command = input(">")


# command = ""
# while True:
#     command = input("> ").lower()
#
#     if command == "help":
#         print('''
#         start - to start the car
#         stop - to stop the car
#         quit - to to exit
#         ''')
#     elif command == "start":
#         print("Car started...Ready to go!")
#     elif command == "stop":
#         print("Car stopped.")
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that...")

# command = ""
# temp = ""
# while True:
#     command = input("> ").lower()
#
#     if command == "help":
#         print('''
#         start - to start the car
#         stop - to stop the car
#         quit - to to exit
#         ''')
#     elif command == "start":
#         if temp == command:
#             print("Car is already started!")
#         else:
#             print("Car started...Ready to go!")
#             temp = command
#     elif command == "stop":
#         if temp == command:
#             print("Car is already started!")
#         else:
#             print("Car stopped.")
#             temp = command
#     elif command == "quit":
#         break
#     else:
#         print("Sorry, I don't understand that...")

# for loop
# print('string')
# p = "Python"
# for i in p:
#     print(i)

# print('list\n')
# liststr = ['Usman', 'ali', 'hmm']
# listno = [1, 2, 3, 4, 5]
# for i in liststr:
#     print(i)
# for i in listno:
#     print(i)

# range
# for i in range(10):  #0 to range
#     print(i)
# for i in range(5,10): #from 1st no , to last no
#     print(i)
# for i in range(0,10,2): #from 1st no , to last no , skipping numbers by this
#     print(i)

# prices = [10, 20, 30]
# sump = 0
# for price in prices:
#     sump += price
# print("total", sump)


# nested loops

# for x in range(4):
#     for y in range(4):
#         print(f"({x}, {y})")

# for i in range(2):
#     for j in range(5, 0, -3):
#         print('x'*j)

# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     print(i * 'x')

# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     out = ""
#     for j in range(i):
#         out+="x"
#     print(out)


# lists tutorial
# names = ['usman', 'ali', 'izhar', 'muaaz']
# print(names)
# print(names[1])
# print(names[-2])
# print(names[0:-1])
# print(names[1:])
# print(names[:-1])
# print(names[:])
# print()
# names[1]="Ali asghar"
# print(names)

# list = [1, 2, 3, 4, 5, 8, 6, 7]
# largest = list[0]
# for j in list:
#         if largest < j:
#             largest = j
# print("largest ", largest)


# 2D lists
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]
# print(matrix)
# print()
# print(matrix[2])
# print()
# print(matrix[1][2]) # [x][y] (x,y)
# print()
# for row in matrix:
#     for column in row:
#         print(column)
# for row in matrix:
#     print(row)


# list methods
# numbers = [5, 2, 7, 3, 4]
# numbers.append(20)
# print(numbers)
# numbers.insert(0, 14)
# print(numbers)
# numbers.remove(2)
# print(numbers)
# numbers.append(26)
# print(numbers)
# numbers.pop() #rmove last element
# print(numbers)
# print(numbers.index(3))
# print(numbers[3])
# print(numbers.count(3))
# print(3 in numbers)
# numbers.sort()  #assending order
# print(numbers)
# numbers.reverse()   #decending order
# print(numbers)
# numbers2 = numbers.copy()
# numbers.clear()
# print(numbers)
# print(numbers2)

# matrix = [[2,9,3], [3,6,3], [1,2,3]]
# matrix[0].sort()
# matrix.sort()
# print(matrix)

# remove duplicate items
# list = [1, 1, 2, 3, 4, 8, 2, 5, 4, 5, 6]
# print(list)
# for i in list:
#     temp = i
#     count = 0
#     for j in list:
#         if temp == j:
#             count+=1
#             if count>1:
#                 list.remove(j)
# list.sort()
# print(list)
#
# numbers = [1, 1, 2, 3, 4, 8, 2, 5, 4, 5, 6]
# print(numbers)
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)
# numbers = [1, 1, 2, 3, 4, 8, 2, 5, 4, 5, 6]
# print(numbers)
# uniques = numbers
# numbers=[]
# for number in uniques:
#     if number not in numbers:
#         numbers.append(number)
# print(numbers)


# tuples
# numbers =(1,2,3)
# print(numbers)
# print(numbers[0])
# print(numbers.count(2))
# print(numbers.index(2))

# unpacking
# coordinates = [1, 2, 3]
# # coordinates =(1,2,3)
# print(coordinates[0] * coordinates[1] * coordinates[2])
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# print(x * y * z)
# i, j, k = coordinates
# print(i * j * k)


# dictionaries
# should be unique attributes
# customer = {
#     "name": "usman hafeez",
#     "age": 21,
#     "is_verified": True
# }
# print(customer["name"])
# # print(customer["birthdate"]) & customer["Name"] shows error
# print(customer.get("name"))
# print(customer.get("Name")) #none
# print(customer.get("birthdate","Jan 1 19980"))
# customer["name"]="usman"
# print(customer["name"])
# customer["birthdate"]="oct 6 2001"
# print(customer["birthdate"])


# numbers_mapping = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
# }
# phone = input("Phone: ")
# output = ""
# for i in phone:
#     for j in numbers_mapping:
#         if i == j:
#             output+= numbers_mapping.get(j)+" "
# print(output)

# numbers_mapping = {
#     "0": "zero",
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four",
#     "5": "five",
#     "6": "six",
#     "7": "seven",
#     "8": "eight",
#     "9": "nine",
# }
# phone = input("Phone: ")
# output = ""
# for i in phone:
#     output += numbers_mapping.get(i, "!") + " "
# print(output)

# Emoji convertor
# message = input("message:\n>")
# words = message.split(' ')
# print(words)
# emojies ={
#     ":)": "😂",
#     ":(": "😞"
# }
# output = ""
# for word in words:
#     output += emojis.get(word,word) + " "
# print(output)

# 2:32
# functions #def defining a function
# def hi():  # smaller case name
#     print("""hello
#     how are you
#     how urs days are going""")
#
#     # 2 lines extra
#
#
# hi()


# parameters  | position arguments
# def greet_user(first_name, last_name):
#     print(f'hi {first_name} {last_name}')
#     print("itx your first python program")
#
#
# print("start")
# greet_user("usman", 'hafeez')
# print("finished")

# keyword arguments
# def greet_user(first_name, last_name):
#     print(f'hi {first_name} {last_name}')
#     print("itx your first python program")
#
#
# print("start")
# greet_user(last_name='hafeez', first_name='usman')
# greet_user("usman", last_name='hafeez')
# print("finished")

# return statement | functions
# def square(side):
#     return side * side
#
#
# print(square(5))

# reuseable function
# emojies = {
#     ":)": "😊",
#     ":(": "😞",
#     "<3": "♥️",
#     '-_-': '🥺'
# }
# message = input("message:\n>")
# words = message.split(' ')
# # print(words)
# output = ""
# for i in range(1):
#     for word in words:
#         output += emojies.get(word, word) + " "
#     output += '\n'
#     message = input(">")
#     words = message.split(' ')
# print(output)

# def emoji_converter(message):
#     words = message.split(' ')
#     emojies = {
#         ":)": "😊",
#         ":(": "😞",
#         "<3": "♥️",
#         '-_-': '🥺'
#     }
#     output = ""
#     for word in words:
#         output += emojies.get(word, word) + " "
#     return output
#
#
# print(emoji_converter(input("message:\n>")))

#exceptions
# try:
#     age =int(input("age: "))
#     income = 20000
#     risk = income/age
#     print(age)
# except ValueError:
#     print("invalid value")
# except ZeroDivisionError:
#     print("age cant be zero")
# finally:
#     print("we are done")

# comments
# use of #