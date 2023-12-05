myNumbers=[4,6,9,44,17,27,22,33,12]
print("Elements of myNumbers list:")
i=0
k=0
while(k<=8):
    for i in range(0,8):
        if(i<8):
            if(myNumbers[i]>myNumbers[i+1]):
                c=myNumbers[i]
                myNumbers[i]=myNumbers[i+1]
                myNumbers[i+1]=c
        i=i+1
    k=k+1


print("\nSorted myNumbers list:")
print(myNumbers)

