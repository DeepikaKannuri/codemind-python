n = int(input())
if n<0:
    rev=0
    n=n*-1
    while n:
        rev=rev*10+n%10
        n//=10
    print("-"+str(rev))
else:
    rev=0
    while n:
        rev=rev*10+n%10
        n//=10
    print(rev)