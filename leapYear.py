print("Check Leap year or not !!")
year = int(input("Which year do you want to check : "))

if year%4==0 and year%100!=0 or year%400==0 :
        print("Given year is a Leap Year")
else:
    print("Given year is not a leap Year")        