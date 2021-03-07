print("Welcome to the simple tip calculator.")
bill = float(input("What is the total bill? "))
tip = int(input("What tip percentage do you want to give? 10, 12 or 15? "))
while tip != 10 and tip != 12 and tip != 15:
	tip = int(input("Please choose between 10, 12 and 15: "))
people = int(input("How many people are you? "))
individual_bill = (bill + bill*tip/100) / people
individual_bill = round(individual_bill, 2)
print(f"Each of you should pay {individual_bill} euroes")