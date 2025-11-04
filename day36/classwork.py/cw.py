# 1) შემოაყვანიეთ მომხმარებელს რაღაცა სიტყვა:
# -> შეამოწმეთ არის თუ არა 'a' ან 'A' ამ სიტყვაში/ტექსტში
# -> შეამოწმეთ თუ "არ" არის სიტყვა 'car' ამ სიტყვაში/ტექსტში


word = input("sheiyvane: ")

if 'a' in word or 'A' in word:
    print("aris 'a' an 'A'")
else:
    print("ar ari 'a' და 'A'")

if 'car' not in word:
    print("ar ari 'car'")
else:
    print("aris sityva 'car'")


# 2) მომხმარებელს შემოატანინეთ ტექსტი.
# -> დაუარეთ ამ ტექტის ასოებს for ლუპით
# -> თუ ასო არის 'a' ან 'A' დასკიპეთ, სხვა შემთხვევაში დაპრინტეთ ასო

you = input("text:")

for i in you:
    if i == 'a' or i == 'A':
        continue
    print(i)