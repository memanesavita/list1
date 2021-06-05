
# Aapko ek aisa program likhna hai jo, bataye, ki uppar wali list mei kitne log: Jaise, 
# uppar wali list ke liye aapka output hoga:
 
# 4 Crorepati hai
# 3 Lakhpati hai
# 4 Dilwale hai 


kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101,
532010, 510, 4100]
c=[]
l=[]
d=[]
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>=10000000:
        c.append(kitna_paisa_hai [i])
    elif kitna_paisa_hai[i]>=100000:
        l.append(kitna_paisa_hai [i])
    else:
        d.append(kitna_paisa_hai [i])
    i=i+1
print("Crorepati hai",c)
print("Lakhpati hai",l)
print("Dilwale hai",d)


    





        

    