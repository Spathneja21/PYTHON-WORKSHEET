# #1
# print("Twinkle,Twinkle, little star.")
# print("How I wonder what you are!")
# print("Up above the world so high,")
# print("Like a diamond in the sky.")
# print("Twinkle,Twinkle, little star.")
# print("How I wonder what you are!")

# #2
# first_name = input("Enter the first name:")
# last_name = input("Enter the last name: ")
# print(last_name,first_name)

# #3
# radius = int(input("Enter the radius : "))
# pi = 3.14
# area = pi*radius*radius
# print(area)

# #4
# color_list = ["red","green","white","black"]
# print(color_list[0])
# print(color_list[3])

# #5
# number = int(input("Enter the number: "))
# ones = number 
# tens = number*10 + ones
# hundreds = number*100 + tens
# add = ones + tens + hundreds
# print(add)

# 6
# x = str(input("Enter the number: ")).split(",")
# print(x)
# x = tuple(x)
# print(x)

# #7
# celsius = float(input("Enetr the temperature in celsius: "))
# fahrenheit = 1.8*celsius + 32
# print(fahrenheit)

# #8
# first , second = int(input("Enter the first number: ")),int(input("Enter the second number: "))
# print (second , first)
# y = second + 1 + first + 1 
# print(y)

# #9
# num = int(input("Enter the number: "))
# if (num%2 == 0) : print("It is an even number.")
# else : print("It is an odd number.")

# #10
# year = int(input("Enter the year: "))
# if (year%4 == 0) : print("It is an leap year.")
# else : print("It is not an leap year.")

# #11 Write a program to find the euclidean distance between two coordinates. 
# x1,y1 = int(input("x1:")), int(input("y1:"))
# x2,y2 = int(input("x2:")), int(input("y2:"))
# distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# print(distance)

# #12 Write a program that take a user input of three angles and will find out whether it can form a triangle or not.
# a1, a2, a3 = float(input("a1:")),float(input("a2:")),float(input("a3:"))
# sum = a1 + a2 + a3
# if (sum == 180) : print("This is a triangle.")
# else : print("This is not a triangle.")

# #13 WAP to find compound interest for given values.
# principle ,rate ,time  = int(input("principle: ")), int(input("rate: ")), int(input("time: "))
# CI = principle*((1+rate)**time)
# print(CI)

# #14 Given a positive integer N, the task is to write a Python program to check if the number is Prime or not in Python.
# N = int(input("Enter the number : "))
# c = 0
# for i in range (2,N): 
#     if(N % i == 0) :  
#         c = c + 1
# if c > 0:
#     print("Not Prime")
# else:
#     print("Prime")

# #15 Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.
# n = int(input("Enter the number: "))
# sum = 0
# for i in range(1,n+1) : 
#     sum = sum + i**2
    
# print(sum)
