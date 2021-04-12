num=int(input("enter any num"))
i=1
sum=0
while i<=num:
    a=num%i
    num=num//10
    sum=sum+a
    i=i+1
if sum==num:
    print("it is harshad num")
else:
    print("it is not harshad num")