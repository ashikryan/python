#_________Practice_________#
#__________________________#
#1

age = int(input("age"))
name = input("name")
goal = input("goal")

print(age,name,goal)

#2
a=int(input("Enter num"))
b=int(input("Enter num"))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

#3
checknumber = int(input("enter number"))

if checknumber % 2 == 0:
    print("Even")
else :
    print("odd")

#4
studentmark=int(input("mark"))

if studentmark >=50:
    print("pass")
else :
    print("fail")


#SECTION - B
#5

for x in range(1,21):
    print(x)

#6
for x in range(2,51,2):
    print(x)

#or 
for x in range(1,51):
    if x % 2 == 0:
        print(x)

#or while loop        
x = 2
while x<=50:
    print(x)
    x+=2

#7
inputnum=int(input("Enter number"))

for i in range(1,11):
    print(inputnum,"x",i,"=",inputnum*i)

#8
total = 0
for x in range(1,101):
    total+=x
print(total)

#9

name=input("Enter your name")
print(name[0])
print(len(name))
print(name[-1])
#last character idk

#10
example = "Ryan"
print(example[::-1])

#11
password = input("Enter password")

if len(password)>=8:
    print("strong")
else:
    print("weak")
