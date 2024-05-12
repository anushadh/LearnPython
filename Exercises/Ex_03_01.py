hours = input('Enter your work hours: ')
finalHours = float(hours)
payRate = input('Enter your pay rate per hour: ')
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