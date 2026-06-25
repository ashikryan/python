# tuple vs Lust

student = ("rahul", "amal")  #Tuple
names = ["rahul","amal"]   #List

#____________name[0] = "john"        # list allowed 
#____________student[0] = "john"     # Tuple not allowed

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#Dictionary______________________

members = {
    "name":"Ryan",
    "years": '5',
    "marks":'50'
}

#_____________________________Access Value:

print(members["name"])
print(members["years"])
print(members["marks"])

#_____________________________Update & Add New Value

members["marks"] = 60
members ["city"] = "Goa"


#-------------------- loop through -----------------
for x in members:    # keys
    print(x)

for x in members:    #values
    print(members[x])

#---------------------------------------------------
values = [1,2,3,4,4,5,5,5,5,5,4,4,3,3,4,4]
unique = set (values)    

print(unique)   

#___________MINI PROJECT________________#
#---------------------------------------#
employee = {
    "role"  : input("Enter your job role:"),
    "salary": int(input("Enter your salary")),
    "mobile": int(input("Enter your obile number"))
}

print(employee)
#_________________________________________