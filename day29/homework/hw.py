# 1)მოცემულია სტრინგი "PythonProgramming".
# ამოიღე პირველი 6 სიმბოლო და დაბეჭდე გამოიყენეთ slicing

idk = "PythonProgramming"

pirveli_6simbolo = idk[:6]

print(pirveli_6simbolo)


# 2)მოცემულია სია numbers = [10, 20, 30, 40, 50, 60, 70].
# ამოიღე მხოლოდ შუა 3 ელემენტი და დაბეჭდე გამოიყენეთ slicing (მინუს ინდექსებითაც)

num = [10, 20, 30, 40, 50, 60, 70]

dadebiti = num[2:5]
print(dadebiti)

uaryofiti = num[-5:-2]
print(uaryofiti)


# 3)მოცემულია სტრინგი "HelloWorld".
# დაბეჭდეთ Hello ტერმინალში slicing ის გამოყენებით (მინუს ინდექსებითაც)

arc_es_ar_vici = "HelloWorld"

dadebiti = arc_es_ar_vici[:5]
print(dadebiti)

uaryofiti = arc_es_ar_vici[:-5]
print(uaryofiti)


# 3)მოცემულია სია letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'].
# დაბეჭდე ყოველ პირველი მესამე მეხუთე ელემენტები გამოიყენეთ indexing (მინუს ინდექსებითაც)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

dadebiti = [letters[0], letters[2], letters[4]]
print(dadebiti)

uaryofiti = [letters[-7], letters[-5], letters[-3]]
print(uaryofiti)


# 4)მოცემულია სტრინგი "Information".
# ამოიღე "forma" ნაწყვეტი slicing-ით (მინუს ინდექსებითაც)

აქ_მითუმეტეს_არ_ვიცი = "Information"

dadebiti = აქ_მითუმეტეს_არ_ვიცი[2:7]
print(dadebiti)


uaryofiti = აქ_მითუმეტეს_არ_ვიცი[-9:-4]
print(uaryofiti)


# 5)
# მოცემულია სტრინგი "abcdefghijklmno".
# შექმენი სამი სხვადასხვა სლაისი:

# პირველი შეიცავდეს მხოლოდ a დან d მდე ასოებს

# მეორე – შეიცავდეს j დან o მდე ასოებს

# მესამე – შეიცავდეს f დან j მდე ასოებს

anbani = "abcdefghijklmno"

a_d = anbani[:4]
print(a_d)

j_o = anbani[9:]
print(j_o)

f_j = anbani[5:10]
print(f_j)