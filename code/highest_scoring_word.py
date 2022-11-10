def high(x):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters = tuple(letters)
    numbers = range(1,27)
    dicc = {letters:numbers}
    dicc = dicc.items()
    list_x = x.split(" ")
    for i in list_x:    
        for key,value in dicc:
                return x
            



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