x=int(input("enter the number of years: "))
i=1
a=0

total_months=x*12
total_temp=0
average_monthlytemp=0
average_yearlytemp=0

while (i<=x):
    i=1
    while(i<=12):
         y=float(input(f"for month {i} :",))
         i=i+1  
    if (a<y):
        a=y   
    print ("highest temperature",a)

    
   

total_temp=total_temp+y
average_monthlytemp=total_temp/total_months
average_yearlytemp=total_temp/x
print("total temperature for each month is: ",total_temp)
print("average highest temperature for month is: ",average_monthlytemp)
print("average highest temperature for year is: ",average_yearlytemp)