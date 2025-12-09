# 1) შექმენით რიცხვებით სავსე სია, თქვენი დავალებაა რომ დაპრინტოთ ახალი სია რომელშიც იქნება თქენს პირველ სიაში მყოფი მხოლოდ ლუწი რიცხვები. გამოიყენეთ შესაბამისი სიის ფუნქცია და for ციკლი.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = []

for i in numbers:
    if i % 2 == 0:
        numbers2.append(i)

print(numbers2)

# 2) შექმენით რიცხვებით სავსე სია, თქვენი დავალებაა რომ დაპრინტოთ ახალი სია რომელშიც იქნება მხოლოდ თქენს პირველ სიაში კენტ ინდექსზე მდგომი რიცხვები რომელბიც არიან აუცილებლად კენტი. გამოიყენეთ შესაბამისი სიის ფუნქცია და for ციკლი.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2= []

for i in range(1, len(numbers), 2):
    if numbers[i] % 2 == 0:
        numbers2.append(numbers[i])

print(numbers2)

# 3) შექმენით სახელებით სავსე სია და ამ სიიდან ამოშალეთ ყოველი ის სიტყვა რომელიც იწყება ასო გ-თი და მთავრდება ასო ი-თი, გამოიყენეთ for ციკლი, დაწერეთ ორივე ხერხით, pop() ფუნქციითაც და remove() ფუნქციითაც.

names = ['გიორგი', 'ნარგიზ', 'გოჩა', 'გია', 'ნიკა']

for i in names[:]:
    if i[0] == 'გ' and i[-1] == 'ი':
        names.remove(i)

for i in range(len(names) - 1, -1, -1):
    if names[i][0] == 'გ' and names[i][-1] == 'ი':
        names.pop(i)

print(names)

# 4) შექმენით სტრინგებით სავსე სია, და ამ სიიდის ყველა ის სიტყვა რომლის პირველი ასო არის Uppercase-ში და რომელიც ამავდროულად დგას კენტ ინდექსზე სიაში, გაუხადეთ ასეთ სიტყვებს ყველა ასო პატარა - lowercase, ხოლო ყველა ის სიტყვა რომლის პირველი ასო არის Uppercase-ში და თან ეს სიტყვა დგას ლუწ ინდექსზე სიაში, ამოშალეთ სიიდან. დაპრინტეთ შეცვლილი სია.

words = ['Gela', 'manana', 'Hidroeleqtrosadguri', 'uka', 'dzroxa', 'Mamali']

i = 0

while i < len(words):
    if words[i][0].isupper():
        if i % 2 == 0:
            words.pop(i)
        else: 
            words[i] = words[i].lower()
            i += 1
    else:
        i += 1

print(words)

# 5) შექმენით სიტყვებით სავსე სია, ამ სიიდან ამოშალეთ ყველა სიტყვა რომელიც იწყება Uppercase დიდი ასო G-თი და რომლის ბოლო 2 ასო არის ასევე Uppercase. ხოლო ყველა სიტყვა რომლის თითოეული ასო არის Lowercase-ში, აიყვანეთ Uppercase-ში შესაბამისი სტრინგის ფუნქციის გამოყენებით. დაპრინტეთ მიღებული სია.
words1 = ['GREAT', 'greetings', 'Good', 'god', 'go', 'GONE','HELLO', 'HOUSE', 'GUITAR', 'GREAT', 'GONE', 'GEMS', 'GIRAFFE', 'GALAXY']

i = 0
while i < len(words1):
    if words1[i][0] == 'G' and words1[i][-2:].isupper():
        words1.pop(i)
    else:
        i += 1

for i in range(len(words1)):
    if words1[i].islower():
        words1[i] = words1[i].upper()

print(words1)

# 6) შექმენით 2 სია, პირველ სიაში იყოს int მონაცემთა ტიპის ელემენტები, ხოლო მეორე სია სავსე იყოს string მონაცემთა ტიპის ელემენტებით. For ციკლის საშუალებით, პირველი სიიდან remove() ფუნქციით ამოშალეთ ყოველი ლუწი რიცხვი რომლებიც დგანან კენტ ინდექსზე, ხოლო მეორე სიიდან pop() ფუნქციით ამოშალეთ ყოველი ის სიტყვა რომელიც იწყება დიდი ასოთი და დგას ლუწ ინდექსზე. ბოლოს შეაერთეთ ორივე შეცვლილი სიები ერთმანეთში, გახადეთ საერთო სია და დაპრინტეთ. (კარგად დააკვირდით პირობას და არ იჩქაროთ. წარმატებები! ! !)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

words = ['GREAT', 'greetings', 'Good', 'god', 'go', 'GONE', 'HELLO', 'HOUSE', 'GUITAR', 'GREAT', 'GONE', 'GEMS', 'GIRAFFE', 'GALAXY']

for i in range(1, len(numbers), 2):
    if numbers[i] % 2 == 0:
        numbers.remove(numbers[i])

for i in range(0, len(words), 2):
    if words[i][0].isupper():
        words.pop(i)
print(numbers.extend(words))


