# 1)შექმენით სია -->  ["ina" , "givi" , "nika" , "daviti" , "ia" , "lizi"] , თქვენი დავალებაა რომ პირველი 2 ელემენტი ჩაანაცვლოთ შემდეგი სიით --> ["irina" , "milana" , "kira", "mate"] //////////////// და ასევე სიის ბოლო ორი ელემენტი შეანაცვლე შემდეგი სიით --> ["gia" , "emzari" , "xvicha"] ამის შემდეგ დაპრინტეთ საბოლოო სია

saxelebi = ["ina", "givi", "nika", "daviti", "ia", "lizi"]

saxelebi[:2] = ["irina", "milana", "kira", "mate"]

saxelebi[-2:] = ["gia", "emzari", "xvicha"]

print(saxelebi)




რიცხვი = int(input("შეიყვანეი რიცხვი: "))

if რიცხვი % 2 == 0:
    print("EVEN")
else:
    print("ODD")