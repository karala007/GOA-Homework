#  1) მომხმარებელს შემოაყვანიეთ რაიმე რიცხვი(მთელი/ათწილადი); შეამოწმეთ ეს რიცხვი - 
# --> თუ დადებითია დაპრინტეთ 'ეს რიცხვი დადებითი რიცხვია'
# --> თუ უარყოფითია დაპრინტეთ 'ეს რიცხვი უარყოფითი რიცხვია'
# --> თუ ნულია დაპრინტეთ 'ეს რიცხვი ნულია'

number = float(input("put any number: "))

if number > 0:
    print("the number is positive")
elif number < 0:
    print("this number is negative")
else:
    print("this number is zero")


#  2) მომხმარებელს შემოაყვანიეთ თავისი ასაკი:
# 0–12 წლის ასაკი --> დაპრინტეთ 'ბავშვი ხარ'
# 13-19 წლის ასაკი --> დაპრინტეთ 'მოზარდი/თინეიჯერი ხარ'
# 20-64 წლის ასაკი --> დაპრინტეთ 'ზრდასრული ხართ'
# 65-120 წლის ასაკი --> დაპრინტეთ 'ხანში შესული ხართ'
# 120 და ზემოთ --> დაპრინტეთ 'გურუ ან ჯადოქარი'
# თუ შემოყვანილი ასაკი უარყოფითია --> დაპრინტეთ 'არასწორი ინფო'

age = int(input("your age: "))

if age < 0:
    print("wrong info")
elif age <= 12:
    print("you are a childe my brother")
elif age <= 19:
    print("you are a teen")
elif age <= 64:
    print("you are a grown up")
elif age <= 120:
    print("you are old my man")
else:
    print("burn the witch")

#  3) დაწერეთ "password guesser" პროგრამა, შექმენით რაიმე ცვლადი და მასში შეინახეთ ის პაროლი რომელსაც ყველგან იყენებთ ;)
# მომხმარებელს მოთხოვეთ გამოიცნოს თქვენი პაროლი
# აღნიშნეთ ცდების რაოდენობა
# გამოიყენეთ while loop, მანამ ატრიალეთ სანამ მომხმარებელი პაროლს არ გამოიცნობს ან დაწერს --> 'nah strong password'
# ბოლოს აჩვენეთ(დაუპრინტეთ) რამდენი ცდა დაჭირდა პაროლის გამოსაცნობად

password = "<Da2006to>!"
guesses = 0
user_guesses = ""

while user_guesses != password and user_guesses != "nah strong password":
    user_guesses = input("guess pasword: ")
    guesses = guesses + 1

if user_guesses == password:
    print("congrats you guessed it", 'in', guesses, "guess")
else:
    print("you gave up", 'in', guesses, "try")

#  4) მომხმარებელს შემოატანიეთ სამი რიცხვი(მთელი/ათწილადი) და ამ სამი რიცხვთაგან დაბეჭდეთ უდიდესი

num1 = float(input("first num: ")) 
num2 = float(input("sec num: "))
num3 = float(input("third num: "))

if num1  >= num2 and num1 >= num3:
    print("bigest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("bigest number is:", num2)
else:
    print("bigest number is:", num3)

#  5) შემოატანიეთ მომხმარებელს რიცხვი 1-დან 7-ჩათვლით
# თუ 1 --> დაპრინტეთ 'ორშაბათი'
# თუ 2 --> დაპრინტეთ 'სამშაბათი'
# თუ 3 --> დაპრინტეთ 'ოთხშაბათი'
# თუ 4 --> დაპრინტეთ 'ხუთშაბათი'
# თუ 5 --> დაპრინტეთ 'პარასკევი' 
# თუ 6 --> დაპრინტეთ 'შაბათი'
# თუ 7 --> დაპრინტეთ 'კვირა' 
# სხვა დანარჩენი --> 'არ ვიცი ეგ რა დღეა'

day = int(input("put number 1-7: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("idk that day")
