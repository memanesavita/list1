# # Q: How to find all pairs in an array of integers whose sum is
# # equal to the given number?
# # Output: [[11,19], [12,18],[13,17]
 
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
a=[]
k=0
while i<len(n)/2:
    b=1
    while b<len(n):
        if n[i]+n[b]==number:
            k=([n[i],n[b]])
            a.append(k)
        b=b+1
    i=i+1
print(a)


    



 

