def solution(number): 
    sum = 0
    while sum == 0:
        number = number - 1
        is_mutiple_three = number % 3 == 0
        is_mutiple_five = number % 5 == 0
        if number < 0:
            return sum
        if is_mutiple_five or is_mutiple_three:
            for num in range (2,number+1):
                num_is_multiple_three = (num % 3 == 0)
                num_is_multiple_five = (num % 5 == 0)
                if num_is_multiple_three:
                    sum += num
                elif num_is_multiple_five:
                    sum += num
                else:
                    continue
        else:
            continue
    return sum



if __name__ == "__main__":
    print ("Testing")
    assert solution(4)==3
    assert solution(5)==3
    assert solution(95)==2028
    assert solution(3)==0
    assert solution(6)==8

    print ("Passed")