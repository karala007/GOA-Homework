queue = ["first", "second"]
rigi = input("rame shemoiyvane:")
queue.insert(0,rigi)

if len(queue) > 5:
    queue.pop()
    print(queue)
else:
    queue.reverse()
    print(queue)