def zero(operation=None):
    if operation == None:
        return 0
    else:
        result = operation(0)
        return result

def one(operation=None):
    if operation == None:
        return 1
    else:
        result = operation(1)
        return result

def two(operation=None):
    if operation == None:
        return 2
    else:
        result = operation(2)
        return result

def  three(operation=None):
    if operation == None:
        return 3
    else:
        result = operation(3)
        return result

def four(operation=None):
    if operation == None:
        return 4
    else:
        result = operation(4)
        return result

def five(operation=None):
    if operation == None:
        return 5
    else:
        result = operation(5)
        return result

def six(operation=None):
    if operation == None:
        return 6
    else:
        result = operation(6)
        return result

def seven(operation=None):
    if operation == None:
        return 7
    else:
        result = operation(7)
        return result

def eight(operation=None):
    if operation == None:
        return 8
    else:
        result = operation(8)
        return result
        

def nine(operation=None):
    if operation == None:
        return 9
    else:
        result = operation(9)
        return result


def times(right_op):
    def temp(left_op):
        result = left_op * right_op
        return result
    return temp

def divided_by(right_op):
    def temp(left_op):
        result = left_op // right_op
        return result
    return temp

def plus(right_op):
    def temp(left_op):
        result = left_op + right_op
        return result
    return temp

def minus(right_op):
    def temp(left_op):
        result = left_op - right_op
        return result
    return temp




if __name__ == "__main__":
    print ("Testing")
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) == 5
    assert six(divided_by(two())) == 3
    print ("Passed")