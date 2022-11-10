def alphabet_position(string):
    if len(string) <1:
        return string
    string = string.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_list = tuple(alphabet)
    number = 1
    diccionari_conversion = {}
    new_string = ""

    for j in alphabet_list:
        diccionari_conversion[j]=str(number)
        number += 1
    for k in string:
        is_in =  k in alphabet_list
        if is_in:
            k = diccionari_conversion[k]
            k = str(k)
            new_string += (k + " ")
        else:
            continue
    new_string = new_string[0:-1]
    return new_string

if __name__ == "__main__":
    print ("Probando casos test")
    assert alphabet_position("The sunset sets at twelve o' clock.") == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
    assert  alphabet_position("The narwhal bacons at midnight.") == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
    print ("Todos los test superados")