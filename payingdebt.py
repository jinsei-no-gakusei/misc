balance = 3329
annualInterestRate = 0.2
#monthlyInterestRate = float(annualInterestRate) / 12.0
previousBalance = float(balance)


minimumMonthlyPayment = 0
#print str(previousBalance)
month = 1
while month <= 12:
	
	#gravy
	monthlyInterestRate = float(annualInterestRate) / 12.0
	monthlyUnpaidBalance = (previousBalance) - (minimumMonthlyPayment)		
	updatedBalanceEachMonth = float(monthlyUnpaidBalance) + float(monthlyInterestRate * monthlyUnpaidBalance)
	previousBalance = updatedBalanceEachMonth
	
	if (previousBalance <= 0):
		break
		
		
	#gravy
	month += 1
	if month > 12:
		month = 1
		minimumMonthlyPayment += 10
		previousBalance = balance
	
	
	
print ('Lowest Payment: ' + str(float(minimumMonthlyPayment)))
print ('UpdatedBalance: ' + str(float(previousBalance))
































