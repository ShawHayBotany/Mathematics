n=0
m=0
n=input("Enter a value: ")
m=input("Enter another value: ")

def EA(n,m):
    q=n/m
    r=n%m
    if r==0:
        return m
    else:
        return EA(m,r)
print("The GCD of",n,"and",m,"is",EA(n,m))