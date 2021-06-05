
# Occurences - occur shabd se bana hai, jiska matlab hota hai, ki kitni baar aata hai. Sample List
 
# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"] 

# Sample List ka Output:
 
# [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]

# a - 6 times
# n - 3 times
# t - 2 times
# x - 2 times
# u - 1 times
# g - 1 times 

# Humei char_list mei jo bhi characters hai, unki occurences count karni hai, 
# aur ek nested list mei save karni hai,
#  phir uss nested list ko use kar kar jo output hai, woh print karna hai.

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
b=[]
while i<len(char_list):
    j=0
    k=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    k.append(char_list[i])
    k.append (count)
    if k not in b:
        b.append (k)
    i=i+1
print(b)


            

        


        






