num=int(input("enter any num:"))
sum=0
while num>0:
    a=num%10
    num=num//10
    sum=sum+a  
print(sum)
