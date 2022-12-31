def permute_a_palindrome (input): 
    num_of_lett = len(input)
    isOdd = num_of_lett%2!=0
    isEven = num_of_lett%2==0
    count_input = 0
    for letter in input:
        lett_count = input.count(letter)
        lett_count_isEven = lett_count%2==0
        if isOdd:
            if lett_count == 1 or lett_count_isEven:
                count_input +=1
            else:
                continue
        if isEven:
            if lett_count_isEven:
                count_input +=1
            else:
                continue
    if count_input == num_of_lett:
        return True
    else:
        return False



if __name__ == "__main__":
    print ("Casos test")
    assert permute_a_palindrome("a")
    assert permute_a_palindrome("aa")
    assert permute_a_palindrome("baa")
    assert permute_a_palindrome("aab")
    assert permute_a_palindrome("baabcd")== False
    assert permute_a_palindrome("racecars")== False
    assert permute_a_palindrome("abcdefghba")== False
    assert permute_a_palindrome("")
