# monthlyInterestrate = Annual interest rate / 12
#minimumMonthlypayment = minimum monthly payment rate * previous balance
#monthlyUnpaidbalance = (previousBalance) - (minimumMonthlypayment)
#updatedBalanceeachmonth = (monthlyUnpaidbalance) + (monthlyInterestrate * monthlyUnpaidbalance)

#balance = outstanding balance on the credit card
#annualInterestrate - annualInterestrate as a decimal
#monthlyPaymentrate - minimum monthly payment rate as a decimal

balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

#bind variables
minimumMonthlyPaymentRate = float(monthlyPaymentRate)
previousBalance = float(balance)
monthlyInterestRate = float(annualInterestRate) / 12
minimumMonthlyPayment = float(minimumMonthlyPaymentRate) * float(previousBalance)
monthlyUnpaidBalance = float(previousBalance) - float(minimumMonthlyPayment)
updatedBalanceEachMonth = float(monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)
totalPaid = 0
fiinalBalance = 0
month = 0
while month < 12:
	month += 1
	minimumMonthlyPayment = float(minimumMonthlyPaymentRate) * float(previousBalance)
	monthlyUnpaidBalance = float(previousBalance) - float(minimumMonthlyPayment)
	updatedBalanceEachMonth = float(monthlyUnpaidBalance) + (monthlyInterestRate * monthlyUnpaidBalance)

	print ('Month: ' + str(month))
	print ('Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2)))
	print ('Remaining balance: ' + str(round(updatedBalanceEachMonth,2)))
	previousBalance = updatedBalanceEachMonth
	
	totalPaid += float(minimumMonthlyPayment)
	finalBalance = float(previousBalance)
print ('Total paid: ' + str(round(totalPaid,2)))
print (('Remaining balance: ' + str(round(finalBalance,2))))