
balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = (annualInterestRate) / 12.0
previousBalance =balance
monthlyPaymentLowerBound = (previousBalance / 12.0)
monthlyPaymentUpperBound = (previousBalance * (1 + monthlyInterestRate)**12) / 12.0
Balance1 = balance
Balance2 = 0

#this is your guess
minimumMonthly = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2

#month = 1
#while month <= 12:

while abs(Balance1 - Balance2) > .1:
    Balance2 = Balance1    
    Balance1 = previousBalance 
    count = 1

    while count < 13:
        Balance1 = (Balance1 - minimumMonthly) * (1 + monthlyInterestRate)
        count += 1

    if Balance1 > 0:
        monthlyPaymentLowerBound = minimumMonthly
    if Balance1 < 0:
        monthlyPaymentUpperBound = minimumMonthly

    minimumMonthly = round(((monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2),2)
    

    #print(Balance1)
    #print(Balance2)
    

print ('Lowest Payment: ' + str(float(minimumMonthly)))


