import threading

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

def calculate_and_print_fibonacci(n):
    for i in range(n+1):
        print(fib(i))

n = int(input("Enter the number of Fibonacci numbers to calculate: "))

t1 = threading.Thread(target=calculate_and_print_fibonacci,args=(n,))
t1.start()
t1.join()
