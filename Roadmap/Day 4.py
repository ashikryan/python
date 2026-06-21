#---------------------------------   >>  Loops  <<   ------------------------------------------#

#----> for loop

i = 20 

for x in range (i):     # which loop mentioned 
    print("hello")
    print("let's go")


#----> range function

for p in range (0,10):
    print("new words",p+1)


#----> step size

for i in range (0,9,5):
    print(i)



#----> While loop

count = 0
while count <=5:
    print("hello everything done")
    count = count + 1



#---->>>>>>>> multiplication <<<<<<-------

num =int (input("enter num:"))  # input 

for i in range(1,11):
    print(num, "x",i,"=",num*i)

#---->>>>> sum of number <<<<<<<<<------

total = 0

for i in range(1,6):
    total += i
    print(total)






