# 1) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა, ანუ წერია lowercase-ში, ამ სიტყვის ყველა ასო გახადეთ დიდი.
# თუ სიტყვა შეიცავს თუნდაც ერთ uppercase ასოს, ეს სიტყვა ამოშალეთ სიიდან. ბოლოს დაპრინტეთ მიღებული სია. (არ შექმნათ ახალი სია, იმუშავეთ პირველ სიტყვების სიაში) გამოიყენეთ while ციკლი.

words = ["hello", "World", "good", "pythON", "javascript", "Code"]

i = 0

while i < len(words):
    if words[i].islower():
        words[i] = words[i].upper()
        i += 1
    else:
        words.pop(i)

print(words)


# 2) შექმენით სტრინგის ცვლადი და ცარიელი სია. სტრინგში მყოფი დიდი ასოები გახადეთ პატარა და ამ სიაში ჩაამატეთ, ხოლო სტრინგში მყოფი პატარა ასოები გახადეთ დიდი და ასევე ჩააგდეთ ამ სიაში. დაპრინტეთ საბოლოო სია, გამოიყენეთ while ციკლი.

text = "GaMaRJoBa"
jami = []

i = 0

while i < len(text):
    if text[i].isupper():
        jami.append(text[i].lower())
    else:
        jami.append(text[i].upper())
    i += 1

print(jami)

# 3) შექმენით სახელებით სავსე სია, ასევე შექმენით ცარიელი სია, თუ სიტყვის ყველა ასო არის პატარა, მაშინ ამ სიტყვის ყველა ასო გახადეთ დიდი და შესაბამისი სიის ფუნქციის გამოყენებით ჩასვით ეს სიტყვა ცარიელი სიის დასაწყისში, ხოლო თუ სიტყვის ყველა ასო არის დიდი, მაშინ ამ სიტყვის ყველა ასო გახადეთ პატარა და შესაბამისი სიის ფუნქციის გამოყენებით ჩასვით ეს სიტყვა ცარიელი სიის ბოლოში. ბოლოს დაპრინტეთ მიღებული სია. გამოიყენეთ for ციკლი.

names = ["nika", "GIORGI", "luka", "SABA", "dato", "ANA"]
result = []

for i in names:
    if i.islower():
        result.insert(0, i.upper())
    elif i.isupper():
        result.append(i.lower())

print(result)

# 4) შექმენით ქალაქების სია, წაშალეთ pop() ან remove() ფუნქციით ყველა ის სიტყვა რომლის ყველა ასო არის დიდი, ხოლო ყველა სხვა სიტყვას ყველა ასო გაუხადეთ დიდი. დაპრინტეთ საბოლოო შედეგი. გამოიყენეთ while ციკლი.
# ბატონი ნიკოლოზ წერეთელი — 12/28/2025 5:02 PM

cities = ["TBILISI", "batumi", "kutaisi", "ZUGDIDI", "gori", "rustavi"]

i = 0

while i < len(cities):
    if cities[i] == cities[i].upper():
        cities.pop(i)
    else:
        cities[i] = cities[i].upper()
        i += 1

print(cities)

# 5) შექმენით გვარებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა, მაშინ ეს სიტყვა ამოშალეთ ამ სიიდან და თავიდან ჩაამატეთ იგივე სიაში, ოღონდ ერთი ინდექსით მარჯვნივ, და ყველა ასო ჰქონდეს დიდი. ხოლო თუ სიტყვის ყველა ასო არის დიდი, მაშინ ეს სიტყვა ამოშალეთ ამ სიიდან და თავიდან ჩაამატეთ იგივე სიაში, ოღონდ ერთი ინდექსით მარცხნივ, და ყველა ასო ჰქონდეს პატარა. იმუშავეთ ერთ სიაში, გამოიყენეთ while ციკლი.

names = ["KARALASHVILI", "chalauri", "ABRAMADZE", "MIDELASHVILI", "chyonia"]

i = 0

while i < len(names):
    sityva = names[i]

    if sityva.islower():
        names.pop(i)
        names.insert(i + 1, sityva.upper())
        i += 1

    elif sityva.isupper():
        names.pop(i)
        new_index = i - 1

        if new_index < 0:
            names.insert(0, sityva.lower())
            i += 1
        else:
            names.insert(new_index, sityva.lower())
            i += 1

    else:
        i += 1

print(names)

# 6) შექმენით სტრინგის ცვლადი და ცარიელი სია, თუ სტრინგის ასო არის პატარა, მაშინ ცარიელ სიაში ჩაამატეთ "+" ნიშანი, ხოლო თუ სტრინგის ასო არის დიდი, მაშინ ცარიელ სიაში ჩაამატეთ "-" ნიშანი. თუ მინუსების რაოდენობა სიაში არის ლუწი, მაშინ წაშალე ყველა "+" ნიშანი, ხოლო თუ მინუსების რაოდენობა სიაში არის კენტი, წაშალე ყველა "-" ნიშანი. "+" და "-" -ების თავიდან სიაში ჩასაგდებად გამოიყენეთ for ციკლი, ხოლო "+" ან "-" -ების წასაშლელად გამოიყენეთ while ციკლი.

texti = "HeLloWoRld"
simboloebi = []

for i in texti:
    if i.islower():
        simboloebi.append("+")
    elif i.isupper():
        simboloebi.append("-")

minus_count = simboloebi.count("-")

i = 0
while i < len(simboloebi):
    if minus_count % 2 == 0:
        if simboloebi[i] == "+":
            simboloebi.pop(i)
        else:
            i += 1
    else:
        if simboloebi[i] == "-":
            simboloebi.pop(i)
        else:
            i += 1

print(simboloebi)

# 7) შექმენით წინადადების სტრინგის ცვლადი და ცარიელი სია, ცარიელ სიაში ჩაამატეთ სიტყვები ცალ-ცალკე, არა ასოები, არამედ მთლიანი სიტყვები. ამაზე იჭყლიტეთ ტვინი, წარმატებებს გისურვებთ.

sentence = "Python is very powerful language"
sityvebi = []

carieli= ""

for i in sentence:
    if i == " ":
        sityvebi.append(carieli)
        carieli = ""
        continue

    carieli += i

if carieli:
    sityvebi.append(carieli)

print(sityvebi)

# 8) შექმენით სტრინგის ცვლადი და შემოაბრუნეთ ეს სტრინგი. არ გამოიყენოთ slicing. და ყველა ასო გაუხადეთ დიდი. დაპრინტეთ საბოლოო სტრინგი.

hello = "Hello World"
shebrun= ""
i = 0

while i < len(hello):
    shebrun = hello[i] + shebrun
    i += 1

print(shebrun.upper())
