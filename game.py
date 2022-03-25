import numpy as np
import random 
import os
field = np.zeros((6,6))
steps = 0
score = 0
merge = 0

def display():
    print("Score: %s\nSteps: %s" % (score,steps))
    print("0\t1\t2\t3\t4\t5")
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i,j]== 0:
                print("_",end="\t")
            else:
                print(int(field[i,j]),end="\t")
        print()



def push_block(col, num):
    if field[5][col] != 0: # Should I check merge first? Yes
        if field[5][col] == num:
            field[5][col] = num*2
            return
        print("Game over!")
        quit()
    for i in range(4,-1,-1):
        if field[i][col] != 0:
            if field[i][col] == num:
                field[i][col] = 2*field[i][col]
                return
            field[i+1][col] = num
            return
    field[0][col] = num
    

def check_merging():
    global merge
    while 1:
        last_stage = np.copy(field)
        # from bottom up, so there will no be gaps
        for col in range(0,6):
            for i in range(4,-1,-1):
                if field[i][col] == field[i+1][col]:
                    field[i+1][col] = 0
                    field[i][col] = field[i][col]*2
        merge+=1
        if np.array_equal(last_stage,field): #no change
            return

while 1:
    display()
    next_number = 2**random.choice([1,1,1,1,1,1,2,2,2,2,2,3,3])
    print("The next number is: %s" % next_number)
    ans = int(input("Which col (starts with 0) you want to put it to? "))
    push_block(ans,next_number)
    check_merging()
    steps += 1
    score = np.max(field)
    os.system("clear")