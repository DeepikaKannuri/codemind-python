n=int(input())
on=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0
while n:
    if n%10==1:
        on+=1
    elif n%10==2:
        two+=1
    elif n%10==3:
        three+=1
    elif n%10==4:
        four+=1
    elif n%10==5:
        five+=1
    elif n%10==6:
        six+=1
    elif n%10==7:
        seven+=1
    elif n%10==8:
        eight+=1
    elif n%10==9:
        nine+=1
    n//=10
if on<2 and two<2 and three<2 and four<2 and five<2 and six<2 and seven<2 and eight<2 and nine<2:
    print("Unique Number")
else:
    print("Not Unique Number")


    