def isMyNumber(guess):
    x = 10
    if guess < x:
        return -1
        
    elif guess == x:
        return 0
        
    elif guess > x:
        return 1  
    
#ba = isMyNumber(8)
#print ba


def jumpAndBackpedal(isMyNumber):
    guess = 1
    if isMyNumber(guess) == 0:
        return guess
    
    else:
        foundNumber = False
        sign = isMyNumber(guess)
        while sign != 0:
            #sign = isMyNumber(guess)
            if sign == -1:
                print guess
                guess *= 2
                print guess
            elif sign == 1:
                print guess
                guess -= 1
                print guess
            sign = isMyNumber(guess)
    return guess
 
ba = jumpAndBackpedal(isMyNumber)
print ba
 
 
 #C:\701dddcc16d70d9036\ -installation media root mssqlserverexpress