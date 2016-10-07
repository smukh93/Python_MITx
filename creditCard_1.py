"""" Write a program to calculate the credit card balance 
after one year if a person only pays the minimum monthly payment 
required by the credit card company each month.The following variables
 contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal
For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. 
Be sure to print out no more than two decimal digits of accuracy. """

def monthlyDebtCalculator(pb, mir, mmpr):
    mmp = mmpr * pb
    mub = pb - mmp
    ub_m = mub+(mir*mub)
    return round(ub_m,2)
    
def debtPay(balance,air,mmpr):
    mir = air/12.0
    pb = balance
    for x in range(0,12):
        new_pb = (monthlyDebtCalculator(pb,mir,mmpr))
        #print("Month" + str(x+1) + " , balance: " + str(new_pb))
        pb = new_pb
    print("Remaining Balance: " + str(new_pb))

debtPay(484,0.2,0.04)
   
    