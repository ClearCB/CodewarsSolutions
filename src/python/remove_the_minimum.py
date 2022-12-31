def remove_smallest(numbers):
    if numbers == []:
        return numbers
    numbers_copy = numbers.copy()
    numbers_copy.sort()
    first_element = numbers_copy[0]
    numbers.remove(first_element)
    return numbers


remove_smallest([34, 375, 71, 102, 147])