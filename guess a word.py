import random
wordlist = ["слово", "космос", "подушка", "аист", "бобр", "голубь"]
word = random.choice(wordlist)
health = 5
while len(word) > 0 and health > 0:
    letter = input("введите букву:")
    if word.find(letter) != -1:
        word = word.replace(letter, "")
        print("Удачная попытка, здоровье =", health)
    elif word.find(letter) == -1:
        health -= 1
        print("Неудачная попытка, здоровье =", health)

if len(word) == 0:
    print("Вы победили!, загаданное слово - это", word)
if health == 0:
    print("Вы проиграли.")