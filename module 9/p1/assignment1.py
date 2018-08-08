"""Guess word"""
def is_word_guessed(secret_word, letters_guessed):
    """Guess word"""
    list_1 = list(secret_word)
    length_1 = len(secret_word)
    count = 0
    for i in list_1:
        for j in letters_guessed:
            if j == i:
                count = count+1
    return bool(count == length_1)
def main():
    """Guess word"""
    user_input = input()
    if user_input:
        data = user_input.split(" ")
        secret_word = data[0]
    else:
        data = []
        secret_word = ""
    list1 = []
    for j in range(1, len(data)):
        list1.append(data[j][0])
    print(is_word_guessed(secret_word, list1))
if __name__ == "__main__":
    main()
