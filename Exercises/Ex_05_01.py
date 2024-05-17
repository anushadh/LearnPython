count = 0
sum = 0
while (number != 'done'):
    number = input('Enter a number:')
    try:
        finalNumber = float(number)
        count = count + 1
        sum = sum + finalNumber
    except:
        print('Please enter a number')
print(sum, count, sum/count)