import threading
import time

class CountThread(threading.Thread):
    def __init__(self, title, start, end, time):
        super.__init__()
        self._title = title
        self._start = start
        self._end = end
        self._time = time
    def __str__(self):
        return "count"

    def run(self):
        for i in range(self._start, self._end + 1)
            print(self._title, i)
            time.sleep(self._time)

            print("count end", self._title)

    def func():
        print("func")

c1= CountThread("aaa",1,5,0.5),
c1.start()
c2= CountThread("bbb",1,5,0.5),
c2.start()
CountThread("ccc",1,5,0.5).start()


print("main end")