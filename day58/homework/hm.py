# 1) შექმენით რიცხვებით სავსე სია, ამ სიიდან იპოვეთ და დაპრინტეთ მეორე ყველაზე დიდი რიცხვი, გამოიყენეთ for ციკლი.

num = [5, 12, 3, 21, 8, 7]

pir = num[0]
meo = num[1]

if meo > pir:
    pir, meo = meo, pir

for i in num[2:]:
    if i > pir:
        meo = pir
        pir = i
    elif i > meo and i != pir:
        meo = i

print(meo)

# 2) მომხმარებელს შემოატანინეთ წინადადება და დაითვალეთ თუ ამ წინადადებაში რამდენი სიტყვის სიგრძე არის 4-ზე მეტი, დაპრინტეთ ასეთი სიტყვების რაოდენობა, მაგალითად 4. გამოიყენეთ while ციკლი.

winadadeba = input("winadadeba: ")
words = winadadeba.split()

i = 0
count = 0

while i < len(words):
    if len(words[i]) > 4:
        count += 1
    i += 1

print(count)

# 3) მომხმარებელს შემოატანინეთ სიტყვა და გაიგეთ ეს სიტყვა არის თუ არა პალინდრომი - ანუ ეს სიტყვა წინიდანაც და უკნიდანაც თუ ზუსტად იგივენაირად იკითხება. თუ კი მაშინ დაპრინტეთ True, თუ არა დაპრინტეთ False, გამოიყენეთ for ციკლი, არ გამოიყენოთ slicing - [::-1].



# 4) შექმენით არეული რიცხვებით სავსე გრძელი სია და 2 ცარიელი სია, ერთ სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, ხოლო მეორე სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და დგას კენტ ინდექსზე, გამოიყენეთ for ციკლი.




# 5) შექმენით ყველანაირი მონაცემთა ტიპების ელემენტებით სავსე სია, ამოშალეთ ყველა დუპლიკატები - ყველაფერი რაც მეორდება 2-ზე მეტჯერ, გამოიყენეთ remove() ფუნქცია და while ციკლი.

monacemebi = [ "rame", 2, "rame", 3, 1, 4, True, False, True]

i = 0

while i < len(monacemebi):
    if monacemebi.count(monacemebi[i]) > 1:
        sityva = monacemebi[i]
        while sityva in monacemebi:
            monacemebi.remove(sityva)
    else:
        i += 1

print(monacemebi)

# 6)  მომხმარებელს შემოატანინეთ წინადადება და დაპრინტეთ ამ წინადადებაში მყოფი ყველაზე გრძელი სიტყვა, გამოიყენეთ while ციკლი, არ გამოიყენოთ max() ფუნქცია.

winadadeba = input("")

words = winadadeba.split()

longestword = ""
i = 0

while i < len(words):
    if len(words[i]) > len(longestword):
        longestword = words[i]
    i += 1

print(longestword)