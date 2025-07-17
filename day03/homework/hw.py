#  1)შექმენი 2 ცვლადი snake_case ის გამოყენებით,მიანიჭეთ ამ ცვლადებს ინტეჯერ ტიპის მონაცემები(რიცხვები),შენი დავალებაა რომ ამ
#ორ ცვლადზე მოახდინო მათემატიკური ოპერაციები(+ - * /) და ეს ოპერაციები შეინახო სხვა ცვლადებში რომლებიც იქნებიან შექმნილები
#ასევე snake_case ის გამოყენებით მაგ
num_one = 15
num_two = 5
sum_of_numbers = num_one + num_two
cifrebis_gamokleba = num_one - num_two
cifrebis_shejameba = num_one * num_two
division_of_numbers = num_one / num_two
print(sum_of_numbers)
print(cifrebis_gamokleba)
print(cifrebis_shejameba)
print(division_of_numbers)


#  2)შექმენი ცვლადი სახელად name რომელსაც მიანიჭებთ მნიშვნელობას თქვენს სახელს,თქვენი დავალებაა რომ ეს ცვლადი განააახლოთ 5 ჯერ
#და დაპრინტოთ ამ ცვლადის საბოლოო მნიშვნელობა
name = "giorgi"
name = "luka"
name = "sandro"
name = "nika"
name = "dato"
print(name) #საბოლოო მნიშვნელობა იქნება "dato"


#  3)შექმენი 5 ცვლადი რომელსაც ერქმევა ერთი სახელი მაგრამ იქნება case sensitive,რაც იმას ნიშნავს რომ ამ ცვლადებში მყოფი ასოები
#იქნება ზოგი დიდი ზოგი პატარა,ანუ ეს 5 ივე ცვლადი იქნება სხვადასხვა ცვლადები,დაპრინტე 5 ივე მათგანი და გამოიტანე პასუხი ტერმინალში
namE = "luiza"
Name = "varlock"
NAME = "gela"
naMe = "zubo"
naME = "davita"
print(name)
print(Name)
print(NAME)
print(naMe)
print(naME)


#  4)გაასოწრეთ შემდეგი ცვლადები და მნიშვნელობები,კომენტარის სახით მიუწერეთ თუ რა არის შეცდომა და შეასწორეთ
# 2name = "giorgi"        ცვლადის სახელი არ შეიძლება ციფრით დაიწყოს
name2 = "giorgi"
# user{name = "bubunauri"  აკრძალულია ფიგურული ფრჩხილების გამოყენება ცვლადის სახელში
user_name = "bubunauri"   
# user_name = goga         სტრინგის მნიშვნელობა უნდა იყოს ბრჭყალებში
user_name = "goga"       
# user-surname = axalaia   დეშის გამოყენება ცვლადის სახელში არ შეიძლება
user_surname = "axalaia"  


#  5)შექმენი 5 ცვლადი რომელიც იქნება snake_case ით დაწერილი,მიანიჭეთ სტრინგ ტიპის მონაცემები,თქვენი დავალებაა რომ გამოიტანოთ ამ
#  5 ცვლადის მნიშვნელობა ერთ გრძელ წინადადებად,კომენტარის სახით მიუწერეთ რა ქვია ამ მოქმედებას როდესაც სტრინგებს ვაერთებთ
first_word = "Python"
second_word = "is"
third_word = "very"
fourth_word = "easy"
fifth_word = "language"
full_sentence = first_word + " " + second_word + " " + third_word + " " + fourth_word + " " + fifth_word
print(full_sentence)
# ეს მოქმედება არის "სტრინგების კონკატენაცია" (concatenation)


#  6)შექმენი 2 ცვლადი,ერთში შეინახე შენი სახელი მეორეშ კი რიცხვი 10,შენი დავალებაა შენი სახელი გამოიტანო ტერმინალში 10 ჯერ
#მოახდინე შესაბამისი ამთემატიკური ოპერაცია
my_name = "davit"
repeat_count = 10
print(my_name * repeat_count)


#  7)კომენტარის სახით ახსენით თუ რომელი მათემატიკური მოქმედებების შესრულება არ შეგვიძლია სტრინგზე და ინტეჯერზე
#და რას მოგვცემს შედეგად
# "hello" + 5         ტიპების შეუთავსებლობა → გამოიტანს შეცდომას: TypeError
# "hello" - 3         არ შეიძლება გამოკლება
# "hello" / 2         არ შეიძლება გაყოფა
# "hello" * 2         შესაძლებელია → "hellohello"

# დასაშვებია მხოლოდ სტრინგის გამრავლება მთელ რიცხვზე (int) ან სტრინგის სტრინგთან დამატება.