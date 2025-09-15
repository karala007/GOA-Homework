str = ["mamuka" , "BMW" , "LOL" , "hidroeleqtrosadguri" , "yveli" , "hipermarketi" , "whats 9 + 10?" , "21" , "you stupid"]


while True:
    index = int(input("put any number from 0 to 8 :"))

    if index >= 0 and index <= 8:
        print("you chose:", str[index])
        break
    else:
        print("pleas choose from 0 to 8")


