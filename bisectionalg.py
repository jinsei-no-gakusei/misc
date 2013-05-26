#new


balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = float((annualInterestRate) / 12.0)
monthlyPaymentLowerBound = float(balance / 12)
monthlyPaymentUpperBound = float((balance * (1 + monthlyInterestRate)**12)) / 12.0

minMonthly = float((monthlyPaymentLowerBound + monthlyPaymentUpperBound))/2.0 


totalminMonthly = 0.0
while abs(totalminMonthly - monthlyPaymentUpperBound) >= 0.01:
	
	print str(minMonthly)
	
	month = 1		
	while month <= 12:
				
		if minMonthly < monthlyPaymentUpperBound:
			monthlyPaymentUpperBound = minMonthly
			print str(monthlyPaymentUpperBound)
		
			#minMonthly = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2  #32517.09
	
		if minMonthly > monthlyPaymentLowerBound:
			monthlyPaymentLowerBound = minMonthly
			print str(monthlyPaymentLowerBound)
			 #28616
			#print ('The minMonthly at this final point is:') + str(minMonthly)
			
			
			minMonthly = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2
			print str(minMonthly)
		if month > 12:
			month = 1
			minMonthly = (monthlyPaymentLowerBound + monthlyPaymentUpperBound)/2
		
print ('Lowest amount') + str(minMonthly)