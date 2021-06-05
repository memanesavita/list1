# Magic Square woh square hota hai jismei - har row ka, 
# har column ka, and dono diagonals ka sum same hota hai. 
# Aapko yeh program likhna hai - jo ek nested list leta hai, 
# aur dekhta hai ki woh magic square hai ya nahi? E.g. 
# Yeh magic square hai, kyuki
 
from typing import MappingView


magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 


i=0
while i<len(magic_square):
    j=0
    sum=0
    while j<len(magic_square[i]):
        sum=sum+(magic_square)[i][j]
        j=j+1
    i=i+1
    print(sum,end=" ")
print()
k=0
while k<len(magic_square):
    l=0
    sum1=0
    while l<len(magic_square[k]):
        sum1=sum1+(magic_square)[k][l]
        l=l+1
    print(sum1)
    k=k+1
m=0
while m<len(magic_square):
    p=0
    sum2=0
    while m<len(magic_square):
        if m==p:
            sum2=sum2+(magic_square)[m][p]
            p=p+1
        m=m+1
    print(sum2)
d=0
while d<len(magic_square):
    n=0
    sum3=0
    while n<len(magic_square):
        if d==n:
            sum3=sum3+(magic_square)[d][n]
            n=n+1
        d=d+1
    print(sum3)
        










        

    





    




















