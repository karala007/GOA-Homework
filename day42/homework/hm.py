# 1) შექმენი სია ხილებზე და დაამატე მასში კიდევ 2 ხილი extend() ფუნქციით.

xili = ["greifruti", "kiwi", "banani"]
xili2 = ["man go", "vashli"]
xili.extend(xili2)
print(xili)

# 2) შექმენი სია numbers და დაამატე მასში [40, 50] extend()-ით.

cif = [10, 20, 30]
cif2 = [40, 50]
cif.extend(cif2)
print(cif)

# 3) შექმენი სია names და შეაბრუნე reverse()-ით.

saxelebi = ["gela", "joni", "luka", "davita"]
saxelebi.reverse()
print(saxelebi)

# 4) შექმენი სია სახელად nums და დათვალე რამდენი ცალი 5 არის მასში count()-ით.

nums = [5,
5,
5,
5,
5,
112,
5,
5,
6,
5,
5,
3,
2,
5,
5,
5,
5,
5,
5,
5,]
datvla = nums.count(5)
print(datvla)

# 5) შექმენი letters = ["a","b","a","c"] და დაბეჭდე რამდენი ცალი "a" არის ჩვენს სიაში.

letters = ["a","b","a","c"]
datvla = letters.count("a")
print(datvla)

# 6) შექმენი სია სახელად names და იპოვე "saba"-ს ინდექსი index()-ით.

names = ["gela", "saba", "nikolozi", "davita", "lukito"]
vipovot_saba = names.index("saba")
print(vipovot_saba)

# 7) შექმენი list = ["red","green","blue"] და იპოვე რომელ ინდექსზე დგას "blue". გამოიყენე შესაბამისი ფუნქცია.

colors = ["red", "green", "blue"]
vipovot_blue = colors.index("blue")
print(vipovot_blue)

# 8) შექმენი სია სახელად nums და დამატე მასში extend()-ით [7, 8, 9].

nums = [1, 2, 3, 4, 5, 6]
num = [7, 8, 9]
nums.extend(num)
print(nums)

# 9) შექმენი სია სახელად foods და დააბრუნე შებრუნებული სია.

sawmelebi = ["xawapuri", "xinkali", "chaqafuli", "qababi", "xashi"]
sawmelebi.reverse()
print(sawmelebi)

# 10) შექმენი სია cities და იპოვე რომელ ინდექსზე დგას "tbilisi".

qalaqebi = ["batumi", "tbilisi", "qutaisi", "ureki", "qobuleti"]
tbilisi = qalaqebi.index("tbilisi")
print(tbilisi)

# 11) შექმენი animals = ["cat","dog","cat","cow"] და დაითვალე ამ სიაში რამდენი "cat" არის.

animals = ["cat", "dog", "cat", "cow"]
kata = animals.count("cat")
print(kata)

# 12)შექმენი სია fruits = ["apple", "banana"] და append ფუნქციით დაამატე "grape". დაბეჭდე სია.

fruits = ["apple", "banana"]
fruits.append("grape")
print(fruits)

# 13)შექმენი სია numbers = [1, 2, 3] და extend()-ით დაუმატე [4, 5]. დაბეჭდე სია.

numbers = [1, 2, 3]
numbers2 = [4, 5]
numbers.extend(numbers2)
print(numbers)

# 14)შექმენი სია names = ["goga", "saba"] და insert()-ით ჩასვი "luka" პირველ ინდექსზე. დაბეჭდე სია.

names = ["goga", "saba"]
names.insert(1, "luka")
print(names)

# 15)შექმენი სია items = ["pen", "pencil", "eraser"] და pop()-ით წაშალე ბოლო ელემენტი; დაბეჭდე განახლებული სია.

items = ["pen", "pencil", "eraser"]
items.pop()
print(items)

# 16)შექმენი სია colors = ["red", "green", "blue"] და remove()-ით წაშალე "green". დაბეჭდე შედეგი.

colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)

# 17)შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", შემდეგ დაბეჭდე სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.

foods = ["bread", "milk"]
if len(foods) >= 2:
    foods.append("cheese")
