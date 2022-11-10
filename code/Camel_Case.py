def to_camel_case(string):
    if string == "":
        return string
    string = string.replace("-",",").replace("_",",").split(",")
    list_string_but_first = string [1:]
    new_string = string [0]
    for elem in list_string_but_first:
        len_elem = len(elem)
        if len(elem)>0:
            camelled_word = str((elem[0].upper())+elem[1:])
            new_string += camelled_word
        else:
            continue
    return new_string

if __name__ == "__main__":
    print ("Starting test")
    assert to_camel_case('') == ('')
    assert to_camel_case("the_stealth_warrior") == ("theStealthWarrior")
    assert to_camel_case("The-Stealth-Warrior") == ("TheStealthWarrior")
    assert to_camel_case("A-B-C") == ("ABC")
    assert to_camel_case("the_Cat-was_kawaii") == ("theCatWasKawaii")
