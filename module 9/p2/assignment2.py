"""string"""
def get_guessed_word(secret_word, letters_guessed):
    """string"""
    list_1 = list(secret_word)
    length_1 = len(secret_word)
    astr = ""
    for i in range(length_1):
        count = 0
        for j in letters_guessed:
            if j == list_1[i]:
                count = 1
        if count == 1:
            astr = astr + list_1[i]
        else:
            astr = astr + '_'
    return astr
def main():
    """string"""
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
    print(get_guessed_word(secret_word, list1))
if __name__ == "__main__":
    main()
