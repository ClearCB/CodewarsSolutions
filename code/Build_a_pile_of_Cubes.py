def find_nb(number):
    next = 0
    n = 0
    while number > n:
        next +=1
        n += next**3
    numb = 1
    for i in range(2,next+1):
        numb += (i**3)
    if numb==number:
        return next
    else:
        return -1



if __name__ == "__main__":
    print("Testing")
    assert find_nb(4183059834009) == 2022
    assert find_nb(135440716410000) == 4824
    assert find_nb(40539911473216) == 3568
    assert find_nb(26825883955641) == 3218
    assert find_nb(24723578342962) == -1
    print("Passed")