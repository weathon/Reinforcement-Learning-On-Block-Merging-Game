import numpy as np
import random 

field = np.zeros((6,6))
steps = 0
score = 0

def display():
    print("0\t1\t2\t3\t4\t5")
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i,j]== 0:
                print("_",end="\t")
            else:
                print(int(field[i,j]),end="\t")
        print()



def push_block(col, num):
    if field[5][col] != 0:
        print("Game over!")
        quit()
    for i in range(4,-1,-1):
        if field[i][col] != 0:
            field[i+1][col] = num
            return
    field[0][col] = num
    

def check_merging():
    pass

while 1:
    display()
    next_number = 2**random.choice([1,1,1,1,1,1,2,2,2,2,2,3,3])
    print("The next number is: %s" % next_number)
    ans = int(input("Which col (starts with 0) you want to put it to? "))
    push_block(ans,next_number)
    check_merging()