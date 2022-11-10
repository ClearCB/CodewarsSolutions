def is_valid_walk(walk):
    dicc_directions = {"n":0,"s":0,"w":0,"e":0}
    for direction in walk:
        dicc_directions[direction] = dicc_directions[direction] + 1
    if sum(dicc_directions.values()) != 10:
        return False
    if (dicc_directions ["n"] - dicc_directions["s"]) != 0:
        return False
    if (dicc_directions ["w"] - dicc_directions["e"]) != 0:
        return False
    else:
        return True

if __name__ == "__main__":
    print("Testing")
    assert is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])


    print("Passed")