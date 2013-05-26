#num = raw_input('type number > :' )
num = 256
if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''	
if num == 0:
    result = "0"
while num > 0:
    result = str(num%2) + result
    #print result
    num = num/2
    print result
    
if isNeg:
    result = '-' + result