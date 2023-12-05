x=int(input("enter the number of years: "))
i=0
total_months=x*12
total_temp=0
average_monthlytemp=0
average_yearlytemp=0

while (i<=total_months):
    y=int(input("highest temperature for"*i," :"))
    i=i+1
total_temp=total_temp+y
average_monthlytemp=total_temp/total_months
average_yearlytemp=total_temp/x
print("total temperature for each month is: ",total_temp)
print("average highest temperature for month is: ",average_monthlytemp)
print("average highest temperature for year is: ",average_yearlytemp)