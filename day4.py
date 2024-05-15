#while loop

x = 5
while (x > 0): 
    x = x - 1
    print('x is ', x)

x = 10
while (x < 0): 
    x = x - 1
    print('x is ', x)
print('I am done with while')    

#while loop with break
x = 9
while(x > 5):
    x = x - 1
    print('x is ', x)
    if(x < 8):
        break
print('I am done with while')

#while loop with continue
x = 9
while(x > 5):
    x = x - 1
    print('x is ', x)
    if(x < 8):
        continue
print('I am done with while')