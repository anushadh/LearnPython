def computepay(hours, payRate):
    try :
        finalHours = float(hours)
        finalPayRate = float(payRate)
        if finalHours > 0 :
            if finalHours > 40 :
                extraHours = finalHours - 40
                wageReg = (finalHours - extraHours) * finalPayRate
                wageExtra = extraHours * 1.5 * finalPayRate
                wage = wageReg + wageExtra
                print('You got Bonus rate!')
            elif finalHours <= 40 :
                wage = finalHours * finalPayRate
        else :
            print('Hours are not valid!')

        print('Here is your wage:', wage)
    except :
        print('Enter a numeric number, please!')
        
computepay(50, 10)
    

