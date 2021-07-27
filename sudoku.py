# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 17:39:10 2021

@author: Ksheer
"""
#%%
length_of_sudoku_grid=int(input('Enter Length of Sudoku (X*X):'))
col=[]
row=[]
tot_sq=[]
var=1
for i in range(pow(length_of_sudoku_grid,2)):
    print('Enter coloumn',var,'space seperated')
    var=var+1
    a=list(map(int,input().split()))
    col.append(a)
for i in range(pow(length_of_sudoku_grid,2)):
    main=[]
    for j in range(pow(length_of_sudoku_grid,2)):
        main=main+[col[j][i]]
    row.append(main)
for i in range(1,pow(length_of_sudoku_grid,2)+1):
    tot_sq.append(i)   
def check(f,t):
    som=0
    for i in t:
        if i in f:
            som=som+1
        else:
            break
    if som==pow(length_of_sudoku_grid,2):
        return 1
    else:
        return 0
def subgridcheck(col):
  for row_var in range(0,pow(length_of_sudoku_grid,2),length_of_sudoku_grid):
      for col_var in range(0,pow(length_of_sudoku_grid,2),length_of_sudoku_grid):
         temp = []
         for row_num in range(row_var,row_var+length_of_sudoku_grid):
            for col_num in range(col_var,col_var+length_of_sudoku_grid):
              if col[row_num][col_num] != 0:
                temp.append(col[row_num][col_num])
         if len(temp) != len(set(temp)):
             return 0
  return 1    
chk=0
for i in range(pow(length_of_sudoku_grid,2)):
    if check(row[i],tot_sq)==1 and subgridcheck(col)==1 and check(col[i],tot_sq)==1:
        chk=chk+1
        continue
    else:
        print('Sudoku Not Solved')
        break   
if chk==pow(length_of_sudoku_grid,2):     
    print('Sudokou Solved')
