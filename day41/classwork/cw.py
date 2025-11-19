# 1)შექმენით სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიის ბოლოში დაამატე სიტყვა --> "ianvari" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა

rame = [980, "saba", 231, "kote", "cico", True, "gio", 40.5]
rame.append("ianvari")
print(rame)

# 2)შექმენი სია ---> [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიაში მეორე ინდექსზე დაამატე სიტყვა ---> "bati" და დაპრინტე საბოლოო სია ნახე დაემატა თუ არა

esecise = [980, "saba", 231, "kote", "cico", True, "gio", 40.5]
esecise.insert(2, "bati")
print(esecise)

# 3)შექმენი სია ---->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე მე 5 ინდექსზე მდგომი ელემენტი და დაპრინტე საბოლოო სია ნახე ამოიშალა თუ არა

shavi_sia = [980, "saba", 231, "kote", "cico", True, "gio", 40.5]
shavi_sia.pop(5)
print(shavi_sia)

# 4)შექმენი სია --->  [980 , "saba", 231 , "kote" , "cico" , True , "gio" , 40.5] ამ სიიდან ამოშალე True და ასევე ამოშალე "kote" და დაპრინტე საბოლოო სია და ნახე ამოიშალა თუ არა

chorni = [980, "saba", 231, "kote", "cico", True, "gio", 40.5]
chorni.remove(True)
chorni.remove("kote")
print(chorni)