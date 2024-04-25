def add(x,y):
    return x+y

def sun(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice=(input("choice "))

    if choice in(1,2,3,4):
        n1=int(input())
        n2=int(input())

    if choice=="1":
        print("result ",add(n1,n2))
    elif choice=="2":
        print("result",sun(n1,n2))
    elif choice=="3":
        print("result",mul(n1,n2))
    elif choice=="4":
        print("result",div(n1,n2))

    break
else:
    print("invalid")