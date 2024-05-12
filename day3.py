def large() :
    print(max('hello'))

large()

def tiny() :
    print(min('hello'))
    
tiny()


def greet(language):
    if(language == 'English'):
        print('Hello')
    elif(language == 'Spanish'):
        print('Hola')
    else:
        print('!!!!')

greet('English')
greet('')

def greet(language):
    if(language == 'English'):
        return('Hello')
    elif(language == 'Spanish'):
        return('Hola')
    else:
        return('!!!!')

print(greet('English'), 'Anusha!')
print(greet('Spanish'), 'Anusha!')

def sum(a, b):
    return a+b

print(sum(100, 200))