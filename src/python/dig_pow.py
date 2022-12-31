def dig_pow(n, p):
    n = str(n)
    number_to_elevate = p
    sum = 0
    for number in n:
        number = int(number)
        sum += number**number_to_elevate
        number_to_elevate += 1
    its_k = sum/ int(n)
    int_k = int(its_k)
    multp = int(n) * int_k
    if multp == sum:
        return int(its_k)
    else:
        return -1


dig_pow (46288,5)
                