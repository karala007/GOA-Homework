# 1)მომხმარებელს შემოატანინეთ input-ის მეშვეობით სახელი და თქვენი დავალებაა შეინახოთ იგი ცვლადში და დაპრინტოთ ეს მნიშვნელობა.
user_name = input("your name ")
print("your name:", user_name)

# 2)მომხარებელს შემოატანინეთ 2 ცალი რიცხვი სხვადასხვა დამოუკიდებელი input-ის მეშვეობით, ამის შემდეგ კი უბრალოდ დაბეჭდეთ
#ამ შემოყვანილი რიცხვების ჯამი. (დაგჭირდებათ int() ფუნქცია)
num1 = int(input("put first number: "))
num2 = int(input("put second number: "))
sum_of_numbers = num1 + num2
print("sum of this numbers:", sum_of_numbers)

# 3)მომხმარებელს შემოატანინეთ თავისი ასაკი, თქვენი დავალებაა შემოყვანილი მნიშვნელობა გადაიყვანოთ integer ტიპის
#მონმაცემად და საბოლოოდ დაბეჭდოთ მომხმარებლის მიერ შემოყვანილი მნიშვნელობის მონაცემთა ტიპი.
age = int(input("your age: "))
print("your age:", type(age))

# 4)შექმენით 4 ცვლადი, თითოულ ცვლადში შეინახეთ 1 მონაცემთა ტიპის მნიშვნელობა, თქვენი დავალებაა
#კი საბოლოოდ დაბეჭდოთ ამ ცვლადების მონაცემტა ტიპები.

var_str = "hello" 
print(type(var_str))
# string

var_int = 25
print(type(var_int))
# integer

var_float = 3.14
print(type(var_float))
# float

var_bool = True
print(type(var_bool))
# boolean





