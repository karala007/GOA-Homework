# no classwork
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