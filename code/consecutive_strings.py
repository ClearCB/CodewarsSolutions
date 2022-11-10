def longest_consec(array,k):
    index_actual_element = 0
    largest_consec = ""
    list = []
    if k > len(array) or array == None:
        return largest_consec
    if k == 0:
        return largest_consec
    if k > 1:
        jump_index = k-1
        for string in array[0:-jump_index]:
            jump_index = k-1
            index_next_element = index_actual_element + 1
            while jump_index > 0:
                next_element = array[index_next_element]
                string += next_element
                jump_index -=1
                index_next_element +=1
            list.append(string)
            index_actual_element +=1
    if k == 1:
        list = array
    actual_lenght = 0
    for elem in list:
        if actual_lenght < len(elem):
            actual_lenght = len(elem)
            largest_consec = elem
        else:
            continue

    return largest_consec



if __name__ == "__main__":

    print("Testing")

    assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2) =="abigailtheta"
    assert longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) ==  "oocccffuucccjjjkkkjyyyeehh"
    assert longest_consec([], 3) ==  ""
    assert longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2) ==  "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck"
    assert longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2) ==  "wlwsasphmxxowiaxujylentrklctozmymu"
    assert longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], -2) ==  ""
    assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3) == "ixoyx3452zzzzzzzzzzzz"
    assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 15) == ""
    assert longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0) == ""
    assert longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1) == "oocccffuucccjjjkkkjyyyeehh"
    print("Passed")