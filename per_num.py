num=int(input("enter any num:"))
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i=i+1
print(sum)
if num==sum:
    print("it is perfect num")
else:
    print("it is not perfect num")

# num=(input("enter any bracket:"))
# true=1
# false=0
# i=1
# if (true):
#     print("it is true")
# elif (false):
#     print("it is false")

# i=1
# while i<9:
#     print(i)
