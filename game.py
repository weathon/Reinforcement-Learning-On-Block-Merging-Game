import numpy as np
import random 

field = np.zeros((5,6))
steps = 0
score = 0

def display():
    print("0\t1\t2\t3\t4\t5")
    for i in range(field.shape[0]):
        for j in range(field.shape[1]):
            if field[i,j]== 0:
                print("_",end="\t")
            else:
                print(int(field[i,j]))
        print()

def check_merging():
    pass

while 1:
    display()
    next_number = 2**random.choice([1,1,1,1,1,1,2,2,2,2,2,3,3])
    print("The next number is: %s" % next_number)
    ans = input("Which col (starts with 0) you want to put it to? ")  