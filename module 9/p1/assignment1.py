"""Guess word"""
def is_word_guessed(secret_word, letters_guessed):
    """ guess word """
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True
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
