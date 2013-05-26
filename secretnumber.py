a = 99

go = 0
halt = 100
b = range(go,halt)


print 'Please think of a number between 0 and 100!'
guess = (go + halt)/2 # guess is assigned the average of the two end points
print 'Is your secret number' + str(guess) + '?'

feedback = '' #feedback is initially assigned empty string
while feedback != 'c':
	
	
	feedback = raw_input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low.Enter "c" to indicate I guessed correctly.' )
 
 #if-if else for different scenarios 
	if feedback == 'c':
		print 'Game over. Your secret number was: ' + str(guess)
	
	elif feedback == 'h':
		halt = guess #if guess is too high assign guess to the end-point of the range - halt and use for new guess
		guess = (go + halt)/2
		print 'Is your secret number' + str(guess) + '?'
		
	
	elif feedback == 'l':
		go = guess #if guess is too low assign guess to the start-point of the range - go and use for new guess
		guess = (go + halt)/2
		print 'Is your secret number' + str(guess) + '?'
		
	else:
		print 'Sorry, I did not understand your input.'
		print 'Is your secret number' + str(guess) + '?'
 
  
 

	
 