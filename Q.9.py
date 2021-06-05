# Ek code likho jo kisi bhi list ke liye yeh output karta hai,
# ki uss list mei odd numbers, even numbers aur sab numbers ka: - count
# sum
# average

# print aaye.
# Sample Input
 
# Sample Output

# odd numbers ka count .... hai even numbers ka count .... 
# hai saare numbers ka count .... hai odd numbers ka sum ....
# hai even numbers ka sum .... hai saare numbers ka sum .... 
# hai odd numbers ka average .... hai even numbers ka average ....
# hai saare numbers ka average .... hai


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]  
c=0
i=0
c1=0
sum=0
sum1=0
count=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        print(elements[i],"it is even")
        count=count+elements[i]
        c=c+1  
    else:
        sum1=sum1+elements[i]
        c1=c1+1
        print(elements[i],"it is odd")
    i+=1
avrg=sum/4
avg=sum1/7
print("even number. count:",c, "/" "sum of even",sum,  "/"   "avrge even :",avrg)
print("odd number.count.:",c1,  "/" "sum of odd",  sum1, "/"   "avg odd:",avg)







    


