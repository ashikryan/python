#____________Function__________

def welcome ():      
    print("Welcome")

welcome() # call it

#use parameters
def greet(name):  # parameter
    print("hello",name)

greet("rahul")  # argument

#_____________________________
def student (name, marks):
    print("your name",name)
    print("your marks",marks)

student("amal",90)

#____return statement________
def add (a,b):
   return a+b     
result = add(10,20)
print(result)

#print()   -> Show value
#return    -> Give value back

def square(number):
    return number*number

print(square(5))

#_________ programs_________
#1
def add (a,b):
    return a+b
print(add(5,3))

#2
def even_or_odd (num):
    if num % 2 ==0:
        return "Even"
    else :
        return "odd"
print(even_or_odd(10))

#3
def student(marks):
    if marks >=50:
        return "pass"
    else :
        return "fail"
print(student(64))

#__ MINI PROJECT __ 
def totalmarks (marks):
    return sum (marks)
def averagemarks (marks):
    return sum(marks) / len(marks)
marks = [80,90,70]

print(totalmarks(marks))
print(averagemarks(marks))

