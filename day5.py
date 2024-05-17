#for loops

for i in [1, 2, 3]:
    print(i)
print('I am done')
    
friends = ['M', 'A', 'S']
for friend in friends:
    print(friend)
    
# find the largest number in the loop
numbers = [3, 41, 12, 9, 74, 15]
largest = 0
for number in numbers:
    if (number > largest):
        largest = number
print('Largest: ', largest)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)