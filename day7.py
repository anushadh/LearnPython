str = 'banana'
indexLetter = str[2]
print('index letter:',indexLetter)

length = len(str)
print('Length:',length)

for letter in str:
    print(letter)

index = 0
while(length > 0):
    print(index, str[index])
    index = index + 1
    length = length - 1

countA = 0 
for letter in str:
    if(letter == 'a'):
        countA = countA + 1
print('Number of time letter a is repeated',countA)