a=input('ENTER FIRST NUMBER ')
b=input('ENTER SECOND NUMBER ')
c=input('ENTER THIRD NUMBER ')

if a>b:
    if a>c:
        print a,' is the largest among ',a,b,c
    else :
        print c,' is the largest among ',a,b,c
elif b>c:
    if b>a:
        print b,' is the largest among ',a,b,c
    else :
        print a,' is the largest among ',a,b,c
elif c>a:
    if c>b:
        print c,' is the largest among ',a,b,c
    else :
        print b,' is the largest among ',a,b,c
elif a==b==c:
    print a,b,c,' are same '
