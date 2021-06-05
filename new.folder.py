

a=int(input("enter the number"))
b=str(a)
l=len(b)
s=l-1
i=0
while i<len(b):
    c=int(b[i])
    n=(c)*10**s
    print(n,end=" ")
    if n!=len(b)-1:
        print("+",end=" ")
        i=i+1
        s=s-1



# a=int(input("enter the number :"))
# b=str(a)
# l=len(b)
# t=l-1
# i=0
# while i<len(b):
#     savita=int(b[i])
#     num=(savita)*10**t
#     print(num,end=" ")
#     if i!=len(b)-1:
#         print("+",end=" ")
#     i=i+1
#     t=t-1