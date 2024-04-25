import threading

def pal(n):
    r=n[::-1]
    if n==r:
        print("palindrome")
    else:
        print("not")

n=input()
t=threading.Thread(target=pal(n))