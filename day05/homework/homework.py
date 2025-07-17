#  1)კომენტარის სახით ახსენი თუ რომელი ოპერატორები ვისწავლეთ და რა დანიშნულება აქვთ მათ
#  ჩვენ ვისწავლეთ == ტოლობა კიდევ ვისწავლეთ < ნაკლებობა და > მეტობა

#  2)მომხმარებელს შემოაყვანინეთ ორი რიცხვი,შეადარეთ თუ პირველი რიცხვი მეტია მეორეზე,ასევე შეადარე თუ პირველი
#  რიცხვი ნაკლებია მეორე რიცხვზე,და ასევე შეადარე თუ პირველი რიცხვი უდრის მეორე რიცხვს

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Is the first number greater than the second?", num1 > num2)
print("Is the first number less than the second?", num1 < num2)
print("Is the first number equal to the second?", num1 == num2)

# 3)მომხმარებელს შემოატანინეთ 5 სტრინგ ტიპის მნიშვნელობა,შენი დავალებაა მოახდინო მათი კონკატინაცია

str1 = str (input("Enter word 1: "))
str2 = str (input("Enter word 2: "))
str3 = str (input("Enter word 3: "))
str4 = str (input("Enter word 4: "))
str5 = str (input("Enter word 5: "))
result = str1 +  str2  +  str3   +  str4  +  str5 
print("Concatenated result:", result)

#  4)მომხმარებელს შემოატანინე 4 რიცხვი,შენი დავალებაა გაიგო ამ რიცხვების საშუალო არითმეტიკული
#  (დღესაც ვისაუბრეთ ამაზე,ვნახოთ როგორ გაათმევთ თავს)

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))
n4 = int(input("Enter number 4: "))
average = (n1 + n2 + n3 + n4) / 4
print("Average is:", average)

# 5)შექმენი 4 ცვლადი,ამ ცვლადებშ შეინახე 4 განსხვავებული მონაცემთა ტიპის ელემენტები და დაპრინტე მათ ტიპი(გამოიყენეთ შესაბამისი ფუნქცია)
  
a = "hello"    
print(type(a)) 
# string

b = 25   
print(type(b))       
# integer

c = 3.14  
print(type(c))      
# float

d = True   
print(type(d))     
# boolean

#  6)შექმენი 2 ცვლადი,შეინახე ორივე ცვლადში სტრინგ ტიპის მნიშვნელობები დაშეადარე ისინი არიან თუ არა ერთნაირები(უდრის თუ არა ერთმანეთს)

str1 = "hello"
str2 = "hello"
print("Are the strings equal?", str1 == str2)  # True or False

#  7)შექმენი 4 ცვლადი,სადაც გექნება მოთავსებული რიცხვები ოღონდ სტრინგის სახით მაგ: "40",გადაიყვანე ეს სტრინგი
#  რიცხვები ინტეჯერში(გამოიყენე შესაბამისი ფუნქცია) და გაიგე ამ ოთხი რიცხვის ჯამი

s1 = "40"
s2 = "10"
s3 = "30"
s4 = "20"

n1 = int(s1)
n2 = int(s2)
n3 = int(s3)
n4 = int(s4)
total = n1 + n2 + n3 + n4
print("The total sum is:", total)

#  8)შექმენი 3 ცვლადი,ამ ცვლადებში შეინახეთ ინტეჯერ ტიპის მონაცემები,შენი დავალებაა ეს რიცხვები გაასტრინგო
#  (გამოიყენე შესაბამისი ფუნქცია) და გამოიტანო ეს რიცხვები ერთ წინადადებაში. მაგ:304050

num1 = 30
num2 = 40
num3 = 50

str1 = str(num1)
str2 = str(num2)
str3 = str(num3)
result = str1 + str2 + str3
print("Final result:", result)


