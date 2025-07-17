# 1)კომენტარების სახით ახსენით რა არის input-ი და output-ი, მოიყავნეთ შესაბამისი მაგალითები.

# input() — გამოიყენება მომხმარებლისგან მონაცემის მისაღებად
# output — არის ის ინფორმაცია, რაც პროგრამა ბეჭდავს ეკრანზე 

# მაგალითა
name = input("your name: ")  #input = მომხმარებელი წერს სახელს

print("hello,", name)  #output = ბეჭდავს ტექსტს და სახელს

# 2)შექმენით ცვლადი, რომელშიც შეინხავთ input ინსტრუქციით შემოტანილ მნიშვნელობას, შემდეგ შეამოწმებთ თუ რა ტიპის მონაცემი
# ინახება ამ ცვლადში და დაპრინტავთ.

user_input = input("something: ")
print("type:", type(user_input))

# 3)თიოთეული მონაცემთა ტიპისთვის (str,int,float), შექმენით 5 ცვლადი და დაუწერეთ კომენტარი თუ რომელ მონაცემთა ტიპს
# ინახავს ცვლადი.

# სტრინგები (str)
name1 = "davita"     # str
name2 = "python"     # str
name3 = "hello"      # str
name4 = "code"       # str
name5 = "data"       # str
# მთელი რიცხვები (int)
age1 = 25            # int
age2 = 18            # int
age3 = 30            # int
age4 = 50            # int
age5 = 12            # int
# ათწილადი რიცხვები (float)
height1 = 1.70       # float
height2 = 2.0        # float
height3 = 0.5        # float
height4 = 3.14       # float
height5 = 9.81       # float


# 4)აიღეთ 3 ცვლადი, შეინახეთ განსხავებული მონაცემთა ტიპები (str,int,float), შემდეგ type ინსტრუქციის გამოყენებით
# შეამოწმეთ, თუ რომელ მონაცემთა ტიპს ინახავს ცვლადი.

my_name = "dato"      # str
my_age = 19           # int
my_weight = 73.5      # float

print(type(my_name))     # <class 'str'>
print(type(my_age))      # <class 'int'>
print(type(my_weight))   # <class 'float'>

# 5)მომხმარებელს შემოატანინეთ ორი სიტყვა, შეინახეთ ისინი ცვლადებში, მოახდინეთ მათი კონკატინაცია და დაბეჭდეთ.

word1 = input("first word: ")
word2 = input("second word: ")

result = word1 + word2
print("sum:", result)

# 6)მომხმარებელს შემოატანინეთ 5 რიცხვი სხვადასხვა დამოუკიდებელი input-ების სახით, თქვენი დავალებაა დაბეჭდოთ მათი საშუალო არითმეტიკული.

num1 = int(input("first number: "))
num2 = int(input("second number: "))
num3 = int(input("third number: "))
num4 = int(input("fourth number: "))
num5 = int(input("Fifth number: "))

average = (num1 + num2 + num3 + num4 + num5) / 5
print("Average arithmetic:", average)
# 7)მომხმარებელს შემოატანინეთ სახელი, გვარი, ასაკი, სიმაღლე, წონა და ამ მონაცემების გამოყენებით დაბეჭდეთ ერთი დიდი წინადადება.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
weight = input("Enter your weight: ")

print("The user is", first_name, last_name + ",", "they are", age, "years old,", "height:", height, "m,", "weight:", weight, "kg.")