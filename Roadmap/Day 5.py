#---------------------------> String <------------------------#

name = "Ryan"
city = "kochi"
goal = "Backend Engineer"

print(f"name :{name}\ncity : {city}\ngoal: {goal}")


#----------------------------> String index <-----------------#

nickname = "RYAN"

print(nickname[1])  
print(nickname[0])
print(nickname[-1])             #------> Negative index (---->> N A Y R )

print(nickname[0:2])            #------> string slicing (0 - 2)
print(nickname[:2])             #___________shortcut method__________>> string[Start : End]

print(nickname[0::])            #>>> postive full
print(nickname[::1])            #>>> Negative full

#------------------------------------------------------------------------#
#---->>> Useful String Methods

word="case"
print(word.upper())
print(word.lower())
print(len(word))

print(word.replace("case","lesson"))  # temp value change still "case"
print(word)
print(word.count("s"))
#------------------------------------->>[solution]
word=(word.replace("case","lesson"))
print(word)
print(word.count("s"))

#-----------------------------------------------------------------------#
eat="cake"
for x in eat:
    print(x)

#----------------- programs ---------------------#
#------------------------------------------------#

data =input("Enter your name")
print(len(data))
print(data.lower())
print(data.upper())
print(data.replace(data,"changed"))  # temp
data=(data.replace(data,"Ryan lesson completed"))   #perm
print (data)
print(data[::-1]) # neg
print(data[0::])  # pos
#_______________________________________________________________

#______________Password Strength Checker________________________

password = input("enter your password")

if len(password) >=12:
    print("Strong Passsword")
elif len(password) >=8:
    print("Average Password")
else :
    print("Weak Password")

#_______________________________________________________________