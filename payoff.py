balance = 3329
annualInterestRate = 0.2
#monthlyInterestRate = float(annualInterestRate) / 12.0
previousBalance = float(balance)

#monthlyInterestRate = float(annualInterestRate) / 12.0
#monthlyUnpaidBalance = (previousBalance) - (minimumMonthlyPayment)
#updatedBalanceEachMonth = float(monthlyUnpaidBalance) + float(monthlyInterestRate * monthlyUnpaidBalance)
minimumMonthlyPayment = 10
totalPaid = 0
fiinalBalance = 0
month = 0
updatedBalanceEachMonth = 0
while (updatedBalanceEachMonth) > 0:
	minimumMonthlyPayment += 10
	previousBalance = float(balance)
	
	while month < 12:
		month += 1
		monthlyInterestRate = float(annualInterestRate) / 12.0
		monthlyUnpaidBalance = (previousBalance) - (minimumMonthlyPayment)
		updatedBalanceEachMonth = float(monthlyUnpaidBalance) + float(monthlyInterestRate * monthlyUnpaidBalance)
		previousBalance = updatedBalanceEachMonth
		
	minimumMonthlyPayment += 10
	previousBalance = float(balance)
	month = 0

print ('Lowest Payment: ' + str(float(minimumMonthlyPayment)))