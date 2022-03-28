import numpy as np
import random 
import os
import pyGameDisplay.generateFrame

def init():
    global choices, field, steps, score, merge
    choices = [2,2,2,4,4,4,8]
    field = np.zeros((6,6))
    steps = 0
    score = 0
    merge = 0



"""Score: 8.0
Steps: 10
0       1       2       3       4       5
_       4       8       _       _       8
_       2       _       _       _       _
_       8       _       _       _       _
_       _       _       _       _       _
_       _       _       _       _       _
_       _       _       _       _       _
The next number is: 4
Which col (starts with 0) you want to put it to? 
Still need hor check, or "1" will be died"""

"""Score: 8.0
Steps: 12
0    1    2    3    4    5    
4    8    4    _    _    _    
2    _    8    _    _    _    
8    _    _    _    _    _    
_    _    _    _    _    _    
_    _    _    _    _    _    
_    _    _    _    _    _    
The next number is: 4
Which col (starts with 0) you want to put it to? 3



looping
"""

def display():
    print("Score: %s\nSteps: %s" % (score,steps))
    # print("0\t1\t2\t3\t4\t5")
    for i in range(6):
        print('{0: <5}'.format(str(i)),end="")
    print()

    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i,j]== 0:
                print('{0: <5}'.format("_"),end="")
            else:
                print('{0: <5}'.format(int(field[i,j])),end="")
        print()

def push_block(col, num):
    if field[5][col] != 0: # Should I check merge first? Yes
        if field[5][col] == num:
            field[5][col] = num*2
            return
        print("Game over!")
        return -1
    for i in range(4,-1,-1):
        if field[i][col] != 0:
            if field[i][col] == num:
                field[i][col] = 2*field[i][col]
                return 0
            field[i+1][col] = num
            return 0
    field[0][col] = num
    
def check_merging():
    global merge
    while 1:
        last_stage = np.copy(field)
        # from bottom up, so there will no be gaps
        # tested hor check works
        for col in range(0,6):
            for i in range(4,-1,-1):
                if field[i][col] == field[i+1][col]:
                    field[i+1][col] = 0
                    field[i][col] = field[i][col]*2
        merge+=1
        if np.array_equal(last_stage,field): #no change
            break

    while 1:
        last_stage = np.copy(field)
        # from bottom up, so there will no be gaps
        # tested hor check works
        for i in range(0,6):
            for col in range(4,-1,-1):
                if field[i][col] == field[i][col+1]:
                    field[i][col+1] = 0
                    field[i][col] = field[i][col]*2 #bizixkouzangxkouhungbizizene haixuyaodrop
        merge+=1 
        if np.array_equal(last_stage,field): #no change
            break

    while 1:
        last_stage = np.copy(field) # forget this
        for col in range(0,6):
            for i in range(4,-1,-1):
                if field[i][col] == 0:
                    field[i][col] = field[i+1][col]
                    field[i+1][col] = 0
        # merge+=1 
        if np.array_equal(last_stage,field): #no change
            break



if __name__ == "__main__":
    init()
    i = 0
    while 1:
        display()
        next_number = random.choice(choices)
        print("The next number is: %s" % next_number)
        ans = int(input("Which col (starts with 0) you want to put it to? "))
        if push_block(ans,next_number) == -1:
            quit()
        check_merging()
        steps += 1
        score = np.max(field)
        os.system("clear")
        maxNum = np.max(field)
        if not maxNum in choices:
            choices.append(int(maxNum/2))
        pyGameDisplay.generateFrame.generateFrame(i,field,next_number)
        i+=1

