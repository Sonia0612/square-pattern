def range_func(n):
    for i in range(n):
        for j in range(n):
            print(i+1,end="")
        print()

def while_func(n):
    i=1
    while i<=n:
        j=1
        while j<=n:
            print(i,end='')
            j=j+1
        print()
        i=i+1
n=int(input())
while_func(n)
range_func(n)