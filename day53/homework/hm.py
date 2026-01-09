# 2) შექმენით სიტყვებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის g, მაშინ ახალ სიაში ჩაამატეთ სახელი "Goga", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო N-თი, მაშინ სიაში ჩაამატეთ სახელი "Nika", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.

words = ["game", "nika", "Nice", "goga", "HELLO", "leader"]

result = []

for word in words:
    if word.islower() and word.startswith("g"):
        result.append("Goga")
    elif word.isupper() or word.startswith("N"):
        result.append("Nika")
    else:
        result.append("ლიდერი")

print(result)

# 3)  შექმენით რიცხვებით სავსე სია, თუ რიცხვი არის ლუწი ან დგას ლუწ ინდექსზე, ჩაამატეთ მისი კვადრატი ახალ სიაში - გამოიყენეთ შესაბამისი მათემატიკური ოპერატორი, ხოლო თუ რიცხვი არის კენტი ან დგას კენტ ინდექსზე, ახალ სიაში ჩაამატეთ 2-ჯერ დიდი რიცხვი. გამოიყენეთ while ციკლი.

numbers = [1, 2, 3, 4, 5, 6]
new_list = []

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0 or i % 2 == 0:
        new_list.append(numbers[i] ** 2)
    else:
        new_list.append(numbers[i] * 2)
    i += 1

print(new_list)

# 4) შექმენით სიტყვებით სავსე სია, თუ სიტყვის სიგრძე არის 6-ზე მეტი ან მისი ყველა ასო არის დიდი, ამ სიტყვის ყველა ასო გახადეთ პატარა და ჩაამატეთ ახალ სიაში. ყველა სხვა შემთხვევაში ახალ სიაში ჩაამატეთ შეუცვლელი სიტყვა ოღონდ გადაბმულად ორჯერ, მაგალითად თუ მოცემული იქნება სიტყვა "Nika", ჩაამატეთ "NikaNika". გამოიყენეთ while ციკლი.

words = ["HELLO", "Python", "Nika", "PROGRAMMING", "code"]
new_list = []

i = 0
while i < len(words):
    if len(words[i]) > 6 or words[i].isupper():
        new_list.append(words[i].lower())
    else:
        new_list.append(words[i] * 2)
    i += 1

print(new_list)

# 5) მოცემული გაქვთ სტრინგის ცვლადი: numbers = "0123456789", ამ სტრინგიდან ახალ სიაში ჩაამატეთ ყველა ის რიცხვი რომელიც დგას ამ სტრინგის ლუწ ინდექსზე ან არის 7-ზე მეტი, სიაში ეს რიცხვები იყოს როგორც integer ტიპის მონაცემები და არა სტრინგები. დაწერეთ ორივე ხერხით, for ციკლით და while ციკლით.

numbers = "0123456789"
result = []

for i in range(len(numbers)):
    digit = int(numbers[i])
    if i % 2 == 0 or digit > 7:
        result.append(digit)

print(result)


# ----------------------------------------


numbers = "0123456789"
result = []

i = 0
while i < len(numbers):
    digit = int(numbers[i])
    if i % 2 == 0 or digit > 7:
        result.append(digit)
    i += 1

print(result)