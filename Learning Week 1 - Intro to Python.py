# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:59:35 2018

@author: rasikka
"""

"""BASICS"""

print("Hello world!")

if 5 > 2:
    print("5 is greater than 2")

#Comment
print("Hello world!")


"""multi-line
comments"""
print("Hello world!")



"""VARIABLES"""
x = "Hello"
y = 5
print(x)
print(y)

x = 4
print(x)
x = "hi"
print(x)



"""NUMBERS"""
test_var = 5.38
print(type(test_var))



"""STRINGS"""
a = " How are you? "
print(a.strip())
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("o", "l"))



"""LISTS"""
example_list = ["apple", "banana", "orange"]

example_list[1] = "grapes" 
print(example_list)

example_list.append("watermelon")
print(example_list)

example_list.remove("apple")
print(example_list)

print(len(example_list))



"""DICTIONARIES""" 
example_dict = {"key":"value"}
example_dict = {"apple":"red", "banana":"yellow", "cherry":"red"}



""" IF STATEMENT"""
a = 5
b = 230

The following code will result in an error: 
if b > a :
print("B is greater than A")


The following code will work as intended: 
if b > a :
    print("B is greater than A")


"""ELIF and ELSE"""
a = 5
b = 230

if b > a :
    print(“b is greater than a")
elif a == b:
    print(“a and b are equal”)
else:
    print(“a is greater than b”)


"""EXERCISE""""
#Scenario 1 
location = "Ottawa" 
pay = 50000 

#Scenario 2
location = "Mississauga" 
pay = 50000 

#Scenario 3
location = "California" 	
pay = 50000 

#Scenario 4
location = "Vancouver" 	
pay = 1

#Scenario 5 
location = "California" 	
pay = 25000 


if location == "Vancouver":
    print("So long, suckers! I’ll take it!")
elif location == "Ottawa":
    if pay < 100000:
        print("No way")
    else:
        print("I’ll take it!")
elif location == "California" and pay > 40000:
   print("I’ll take it!")
elif pay > 60000:
    print("I’ll take it!")
else:
    print("No thanks, I can find something better.")


"""WHILE LOOP"""
#Print ‘i’ as long as ‘i’ is less than 8:
i = 0
while i < 8: 
    i+=1
    print(i)

#To exit the loop when i = 5: 
i = 0
while i < 8: 
    i+=1
    print(i)
    if i == 5: 
        break
    
    
    
"""FOR LOOP"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)


#To exit the loop when the list value is “banana”: 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break 
    print(x)
    
    
#To not print the list value of “banana”: 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue 
    print(x)
    
    
"""LOOPS EXERCISES"""

#Exercise 1: 
num = 10 
while num > 3: 
    num = num - 1
    print(num) 


#Exercise 2: 
num = 10
while True:
    num -= 1
    if num < 7:
        break
    print(num)


#Exercise 3: 
count = 0
for letter in "Snow!":
    count += 1
    print("Letter #", count, "is", letter)


"""FUNCTIONS"""

def my_function():
    print("Hello")
my_function()


def my_function(country):
    print("I live in: " + country)
my_function("Canada") 
my_function("USA")
my_function("Norway")


def my_function(x):
    return 5 * x 
print(my_function(-4))
print(my_function(7))
print(my_function(6))



"""LIBRARIES"""
import pandas
import xlrd
import numpy


