#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

balance = 3329
annualInterestRate = 0.2
#monthlyInterestRate = float(annualInterestRate) / 12.0
previousBalance = float(balance)

#monthlyInterestRate = float(annualInterestRate) / 12.0
#monthlyUnpaidBalance = (previousBalance) - (minimumMonthlyPayment)
#updatedBalanceEachMonth = float(monthlyUnpaidBalance) + float(monthlyInterestRate * monthlyUnpaidBalance)
minimumMonthlyPayment = 10
month = 0
totalmonthly = 0
while totalmonthly < balance:	
	
	for month in range(12):
		#minimumMonthlyPayment += 10
		monthlyInterestRate = float(annualInterestRate) / 12.0
		monthlyUnpaidBalance = (previousBalance) - (minimumMonthlyPayment)
		updatedBalanceEachMonth = float(monthlyUnpaidBalance) + float(monthlyInterestRate * monthlyUnpaidBalance)
		previousBalance = updatedBalanceEachMonth - minimumMonthlyPayment
	
	if (totalmonthly > balance):
		minimumMonthlyPayment = minimumMonthlyPayment 
		break
	else:
		minimumMonthlyPayment += 10
		previousBalance = balance
	
	
		
	totalmonthly += minimumMonthlyPayment
print ('Lowest Payment: ' + str(float(minimumMonthlyPayment)))
print ('UpdatedBalance: ' + str(float(previousBalance)))
print str(totalmonthly)
#print str(count)
