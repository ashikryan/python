
student =["arathy","rahul","akash"]
print(student[0])
print(student[-3])  #neg

student.append("amal")                #Add
print(student)
student.remove("arathy")  
student.insert(0,"ryan")
print(student)
print(len(student))

for x in student:
    print(x)


for i in range(len(student)):
    print(student[i])

#-------------------------------------------------------------#
#leetcode example

numbers=[5,10,3,8]
largest = numbers[0]
for x in numbers:
    if x > largest:
        largest = x

print(largest)

#-------------------------------------------------------------#
array=[]

for x in range(5):
    a=(input("enter num"))
    array.append(a)
print(array)

#______________________________________________________________#