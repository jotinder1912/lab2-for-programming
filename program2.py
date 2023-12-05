diet_calorie=int(input("Enter daily calorie intake: "))
days=int(input("enter the number of days: "))
average_intake=int(input(" Enter average daily percentage increase/decrease.{}(if decrease,enter the value in negative): ") )
i=1
if average_intake>0 or average_intake==0:
    while(i<=days):
        if (diet_calorie>=1200):
            print(f"days{i}:",diet_calorie)
            diet_calorie=diet_calorie+(diet_calorie*(average_intake/100)) 
            i=i+1                         
        else:
            
            print(" ")
            break


else:
    while(i<=days):
        if (diet_calorie>=1200):
           print(f"days{1}: ",diet_calorie)
           diet_calorie=diet_calorie-(diet_calorie*(average_intake/100))
           i=i+1
        else:
          print("")
          break