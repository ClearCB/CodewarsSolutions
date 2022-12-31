def zero(function):
    global left_op 
    left_op= 0
def one(function): 
    global left_op
    left_op = 1
def two(function):
    global left_op
    left_op = 2
def three(function):
    global left_op
    left_op = 3
def four(function):
    global left_op
    left_op = 4
def five(function):
    global left_op
    left_op = 5
def six(function): 
    global left_op
    left_op = 6
def seven(function): 
    global left_op
    left_op = 7
def eight(function): 
    global left_op
    left_op = 8
def nine(function): 
    global left_op
    left_op = 9

def plus(function_1):
    right_op = function_1
    result = (left_op+right_op)
    return result
def minus(function_1):
    right_op = function_1
    result = (left_op-right_op)
    return result
def times(function_1):
    right_op = function_1
    result = (left_op*right_op)
    return result
def divided_by(function_1):
    right_op = function_1
    result = (left_op//right_op)
    return result



if __name__ == "__main__":
    print("Testing")
    assert seven(times(five())) == 35
    assert four(plus(nine())) == 13
    assert eight(minus(three())) ==  5
    assert six(divided_by(two())) == 3
    print("Passed")