n=int(input())
s=n**2
p=0
while s>0:
    a=s%10
    p=a+p
    s=s//10
if p==n:
    print('Neon Number')
else:
    print('Not Neon Number')