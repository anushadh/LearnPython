def new_func():
    count = 0
    sum = 0
    number = 0
    while (number != 'done'):
        number = input('Enter a number:')
        try:
            finalNumber = float(number)
            count = count + 1
            sum = sum + finalNumber
        except:
            print('Please enter a number')
    print(sum, count, sum/count)
    return number

#number = new_func()


count = 0
sum = 0
iAmANumber = True
number = 0
while (iAmANumber):
    if(number == 'done'):
        break
    number = input('Enter a number:')
    try:
        finalNumber = float(number)
        count = count + 1
        sum = sum + finalNumber
    except:
        print('Please enter a number')
        continue
print(sum, count, sum/count)