

n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 

# iss lists mei se duplicates nikal kar,
# kisi aur list mei daal kar print karne hai.

i=0
k=[]
while i<len(n):
    if n[i]>1:
        if n[i] not in k:
            k.append(n[i])
        i=i+1
print(k)








        

        







