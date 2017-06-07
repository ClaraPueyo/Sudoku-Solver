
"""
Created on Wed Jun 07 14:15:37 2017

@author: Clara Pueyo
"""
import numpy as np

sudoku = open('inputfile.txt', 'r')
numbers = sudoku.readlines()
sudokutable = np.zeros((9,9))

for k in range(0,9):
    m=numbers[k].replace(";","0")
    n1 = int(m[0])
    n2 = int(m[1])
    n3 = int(m[2])
    n4 = int(m[3])
    n5 = int(m[4])
    n6 = int(m[5])
    n7 = int(m[6])
    n8 = int(m[7])
    n9 = int(m[8])
    sudokutable[k]=[n1,n2,n3,n4,n5,n6,n7,n8,n9]

print 'We have to solve the sudoku table below:'
print sudokutable

def print_table():
    for i in range(9):
        print(sudokutable[i])


def used_in_row(row, num):

    for j in range(9):
        if sudokutable[row][j] == num: 
            return True

    return False


def used_in_column(col, num):

    for i in range(9):
        if sudokutable[i][col] == num: 
            return True

    return False

def used_in_box(x, y, num):

    for i in range(3):
        for j in range(3):
            if sudokutable[i+x][j+y] == num: 
                return True

    return False


def is_it_free(i, j, num):

    return not used_in_row(i, num) and not used_in_column(j, num) and not used_in_box(i-i%3, j-j%3, num)


def sudokusolver(i, j):
    
    if i == 9: return True
        
    if sudokutable[i][j]:
        if j == 8:
        
            if sudokusolver(i+1, 0): return True
        else:
            
            if sudokusolver(i, j+1): return True

        return False  

    
    for num in range(1,10):  
        if is_it_free(i, j, num):
            sudokutable[i][j] = num 
   
            if (j == 8):
                
                if sudokusolver(i+1, 0): return True
            else:
               
                if sudokusolver(i, j+1): return True
   
            
            sudokutable[i][j] = 0

    return False 


if sudokusolver(0, 0):
    print 'The solution is:'
    print_table()
else:
    print 'Not solution available'

    
    