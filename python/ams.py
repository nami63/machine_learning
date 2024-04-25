import threading

def ams(n):    
    sum=0
    s=n
    while n>0:
        r=n%10
        sum=sum+r**3
        n=n//10

    if s==sum:
        print("amstrong")
    else:
        print("not")

n = int(input("Enter a number: "))

t1 = threading.Thread(target=ams, args=(n,))
t1.start()
