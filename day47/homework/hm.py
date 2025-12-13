# 1) შექმენით სახელებით სავსე სია და ასევე ცარიელი სია: Upper_name = [].  სახელების სიიდან ცარიელ სიაში ჩაამატეთ ყველა ის სახელი რომელიც იწყება დიდი ასოთი, გამოიყენეთ for ციკლი და შესაფერისი სიის და სტრინგის ფუნქციები.

saxelebi = ["Davita", "gela", "Petre", "pavle", "nikolozi", "Luka", "Googa"]

saxelebi2 = []

for i in saxelebi:
    if i[0].isupper():
        saxelebi2.append(i)

print(saxelebi2)

# 2) შექმენით 2 სია - სახელების და გვარების. for ციკლის და ფუნქციების გამოყენებით სახელების სიაში ყველა სახელის ყველა ასო გახადეთ დიდი, ხოლო გვარების სიაში ყველა გვარის თითოეული ასო გახადეთ პატარა, სულ ბოლოს კი გააერთიანეთ სახელების სია გვარის სიასთან და დაპრინტეთ მიღებული შედეგი.

first_names = ["George", "Nick", "Levan", "Mariam"]
last_names = ["Mamladze", "Khutsishvili", "Kvantadze", "Abramishvili"]

for i in range(len(first_names)):
    first_names[i] = first_names[i].upper()
    last_names[i] = last_names[i].lower()

full_names = []
for i in range(len(first_names)):
    full_names.append(first_names[i] + " " + last_names[i])

print(full_names)

# ბატონი ნიკოლოზ წერეთელი — 12/9/2025 9:44 PM
# 3) შექმენით სტრინგებით სავსე სია და ამ სიიდან ამოშალეთ ყველა ის სიტყვა რომელიც არის ან 6-ზე ნაკლები სიგრძეში, ან რომელიც მთავრდება დიდი ასოთი. 

sityvebi = ["hellO", "world", "wonderful", "goodbyE", "precious", "wealthY"]

sityvebi2 = []

for i in sityvebi:
    if len(i) > 6 and not i[-1].isupper():
        sityvebi2.append(i)

print(sityvebi2)

# 4) შექმენით float მონაცემთა ტიპის ელემენტებით სავსე სია რომელშიც იქნება 10 float ელემენტი და ამ სიიდან ახალ ცარიელ სიაში ჩაამატეთ ის რიცხვები რომლებიც არიან 10-ზე მეტი და 100-ზე ნაკლები.

cifr = [10.5414, 12.7141, 50765.3141, 150134.2235, 10.9235, 455425.5, 200124.114241, 67.24143, 23141224.5413, 101424.1]

cifr2 = []

for i in cifr:
    if 10 < i < 100:
        cifr2.append(i)

print(cifr2)

# ბატონი ნიკოლოზ წერეთელი — 12/9/2025 9:56 PM
# 5) შექმენით 2 სია, პირველი სია იყოს სავსე 5 ცალი ქალაქის სახელებით, და მეორე სიაში მოთავსებული იყოს 10 ქვეყნის სახელი. თქვენი დავალებაა რომ ქვეყნის სახელებში ჩაამატოთ ყველა ქალაქის სახელები ცალ-ცალკე მენულე ინდექსიდან მეოთხე ინდექსის ჩათვლით. გამოიყენეთ for ციკლი და შესაბამისი ფუნქციები.

qalaqebi = ["Tbilisi", "erevani", "ar vici", "turketi", "moskovi"]

qveynebi = ["Georgia", "sasomxeti", "azervbaijani", "turqeti", "ruseti", "ukraina",  "poloneti", "germania", "safrangeti", "amerika"]

for i in range(len(qalaqebi)):
    qveynebi[i] = qveynebi[i] + "  " + qalaqebi[i]

print(qveynebi)
