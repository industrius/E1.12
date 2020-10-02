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

def update_hidden_word(char, secret_word, hidden_word):
    """
    Обновление отображаемого слова с учетом угаданных букв
    """
    new = ""
    for i in range(len(secret_word)):
        if char == secret_word[i]:
            new += char
        else:
            new += hidden_word[i] 
    return new


def check_input(char, secret_word):
    """
    Проверка введенной буквы на совпанение с загаданным словом
    """
    if char in secret_word:
        return True
    else:
        return False


while wrong < max_wrong and hidden_word != secret_word:
    print("\nКоличество ошибок: ", wrong)
    print("\nСлово: ", hidden_word)
    char = input("\n\nВведите букву: ").upper()
   
    while char in hidden_word:
        print("Такая буква уже была")
        char = input("Введите букву: ").upper()

    if check_input(char, secret_word):
        hidden_word = update_hidden_word(char, secret_word, hidden_word)
        print("\nУгадал")
    else:
        wrong += 1
        print("\nОшибка")


if wrong == max_wrong:
    print("\nПроиграл")
else:
    print("\nПобедил")
    
print("\nА слово было: ", secret_word)