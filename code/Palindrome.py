def permute_a_palindrome(string):
    large_string = len(string)
    letter_able = 0
    letter_able_alone = 0
    for letter in string:
        letter_count = string.count(letter)
        letter_count_is_even = letter_count % 2 == 0
        if letter_count_is_even:
            letter_able += 1
        if letter_count == 1:
            letter_able += 1
            letter_able_alone += 1
        else:
            continue
    if large_string == 1:
        return True
    if letter_able == large_string and letter_able_alone <= 1:
        return True
    else:
        return False




if __name__ == "__main__":
    print ("Casos test")
    assert permute_a_palindrome("a")
    assert permute_a_palindrome("aa")
    assert permute_a_palindrome("baa")
    assert permute_a_palindrome("aab")
    assert permute_a_palindrome("baabcd") == False
    assert permute_a_palindrome("racecars")== False
    assert permute_a_palindrome("abcdefghba")== False
    assert permute_a_palindrome("")
