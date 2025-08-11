#  1) Conditional statement  არის კოდის ბლოკი რომელიც შესრულდება მხოლოდ იმ შემთხვევაში თუ მოცემული პირობა  ჭეშმარიტია 
#    მათი ვალდებულებაა  გადაწყვეტილება მიიღოს სხვადასხვა სიტუაციებში და განსაზღვროს რომელი კოდის ნაწილი უნდა შესრულდეს.

#  2) for ციკლის მეშვეობით გამოიტანეთ "hello world" 50-ჯერ.

text = 'hello world'

for i in range (50):
    print(str(i) + text)

#  3) while ციკლის მეშვეობით გამოიტანეთ რიცხვები 3-დან 17-ის ჩათვლით.

num = 3

while num < 18:
    print(num)
    num = num + 1

#  4) მომხმარებელს შემოატანინეთ პაროლი, შემდეგ კი შედეგი შეინახეთ ცვლადში. შექმენით პირობა თუ ის უდრის "1234"-ს დაბეჭდეთ
#    "Password is correct", სხვა შემთხვევაში დაბეჭდეთ "Password is incorrect".

password = int(input("password:"))

if password == 1234:
    print('Password is correct')
else:
    print('Password is incorrect')

#  5) შექმენით ცვლადი სადაც შეინახავთ მომხმარებლის მიერ შემოყვანილი ცხოველის სახეობას. თუ სახეობა უდრის "ძაღლი" დაბეჭდეთ "woaf! woaf!", 
#     სხვა შემთხვევაში "შენ არ გყავს ძაღლი"


animal = input('animal breed:')

if animal == 'dog':
    print("woaf! woaf!")
else:
    print('you dont have a dog')


