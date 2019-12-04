import numpy as np

mylist =  []
for i in range(0,2) :
    temp = []
    for j in range(0,2):
            temp.append(0)
        mylist.append(temp)

    print(mylist)

    mylist = np.zeros(2,2)
    print(mylist)
