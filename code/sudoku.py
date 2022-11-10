from ipaddress import collapse_addresses


def valid_solution(sudoku):
    
    colum_list_one = []
    colum_list_two = []
    colum_list_three = []
    colum_list_four = []
    colum_list_five = []
    colum_list_six = []
    colum_list_seven = []
    colum_list_eight = []
    colum_list_nine = []
    colum_index = 0
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_one.append(first_num)
    colum_index = 1
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_two.append(first_num)
    colum_index = 2
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_three.append(first_num)
    colum_index = 3
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_four.append(first_num)
    colum_index = 4
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_five.append(first_num)
    colum_index = 5
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_six.append(first_num)
    colum_index = 6
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_seven.append(first_num)
    colum_index = 7
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_eight.append(first_num)
    colum_index = 8
    for row in sudoku:
        first_num = row[colum_index]
        colum_list_nine.append(first_num)
    for row in sudoku:
        for elem in row:
            




if __name__ == "__main__":
    print("Testing")
    assert valid_solution(       [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 4, 5, 2, 8, 6, 1, 7, 9]])

    assert valid_solution(       [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                                 [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                 [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                 [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                 [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                 [3, 0, 0, 4, 8, 1, 1, 7, 9]]) == False

    assert valid_solution(       [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])

    assert valid_solution(       [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]) == False

    assert valid_solution(       [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 0, 3, 7, 5]
                                ,[7, 0, 6, 3, 8, 0, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 0, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 0, 8, 4, 6]
                                ,[9, 8, 0, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 0, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 0, 6, 4, 2, 1, 3, 5]]) == False

    assert valid_solution(        [[1, 2, 3, 4, 5, 6, 7, 8, 9]
                                 ,[2, 3, 4, 5, 6, 7, 8, 9, 1]
                                 ,[3, 4, 5, 6, 7, 8, 9, 1, 2]
                                 ,[4, 5, 6, 7, 8, 9, 1, 2, 3]
                                 ,[5, 6, 7, 8, 9, 1, 2, 3, 4]
                                 ,[6, 7, 8, 9, 1, 2, 3, 4, 5]
                                 ,[7, 8, 9, 1, 2, 3, 4, 5, 6]
                                 ,[8, 9, 1, 2, 3, 4, 5, 6, 7]
                                 ,[9, 1, 2, 3, 4, 5, 6, 7, 8]]) == False