n = int(input())
sq=n*n
sum=0
while sq:
    sum+=sq%10
    sq//=10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")