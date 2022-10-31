a=int(input())
b=int(input())
s_a=0
s_b=0
for i in range(1,a):
    if a%i==0:
        s_a+=i
for i in range(1,b):
    if b%i==0:
        s_b+=i
if s_a==b and s_b==a:
    print('Amicable')
else:
    print('Not Amicable')