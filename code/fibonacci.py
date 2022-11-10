def tribonacci(array,n):
    if n == 0:
        return [] 
    the_list = array[:]
    to_sum = []
    len_the_list = len(the_list)
    while len_the_list < n:
        for i in array:
            len_to_sum = len(to_sum)
            if len_to_sum == 3:
                elem_to_add = sum(to_sum)
                array.append(elem_to_add)
                the_list.append(elem_to_add)
                to_sum = []
                array = array[1:]
                len_the_list = len(the_list)
            else:
                to_sum.append(i)
    return the_list[0:n]

# def tribonacci(signature,n):
#     result = signature.copy()
#     if n==0:
#         return []
#     while len(result) < n:
#         result.append(sum(result[-3:]))
#     return result[:n]

if __name__ == "__main__":
    print("Testing")
    assert tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    assert tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    assert tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    assert tribonacci([1, 0, 0], 10) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
    assert tribonacci([0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
    assert tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190]
    assert tribonacci([1, 1, 1], 1) == [1]
    print("Passed")