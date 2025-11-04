# 1) მომხმარებელს შემოატანინეთ სიტყვა.  
# -> იტერაციით გაიარეთ თითო ასო  
# -> თუ შეხვდებით ასო 'e'-ს ან 'E'-ს გაჩერდით (break)  
# -> დაბეჭდეთ მხოლოდ ის ასოები, რაც მანამდე იყო  

idk = input("put word: ")

for i in idk:
    if i == 'e' or i == 'E':
        break
    print(i)




# 2) მომხმარებელს შემოატანინეთ წინადადება.  
# -> შეამოწმეთ არის თუ არა ტექსტში სიტყვა 'bad'  
# -> თუ არის, დაპრინტეთ "აკრძალული სიტყვა!"  
# -> თუ არაა, დაპრინტეთ "ყველაფერი რიგზეა"  

es_mitumetes = input("sheiyvane rame: ")

if "bad" in es_mitumetes:
    print("აკრძალული სიტყვა!")
else:
    print("ყველაფერი რიგზეა")


# 3) მომხმარებელს შემოატანინეთ წინადადება.  
# -> დაუარეთ ტექსტს for ციკლით  
# -> გამოტოვეთ ყველა space => ' '
# -> დაბეჭდეთ ყველა დანარჩენი სიმბოლო  

LOL = input("sheiyvane randomze: ")

for i in LOL:
    if i == ' ':
        continue
    print(i)


# 4) მომხმარებელს შემოატანინეთ წინადადება.  
# -> დაუარეთ მას for ლუპით  
# -> გამოტოვეთ ხმოვნები (a, e, i, o, u)  
# -> დაბეჭდეთ მხოლოდ თანხმოვნები და თავისთავათ ყველა სხვა სიმბოლო 

sentence = input("kide ertxel: ")

for i in sentence:
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        continue
    print(i)


# 5) მომხმარებელს შემოაყვანით ორი რიცხვი
# --> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით პირველი რიცხვი ამ შუალედში რომელიც იყოფა 15-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)

pirveli = int(input("axla ricxvi: "))
meore = int(input("kide ertxel: "))

for i in range(pirveli,meore + 1):
    if i % 15 == 0:
        print(i)
        break


# 6) შექმენით უსასრულო while loop:
# --> სანამ მომხმარებელი არ შემოიყვანს 'python is best', მანამდე დაპრინტეთ 'you should learn python'

while True:
    iseve = input("chawere eame pitonze: ")
    if iseve == "python is best":
        break
    print("you should learn python")

# 7) \<.BOSS.>/ 
# მომხმარებელს შემოაყვანით ორი რიცხვი
# --> დაუარეთ ყველა რიცვს ამ დიაპაზონში
# --> დაბეჭდეთ მხოლოდ რიგით მესამე რიცხვი ამ შუალედში რომელიც იყოფა 3-ზე(შეწყვიტეთ ციკლი თუ არის ეგეთი)

pirveli = int(input("tame dabali ricxvi: "))
meore= int(input("ricxvi minda rame magali: "))

count = 0

for i in range(pirveli,meore + 1):
    if i % 3 == 0:
        count += 1
        if count == 3:
            print(i)
            break