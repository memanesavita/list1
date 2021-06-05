# iss program mei humein agar koi number binary form mei diya gaya hai,
#  toh hum uski decimal form nikalna seekhenge.
# content

# Jaise yeh diagram dekho.
 
binary_number = [1, 0, 0, 1, 1, 0, 1, 1] 

i=0
sum=0
while i<len(binary_number):
    a=binary_number[len(binary_number)-i-1]
    sum=sum+a*(2**i)
    i=i+1
print(sum)

