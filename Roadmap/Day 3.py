#----------> logical operators <------------#

age = 30
nationality = True

#----------> AND

if age > 40 and nationality == True:
    print("everything fine")
else :
    print("sorry , your not eligible")

#----------> OR

if age > 40 or nationality == True:
    print("everything fine")
else :
    print("sorry , your not eligible")

#---------> NOT

if not nationality :
    print("sorry")
else :
    print("everything fine")
