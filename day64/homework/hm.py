# ```
# 1)შექმენი ფუნქცია, რომელსაც აქვს ერთი პარამეტრი —name.
# ფუნქციამ უნდა დააბრუნოს ტექსტი:
# გამარჯობა, [სახელი]!
# ფუნქცია გამოიძახე სხვადასხვა არგუმენტით მინიმუმ 3-ჯერ.

def greet(name):
    return "gamarjoba " + name 

print(greet("davit"))
print(greet("gelaa"))
print(greet("zviangi"))




# 2)შექმენი ფუნქცია, რომელსაც აქვს ორი პარამეტრი — num1 და num2.
# ფუნქციამ უნდა დააბრუნოს მათი ჯამი.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def nomer(num1, num2):
    return num1 + num2

print(nomer(3, 5))
print(nomer(10, 20))
print(nomer(2, 3))
print(nomer(6, 7))
print(nomer(6, 9))

# 3)შექმენი ფუნქცია ერთი პარამეტრით num.

# ფუნქციამ უნდა დააბრუნოს (return) გადაცემული რიცხვის კვადრატი.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def xarisxi(num):
    return num * num

print(xarisxi(2))
print(xarisxi(5))
print(xarisxi(10))

# 4)შექმენი ფუნქცია ერთი პარამეტრით — age.

# თუ ასაკი არის 18 ან მეტი, დააბრუნოს:
# სრულწლოვანი ხარ

# სხვა შემთხვევაში:
# არ ხარ სრულწლოვანი

def age(age):
    if age >= 18:
        return "xar srul wlovani"
    else:
        return "ar xar srulwlovani"

print(age(67))
print(age(69))
print(age(2))
print(age(34))
print(age(6))


# 5)შექმენი ფუნქცია ერთი პარამეტრით — (string).

# ფუნქციამ უნდა დაბეჭდოს ტექსტის სიმბოლოების რაოდენობა.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით


def text_length(text):
    return(len(text))

print(text_length("pitoni"))
print(text_length("gamarjoba"))


print(text_length)



# 6)შექმენი ფუნქცია ორი პარამეტრით num1 და nuk2.

# ფუნქციამ უნდა დააბრუნოს მათი ნამრავლი.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def som(num1,nuk2):
    return num1 * nuk2

print(som(34,35))
print(som(124,421))
print(som(124,532))
print(som(42,12))

# 7)შექმენი ფუნქცია ერთი პარამეტრით — score.

# თუ ქულა ≥ 90 → დააბრუნოს "შესანიშნავი ქულა"

# თუ ქულა >= 70 და ნაკლებია ან <=89 → დააბრუნოს "კარგი ქულა"

# თუ ქულა >= 50 და <= 69 → დააბრუნოს "დამაკმაყოფილებელი ქულა"

# სხვა შემთხვევაში დააბრუნოს "ჩაჭრილი"

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def qula(score):
    if score >= 90:
        return "mshvenieri qulaa"
    elif score >= 70 and score <= 89:
        return "meti shegedzlo"
    elif score >= 50 and score <= 69:
        return "ari ra"
    else:
        return "chaiweri"

print(qula(95))
print(qula(75))
print(qula(60))
print(qula(40))

# 8)შექმენი ფუნქცია ერთი პარამეტრით — number.

# ფუნქციამ უნდა დააბრუნოს, ლუწია თუ კენტი.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def arr(number):
    if number % 2 == 0:
        return "luwia"
    else:
        return "kentia"

print(arr(4))
print(arr(7))
print(arr(10))

# 9)შექმენი ფუნქცია ერთი პარამეტრით — name

# ფუნქციამ უნდა დააბრუნოს მხოლოდ პირველი ასო.

# მაგალითად:
# „Giorgi“ → G

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def aso(name):
    return name[0]

print(aso("davita"))
print(aso("maikli"))
print(aso("giorgi"))

# 10)შექმენი ფუნქცია სამი num1 num2 num3.

# ფუნქციამ უნდა დააბრუნოს ამ სამი რიცხვის საშუალო არითმეტიკული.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def sash(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print(sash(3, 6, 9))
print(sash(10, 20, 30))
print(sash(5, 7, 9))

# ```
# 11)შექმენი ფუნქცია ერთი პარამეტრით —password.

# თუ პაროლი უდრის "python123" → დააბრუნოს  "წვდომა დაშვებულია"

# სხვა შემთხვევაში → "არასწორი პაროლი"

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def passw(password):
    if password == "python123":
        return "sworiaa"
    else:
       return "arariswori"

print(passw("python321"))
print(passw("00123"))
print(passw("Davita"))
print(passw("python123"))

# 12)შექმენი ფუნქცია ერთი პარამეტრით — text.

# ფუნქციამ უნდა დააბრუნოს ეს ტექსტი მთლიანად დიდი ასოებით.

# გამოიძახე ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტებით

def upp(text):
    return text.upper()

print(upp("gelaaa"))
print(upp("me miyvars deda"))
print(upp("miama"))