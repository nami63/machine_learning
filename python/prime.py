import threading

def pri(n):
    flag=False
    if n==1:
        print("not a prime")
    else:
        for i in range(2,n):
            if (n%i)==0:
                flag=True
                break
    if flag:
        print("not")
    else:
        print("yes")

n=int(input(""))
t1=threading.Thread(target=pri,args=(n,))                
t1.start()
t1.join()