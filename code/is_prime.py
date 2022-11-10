from math import sqrt
def is_prime(num):
    is_negative = 0
    if num < 0:
        num = num * -1
        is_negative +=1
    if num < 2:
        return False
    if num < 3:
        return True
    multiples = 0
    while multiples < 2:
        n = num+1
        while n > 2**10:
            n = int(sqrt(n))
        for i in range(1,n):
            if i == 0:
                continue
            if num % i==0:
                multiples += 1
    if multiples > 2:
        return False
    if is_negative>0 and multiples == 2:
        return False
    else:
        return True

if __name__ == "__main__":
    print ("Testing")
    assert is_prime(75) == False
    assert is_prime(-1) == False
    assert is_prime(4) == False
    assert is_prime(0) ==  False
    assert is_prime(2) ==  True
    assert is_prime(-41) ==  False
    assert is_prime(-5) ==  False

    print ("Passed")