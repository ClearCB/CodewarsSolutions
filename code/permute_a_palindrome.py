def permute_a_palindrome(string):
    print(string)
    string = string.lower()
    large_string = len(string)
    if large_string <= 1:
        return True
    letter_able = 0
    letter_able_alone = 0
    for letter in string:
        letter_count = string.count(letter)
        letter_count_is_even = letter_count % 2 == 0
        if letter_count == len(string):
            return True
        if letter_count_is_even:
            letter_able += 1
        if letter_count == 1:
            letter_able += 1
            letter_able_alone += 1
        else:
            continue
    if letter_able == large_string and letter_able_alone <= 1:
        return True
    else:
        return False