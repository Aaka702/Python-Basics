def camelcase(s):
    words = []
    current_word = []

    for letter in s:
        print(letter)
        if letter.isupper() and current_word:
            words.append(''.join(current_word))
            current_word = []
            #print(current_word)
        current_word.append(letter)

    if current_word:
        words.append(''.join(current_word))

    for word in words:
        print(word)

if __name__ == '__main__':
    s = input()
    camelcase(s)
