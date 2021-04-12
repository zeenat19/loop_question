num=int(input("enter any num:"))
i=1
sum=0
i=num
while i>0:
    digit=i%10
    sum=sum+digit**3
    i//=10
    
if num==sum:
    print(num,"it is armstrong num")
else:
    print(num,"it is not armstrong num")

    