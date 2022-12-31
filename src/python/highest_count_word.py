def high(string):
    string = string.split(" ")
    dicc_alphabet = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    highest_count = 0
    highest_word = ""
    for word in string:
        word_count = 0 
        for letter in word:
            word_count += dicc_alphabet[letter]
        if word_count > highest_count:
            highest_count = word_count
            highest_word = word
        else:
            continue
    return highest_word





if __name__ == "__main__":
    print("Testing")
    assert high('man i need a taxi up to ubud'), 'taxi'
    assert high('what time are we climbing up the volcano'), 'volcano'
    assert high('take me to semynak'), 'semynak'
    assert high('aa b'), 'aa'
    assert high('b aa'), 'b'
    assert high('bb d'), 'bb'
    assert high('d bb'), 'd'
    assert high("aaa b"), "aaa"
    print("Passed")