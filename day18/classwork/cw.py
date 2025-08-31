num1 = int(input("put first num: "))
num2 = int(input("put sec num: "))
num3 = int(input("put მესამე num: "))

if num1 == num2 and num2 == num3:
    print("3 of them are equal")
elif num1 == num2 and num1 != num3:
    print("1 and 2 are equal")
elif num1 == num3 and num1 != num2:
    print("1 and 3 ar equale")
elif num2 == num3 and num2 != num1:
    print("2 and 3 are equale")
else:
    print("non of them are equale")

# ------------------------------------------------------------------

month = int(input("put number 1-12: "))

if month == 12 or month == 1 or month == 2:
    print("winter")
elif month == 3 or month == 4 or month == 5:
    print("spring")
elif month == 6 or month == 7 or month == 8:
    print("summer")
elif month == 9 or month == 10 or month == 11:
    print("fall")
else:
    print("pleas put number between 1-12")


#---------------------------------------------------------------------

name = input("pleas your name: ")

if name == "admin":
    password = input("pleas input admin pass: ")
    
    if password == "adminpassword123":
        print("hello!!")
    else:
        print("you dont have access")
else:
    print("hello user!!")