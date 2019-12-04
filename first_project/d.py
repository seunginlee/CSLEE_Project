import time
import threading
from subprocess import _args_from_interpreter_flags


def count(low,high):
    tot = 0
    for i in range(low,high):
        print("count :" + str(i))
        tot += i
        time.sleep(1)
    print("count end : " + str(tot))

def doSum(start, end) :
    for i in range(start, end) :
        print("doSum",i)
        time.sleep(0.7)
        print("doSum end")

print("main start")
#count(3,5)
t = threading.Thread(target=count,_args=(3,5))
t.start()
doSum(30,37)
print("main end")
