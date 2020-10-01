import random
 
secret_word = random.choice([
    "skillfactory", 
    "testing", 
    "blackbox", 
    "pytest", 
    "unittest", 
    "coverage"
    ]).upper()
hidden_word = "_" * len(secret_word)
wrong = 0
max_wrong = 4

while wrong < max_wrong and hidden_word != secret_word:
    print("\nКоличество ошибок: ", wrong)
    print("\nСлово: ", hidden_word)
    char = input("\n\nВведите букву: ").upper()
   
    while char in hidden_word:
        print("Такая буква уже была")
        char = input("Введите букву: ").upper()
 
    if char in secret_word:
        print("\nУгадал")

        new = ""
        for i in range(len(secret_word)):
            if char == secret_word[i]:
                new += char
            else:
                new += hidden_word[i]              
        hidden_word = new
 
    else:
        print("\nОшибка")
        wrong += 1
 
if wrong == max_wrong:
    print("\nПроиграл")
else:
    print("\nПобедил")
    
print("\nА слово было: ", secret_word)