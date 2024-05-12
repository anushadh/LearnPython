x = 0
if x <= 5 :
    print('I am less than 5')
elif x == 5 :
    print('I am 5')
else:
    print('I am greater than 5')


myName = 'Anusha'
try :
    intName = int(myName)
    print('in try')
except : 
    intName = 0
    print('in except')

    
print(intName)

myName = '99'
try :
    intName = int(myName)
    print('in try')
except : 
    intName = 0
    print('in except')
print(intName)

inputValue = input('Enter a number: ')
try :
    finalValue = int(inputValue)
except :
    finalValue = 0

if finalValue > 0 :
    print('Good!')
else :
    print('You did not enter a number :(')