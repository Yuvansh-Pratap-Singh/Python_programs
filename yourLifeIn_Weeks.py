age = int(input("Enter your age : "))
years_remaining = 90 - age
days_remaining = years_remaining * 365
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months, {years_remaining} years left."
print(message)