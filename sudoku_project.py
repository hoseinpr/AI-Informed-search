"""
hohi
"""
import time
numbers = {
    1 : 0, 2 : 0, 3 : 0,
    4 : 0, 5 : 0, 6 : 0,
    7 : 0, 8 : 0, 9 : 0 }


def sudoku_file_reader():
    """For reading sudoko from test files"""
    sudoku_file = []
    path = r"D:\UNIVERCITY\term 6\AI\sudoku\sudoku_test.txt"
    with open(path, 'r', encoding='utf-8') as f_f:
        i = 0
        for line in f_f:
            sudoku_file.append(list(map(list, list(line.strip().replace(' ', '')))))
            for j in range(0,9):
                if sudoku_file[i][j] != ['0']:
                    #pass the sudoku to a function for finding the number of each number
                    how_many_numbers(numbers,sudoku_file[i][j])
            i += 1
    return sudoku_file


def how_many_numbers(numbers, number):
    """For measuring how many of a number exiist in sudoku"""
    numbers[int(number[0])] += 1
    if numbers[int(number[0])] == 9:
        del numbers[int(number[0])]
    return None


def sort_dictionary(numbers):
    """For sorting the dictionary by value B->b """
    sorted_list = dict(sorted(numbers.items(), key=lambda item: item[1], reverse=True)).keys()
    return sorted_list


def print_sudoku(sudoku):
    """For printing sudoko"""
    for i in range(0 , 9):
        for j in range(0 , 9):
            print(sudoku[i][j], end='')
            if j + 1 == 3 or j + 1 == 6:
                print("   " , end='')
        print('')
        if i + 1 == 3 or i + 1 == 6:
            print(" ")
    return None


def now_delete_notes(sudoku, row, col, value):
    """For now_delete_note"""
    for check_row in range(0, 9):
        if len(sudoku[row][check_row]) > 1:
            sudoku[row][check_row] = [s for s in sudoku[row][check_row] if s != value]
    for check_col in range(0, 9):
        if len(sudoku[check_col][col]) > 1:
            sudoku[check_col][col] = [s for s in sudoku[check_col][col] if s != value]


def alone_in_the_box(sudoku, value):
       
    for row in [0, 3, 6]:
        for col in [0, 3, 6]:
            count = 0
            box_row = row + 3
            box_col = col + 3
            for i in range(row, box_row):
                for j in range(col, box_col):
                    for item in range(0, len(sudoku[i][j])):
                        if len(sudoku[i][j]) > 1 and sudoku[i][j][item] == str(value) and count <= 1:
                            count += 1
                            i_temp = i
                            j_temp = j
            if count == 1:
                sudoku[i_temp][j_temp] = [str(value)]
                how_many_numbers(numbers,str(value))
                now_delete_notes(sudoku, i_temp, j_temp, str(value))
                sorted_list_two = sort_dictionary(numbers)
                for check in sorted_list_two:
                    alone_in_the_box(sudoku, check)
                    if check == value:
                        break


def there_is_same_number_in_box(sudoku, row, col, value):
    """check taht if there is a same number already exist or not"""
    box_row = row + 3
    box_col = col + 3
    for i in range(row, box_row):
        for j in range(col, box_col):
            if sudoku[i][j] == [str(value)]:
                return True
    return False


def check_blocks_in_box(sudoku, row, col, value):
    '''nhouoio'''
    box_row = row + 3
    box_col = col + 3
    add_count = 0
    for i in range(row, box_row):
        for j in range(col, box_col):
            if sudoku[i][j] == ['0'] or len(sudoku[i][j]) > 1 :
                col_or_row_allowed = True
                for check in range(9):
                    if sudoku[i][check] == [str(value)] or sudoku[check][j] == [str(value)]:
                        col_or_row_allowed = False
                if col_or_row_allowed:
                    sudoku[i][j].append(str(value)) 
                    i_temp = i
                    j_temp = j
                    add_count += 1
    if add_count == 1:
        sudoku[i_temp][j_temp] = [str(value)]
        how_many_numbers(numbers,str(value))
        now_delete_notes(sudoku, i_temp, j_temp, str(value))
        #start_checking(sudoku)
        

          
def start_checking(sudoku):
    '''yfii'''
    print_sudoku(sudoku)
    sorted_list = sort_dictionary(numbers)
    print(sorted_list)
    for num in sorted_list:
        sorted_list_two = sort_dictionary(numbers)
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if not there_is_same_number_in_box(sudoku , row , col , num):
                    check_blocks_in_box(sudoku, row, col, num)
        for check in sorted_list_two:
            alone_in_the_box(sudoku, check)
            if check == num:
                break
    print("*************************************************")            

    print(numbers)


def divine_promition(sudoku, row, col, value):
    for i in range(9):
        if sudoku[row][i] == [str(value)] or sudoku[i][col] == [str(value)]:
            return False
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[box_row+i][box_col+j] == [str(value)]:
                return False
    return True


def wings_of_angeles(sudoku,row,col):
    digits = []
    for i in range(len(sudoku[row][col])):
        if i > 0:
            digits.append(int(sudoku[row][col][i]))
    return digits


def god_power(sudoku, certain_sudoku):
    sudoku_end = True
    for row in range(9):
        for col in range(9):
            if certain_sudoku[row][col] == ['0']:
                sudoku_end = False
                digits = wings_of_angeles(sudoku,row,col)
                for digit in digits:
                    if divine_promition(certain_sudoku,row,col,digit):
                        certain_sudoku[row][col] = [str(digit)]
                        if god_power(sudoku, certain_sudoku):
                            return True
                        certain_sudoku[row][col] = ['0']
                return False
    if sudoku_end:
        return True


"""main"""

sudoku = sudoku_file_reader()
certain_sudoku = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
start_time = time.time()
start_checking(sudoku)
print(sort_dictionary(numbers))
if numbers != {}:
    for row in range(9):
        for col in range(9):
            if len(sudoku[row][col]) == 1:
                certain_sudoku[row][col] = sudoku[row][col]
            if len(sudoku[row][col]) > 1:
                certain_sudoku[row][col] = ['0']
    god_power(sudoku, certain_sudoku)
print("time: %s sec" % (time.time() - start_time))
print_sudoku(sudoku)

#print_sudoku(certain_sudoku)

