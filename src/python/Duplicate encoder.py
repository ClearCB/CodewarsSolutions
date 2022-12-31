def duplicate_encode(string):
    string = string.lower()
    new_string = ""
    for letter in string:
        letter_count = string.count(letter)
        if letter_count == 1:
            new_string +=  "("
        if letter_count > 1:
            new_string += ")"
    return new_string


if __name__ == "__main__":
    print ("Probando casos test")
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())" # "should ignore case"
    assert duplicate_encode("(( @") == "))(("
    print ("Todos los casos aprobados")