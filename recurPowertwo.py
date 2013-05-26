def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    
    if ((exp%2) == 0 and exp > 0):
        return (exp/2) * base + recurPowerNew(base,exp) + (m/2)*n
    elif ((exp > 0) and (exp%2 != 0)):
        return (exp - 1) * recurPowerNew(base, exp-1)
    elif exp == 0:
        return 1
		
		
a = recurPowerNew(2, 9)

print a