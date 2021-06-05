# Code likho jo iss list mein se second maximum element 
# (doosra sabse bada element) dhund kar kar print kare.
 
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]


i=0
while i<len(numbers):
    a=numbers[i]
    if a>numbers[0]and a<numbers[3]:
        print("second max",[a])
    i=i+1
