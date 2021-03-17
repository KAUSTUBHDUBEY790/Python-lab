a=int(input("Enter the year here "))
if a%4==0 and a%100!=0:
          print("The year is a leap year")
elif a%100==0:
          if a%400==0:
               print("The year is a leap year")

          else:
                    print("The year is a not leap year")
else:
          print("The year is not a leap year")
