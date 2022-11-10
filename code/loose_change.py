def loose_change(numb):
    coin_value = {'Quarters': 25,'Dimes': 10,'Nickels': 5,'Pennies': 1}
    coin_value_items = coin_value.items()
    change = {'Quarters': 0, 'Dimes': 0, 'Nickels': 0,'Pennies': 0}
    for key, value in coin_value_items:
        is_in = numb // value >= 1 
        while is_in:
            change[key]+=1
            numb -= value
            is_in = numb // value >= 1 
    return change





if __name__ == "__main__":
    print ("Testing")
    assert loose_change(29) == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
    assert loose_change(91) == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
    assert loose_change(0) ==  {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(-2) == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
    assert loose_change(3.9) == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
    print ("Passed")