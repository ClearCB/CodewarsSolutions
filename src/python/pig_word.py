def pig_it(text):
    text = text.split(" ")
    list_text = list(text)
    new_list = []
    cuestion_marks = "?¿!¡.,"
    for word in list_text:
        if cuestion_marks.find(word) == -1:
            new_word = word[1:] +  word [0] +  "ay"
            new_list.append(new_word)
        else:
            new_list.append(word)
    new_list = " ".join(new_list)
    return new_list

if __name__ == "__main__":
    print ("Testing")
    assert pig_it("O tempora o mores !") == 'Oay emporatay oay oresmay !'
    print ("Passed")