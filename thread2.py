import threading

def squ(n):
    print(f"squre of number{n*n}")

def cu(n):
    print(f"cube of number{n*n*n}")

n=int(input())

t1=threading.Thread(target=squ,args=(n,))
t2=threading.Thread(target=cu,args=(n,))

t1.start()
t2.start()

t1.join()
t2.join()