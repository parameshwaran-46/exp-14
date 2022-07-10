str1=input("enter your string: ")
k=0
for i in range(len(str1)-1):
    if "Hi"==str1[i:i+2]:
        k=k+1
print(k)