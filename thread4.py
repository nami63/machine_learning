import threading

matrix = [
    [5, 8, 2, 7],
    [3, 9, 6, 1],
    [4, 0, 2, 5],
    [7, 3, 8, 6]
]

maxvalue=float('-inf')
minvalue=float('inf')
lock=threading.Lock()

def minp():
    global minvalue
    for row in range(2):
        for col in range(2):
            value=matrix[row*2][col*2]
            lock.acquire()
            minvalue=min(minvalue,value)
            lock.release()

def maxp():
    global maxvalue
    for row in range(2):
        for col in range(2):
            value=matrix[row*2][col*2]
            lock.acquire()
            maxvalue=max(maxvalue,value)
            lock.release()
            
t1=threading.Thread(target=minp)
t2=threading.Thread(target=maxp)

t1.start()
t2.start()

t1.join()
t2.join()

print("Min value:", minvalue)
print("Max value:", maxvalue)
