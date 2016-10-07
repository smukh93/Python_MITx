def fun(balance, annualInterestRate):    
    fixedPay = balance / 120 * 10
    monthlyInterest = annualInterestRate / 12
    debt = balance # use a initial variable to store start input balue
    # and keep refresh debt value every time
    while debt > 0:
        debt = balance # replace debt value after inner for loop       
        for i in range(1,13): # use two layer loop to control 
            debt -= fixedPay
            if debt <= 0: # set a condition to return fixedPay value
                return fixedPay 
            debt *= (monthlyInterest + 1)
            print ('month :' + str(i))
            print ('monthly payment: ' + str(fixedPay))
            print ('debt :' + str(debt))
            print ('\n')
        fixedPay += 10 #test condition to continue

balance = 4773
annualInterestRate = 0.2

print ('Lowest Payment: '+ str(fun(balance, annualInterestRate)))
