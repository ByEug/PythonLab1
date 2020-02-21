import string

WordBase = dict()

with open('/home/eugene/PycharmProjects/lab1/forTask1', 'r', encoding='utf-8') as file:
    for line in file:
        table = str.maketrans(dict.fromkeys(string.punctuation))
        line = line.translate(table)
        words = line.split()

        for word in words:
            WordBase.setdefault(word, 0)
            WordBase[word] += 1

for key in WordBase:
    print(key, WordBase[key])

sentence = ""
counter = 0
for i in sorted(WordBase.items(), key=lambda key_value: key_value[1], reverse=True):
    if counter == 0:
        sentence += i[0].capitalize()
        counter += 1
    elif counter < 10:
        sentence += ' '
        sentence += i[0]
        counter += 1
sentence += '.'
print(sentence)
