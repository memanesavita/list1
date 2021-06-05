# palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai.
# Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai.
# Aise hi MOM bhi ek palindrome hai.
# Code likho jo check kare ki kya list palindrome hai ya nahi.
# Aur print karo “Haan! palindrome hai” agar hai.
# Aur “nahi! Palindrome nahi hai” agar nahi hai.
# Abhi ke liye iss list ko use kar ke code likh sakte ho:
 
name=[ 'n', 'i', 't', 'i', 'n' ] 
a=[]
i=1
while i<=len(name):
    a.append(name[-i])
    i=i+1
print(a)
if a==name:
    print("palindrome")
else:
    print("not palindrome")

  















# a=input("enter the letter")
# b=a[-1::-1]
# if(a==b):
#     print("palindrom sring")
# else:
#     print("not palindrom sring")











# i=1
# while i<=10:
#     if i==5:
#         print()
#         i=i+1
#         continue
#     print(i)
#     i=i+1




# i=1
# while i<=10:
#     if i==5:
#         break
#     print (i)
#     i=i+1



