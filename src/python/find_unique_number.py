def find_uniq(arr):
    arr.sort()
    if(arr[0] < arr[len(arr)-1] and arr[0] < arr[len(arr)-2]):
        n = arr[0]
    else:
        n = arr[len(arr)-1]
    return n
if __name__ == "__main__":
    print("Testing")
    assert find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    assert find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    assert find_uniq([ 3, 10, 3, 3, 3 ]) == 10
    print("Passed")