#  1) შექმენით ცვლადი სადაც შეინახავთ ინტეჯერ ტიპის მონაცემს,შემდეგ შეამოწმეთ თუ ეს რიცხვი რომელიც ცვლადში გაქვთ შენახული მეტია
#10 ზე დაპრინტეთ "more than 10" სხვა შემთხვებაში დაპრინტეთ "less than 10"

# 1.
number = 9

if number > 10:
    print('more than 10')
else:
    print('less than 10')

# 2.

number_2 = 13

if number_2 > 10:
    print('more than 10')
else:
    print('less tan 10')

# 2) მომხმარებელს შემოაყვანინეთ რიცხვი,შემდეგ შეამოწმეთ თუ ეს რიცხვი უდრის 15 ს დაუპრინტეთ "equal to 15" სხვა შემთხვევაში
#დაუპრინტეთ "not equal to 15"

number_3 = int(input('put any number:'))

if number_3 == 15:
    print("equal to 15")
else:
    print("not equal to 15")

# 3)მომხმარებელს შემოატანეთ სტრინგი შენი დავალებაა შეამოწმო,თუ მომხამრებლის მიერ შემოყვანილი სტრინგი არის giorgi დაუპრინტეთ
#you are correct სხვა შემთხვევაში დაუპრინტეთ "you are wrong"

name = str(input('your name:'))

if name == 'giorgi':
    print('you are correct')
else:
    print('you are wrong')

# 4)დაატრიალეთ ფორ ციკლი 50 დან 100 მდე 5 ის გამოტოვებით

for i in range(50,100,5):
    print(i)

# 5)ფორ ციკლის დახმარებით გამოიტანეთ ტერმინალში თქვენი სახელი და გვარი

my_name = 'davit karalashvili'

for i in range (1):
    print(my_name)

# 6)while loop ის დახმარებით ტერმინალში გამოიტანეთ რიცხვები 20 დან 50 მდე

num = 20

while num < 50:
    print(num)
    num = num + 1

