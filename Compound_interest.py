p,r,t=map(int,input().split())
k=1+(r/100)
i=(p*(k**t))
print("{:.2f}".format(i))