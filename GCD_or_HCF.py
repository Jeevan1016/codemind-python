a,b=map(int,input().split())
while True:
    if a==0 or b==0:
        break
    elif a>b:
        a=a%b
    elif b>a:
        b=b%a
print(max(a,b))