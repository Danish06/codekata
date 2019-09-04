a,b,c=map(int,input().split())
if(a>b and a>c):
    if(a*a==(b*b)+(c*c)):
        print('yes')
elif(b>c and b>a):
    if(b*b==(a*a)+(c*c)):
        print('yes')
else:
    if(c*c==(a*a)+(b*b)):
        print('yes')
