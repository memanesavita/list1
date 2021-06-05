# Ek code likho jo kisi bhi list ke liye yeh output karta hai,
#  ki uss list mei kitne odd numbers hai aur kitne even numbers hai.
 
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
c=0
i=0
c1=0
sum=0
while i<len(elements):
    if elements[i]%2==0:
        print(elements[i],"it is even")
        c+=1   
    else:
        c1=c1+1
        print(elements[i],"it is odd")
    i+=1
print("even number.:",c)
print("odd number.:",c1)
print()

    