else:
    foods.append("meat")
print(foods)

# 18)შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი. თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.

nums = [10, 20, 30]
random = int(input("chawere rame ricxvi: "))
if random in nums:
    print("ari ukve sheni ricxvisiashi")
else:
    nums.append(40)
    print(nums)

# 19)შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, შემდეგ insert()-ით ჩასვი ის სიის შუაში (ცენტრალურ ინდექსზე). დაბეჭდე სია.

letters = ["a", "b", "c"]
momx = input("chasvi nebismieri aso:")
letters.insert(1,momx)
print(letters)

# 20)შექმენი სია values = [1, 2, 3, 4]. მომხმარებელს შემოატანინე ინდექსი. თუ ინდექსი სიის ფარგლებშია, pop()-ით ამოშალე შესაბამისი ელემენტი; თუ არა, დაბეჭდე "Index out of range". ბოლოს დაბეჭდე სია.

values = [1, 2, 3, 4]
momx2 = int(input("chawere cifri: "))
if 0 <= momx2 < len(values):
    values.pop(momx2)
else:
    print("Index out of range")
print(values)

# 21)შექმენი სია pets = ["cat", "dog", "hamster"].  მომხმარებელს შემოატანინე შინაური ცხოველის სახელი. თუ იგი არის სიის შიგნით, remove()-ით ამოშალე და დაბეჭდე "Removed", თუ არა — დაბეჭდე "Not found" და სია უცვლელი დატოვე; საბოლოოდ დაბეჭდე სია.

pets = ["cat", "dog", "hamster"]
ar_vici = input("shinauri cxoveli: ")
if ar_vici in pets:
    pets.remove(ar_vici)
    print("Removed")
else:
    print("Not found")
print(pets)

# 22)შექმენი სია a = [5, 5, 7]. მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი არის სიის ელემენტი, დაბეჭდე რამდენჯერ არის სიაში - count() ფუნქციის გამოყენებით. სხვა შემთხვევაში append()-ით ჩასვი ის სიაში და დაბეჭდე სია.

a = [5, 5, 7]
shemoiyvane = int(input("shemoiyvane ricxvi:"))

if shemoiyvane in a:
    rame = a.count(shemoiyvane)
    print(rame)
else:
    a.append(shemoiyvane)
    print(a)

# 23)შექმენი სია queue = ["first", "second"].  მომხმარებელს შემოატანინე ახალი ელემენტი და insert()-ით ჩასვი სიის დასაწყისში. შემდეგ if-ით შეამოწმე სიის სიგრძე — თუ უფრო დიდია 5-ზე, pop()-ით ამოშალე ბოლო ელემენტი; ბოლოს დაბეჭდე სია, თუ არ არის 5-ზე მეტი დაბეჭდე შებრუნებული სია.

queue = ["first", "second"]
rigi = input("rame shemoiyvane:")
queue.insert(rigi)

if len(queue) > 5:
    queue.pop()
    print(queue)
else:
    queue.reverse()
    print(queue)

# 24)შექმენი სია nums = [2, 4, 6].  მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი დადებულია, append()-ით დაამატე; თუ 0-ია ან ნაკლებია ნულზე, დაბეჭდე "Only positive allowed". ბოლოს დაბეჭდე სია.

nums = [2, 4, 6]
num = int(input("ricxvi mome:"))

if num > 0:
    nums.append(num)
else:
    print("Only positive allowed")
print(nums)

# 25) შექმენი სია mix = ["x", "y", "z"]. extend()-ით დაუმატე [1, 2, 3]. შემდეგ მომხმარებელს შემოატანინე ასო; თუ ეს ასო არის სიაში, remove()-ით წაშალე პირველად როცა შეგხვდება და დაბეჭდე "Removed", თუ არა — დაბეჭდე "No such element". ბოლოს დაბეჭდე სია.

mix = ["x", "y", "z"]
levana= ["1", "2", "3"]
mix.extend(levana)
arr=input("idk anymore:")

if arr in mix:
    mix.remove(arr)
    print("Removed")
else:
    print("No such element")
print(mix)