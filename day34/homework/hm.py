# 1) შექმენით სია სადაც შეინახავთ სხვადასხვა ქალაქების სახელებს.  
#    for loop ით დაბეჭდეთ მხოლოდ ის ქალაქები, რომელთა სახელის სიგრძე მეტია 6-ზე.

qalaqebi = ["tbilisi", "qutaisi", 'poti', 'gurjaani']

for i in qalaqebi:
    if len(i) > 6:
        print(i)

# 2) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად იყოფა 15-ზე.

random_sityvebi = ['lela', 'davita', 'mukbangi', 'wyali', 'hidroeleqtrosadguri', 'armaxsendebadzaliandidisityva', 'iyofa romelime sityva 15-ze ??', 'i love my mom']

for i in random_sityvebi:
    if len(i) % 15 == 0:
        print(i)

# 3) შექმენით სია რიცხვებით.  
# -> გამოიყენეთ for loop რათა დათვალოთ რამდენი რიცხვია სიაში.  
# -> არ გამოიყენოთ len() — დაითვალეთ ხელით.

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

jami = 0

for i in num:
    jami += 1

print(jami)

# 4) შექმენით სია სხვადასხვა სიტყვებით.  
# -> for loop-ით დაბეჭდეთ მხოლოდ ის სიტყვები, რომელთა სიგრძე ზუსტად 5 სიმბოლოა.

random_sityvebi = ['lela', 'davita', 'mukbangi', 'wyali', 'hidroeleqtrosadguri', 'armaxsendebadzaliandidisityva', 'iyofa romelime sityva 15-ze ??', 'i love my mom', 'chava', 'mateb', 'sityv' , 'ebs']

for i in random_sityvebi:
    if len(i) == 5 :
        print(i)

# 5) მომხმარებელს შემოატანინე წინადადება.  
# -> გაიგე რამდენი სიმბოლოა წინადადებაში.  
# -> for ციკლით დათვალე რამდენი აso "a" ან "A" არის ტექსტში.

ravi_aba = ['I was breathing at Atlanta with my electric green cat when Tim Cheese pulled up with John Doe, he told me he was offended by my blue fire monkey that I stole from Antarctica but I was confused since I thought it was a gift to me from my mailbox but my pet rock that tells me very detailed stories about the future shot an elephant in my pajamas']

jami = ravi_aba[0]

datvla_a_si = 0

for i in jami:
    if i == "a" or i == "A":
        datvla_a_si += 1

print(datvla_a_si)

# 6) <= Boss Level =>
# შექმენით სია სადაც შეინახავთ სხვადასხვა სტრინგებს.
# --> დაპრინტეთ ამ სიიდან ყველაზე გრძელი სტრინგი

ravi_aba = ['I', 'was', 'breathing', 'at', 'Atlanta', 'with', 'my','electric', 'green', 'cat', 'when', 'Tim','Cheese', 'pulled', 'up', 'with', 'John', 'Doe', 'he','told', 'me', 'he','was' ,'offended',' by', 'my' ,'blue' ,'fe', 'monkey', 'that', 'I', 'stole' 'from', 'Antarcti'] 

biggest_bird = ravi_aba[0]

for i in ravi_aba:
    if len(i) > len(biggest_bird):
        biggest_bird=i

print(biggest_bird)
