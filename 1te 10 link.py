# Write a Python program to find the difference between elements 
# (n+1th - nth) of a given list of numeric values
# Original list:
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Dfference between elements (n+1th - nth) of the said list :
# x=[1, 1, 1, 1, 1, 1, 1, 1, 1]
# Original list:
# [2, 4, 6, 8]
# Dfference between elements (n+1th - nth) of the said list :
# [2, 2, 2]





i=1
y=[]
while i<len(x):
    z=x[0]
    y.append(z*1)
    i=i+1
print(y)