

# Ek code likho jo kissi bhi list ke liye uss list ke do sum ka output karta hai, 
# ki uss list mei odd numbers ka sum aur even numbers ka sum kitna hai.
 

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
c=0
i=0
c1=0
sum=0
sum1=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        print(elements[i],"it is even")
        c=c+1  
    else:
        sum1=sum1+elements[i]
        c1=c1+1
        print(elements[i],"it is odd")
    i+=1
print("even number.:",c,sum)
print("odd number.:",c1,sum1) 


    

