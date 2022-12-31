def anagrams(string, list):
    string = string.lower()
    list_lower = []
    end_list = []
    len_string = len(string)
    for elem in list:
        list_lower.append(elem.lower())
    for i in list:
        equal_letter = 0
        for j in i:
            len_elem_list = len(i)
            string_count = string.count(j)
            i_count = i.count(j)
            if string_count == i_count:
                equal_letter += 1
                if equal_letter == len_string and equal_letter == len_elem_list:
                    end_list.append(i)
                continue
            else:
                break

            


    return end_list






if __name__ == "__main__":
    print ("Starting test cases")
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada', 'abbb', 'aaab']) == ["aabb","bbaa"]
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']
    assert anagrams('laser', ['lazing', 'lazy', 'lacer']) == []
    print ("All test cases passed")