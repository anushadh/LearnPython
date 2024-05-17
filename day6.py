count = 0
for item in [1, 2, 3, 4, 5]:
    count = count + 1
print(count)

count = 0
for item in [1, 2, 3, 4, 5]:
    count = count + item
print(count)

for item in [1, 2, 3, 4, 5]:
    if(item > 3):
        print("I am greater than 3",item)
 
iAm5 = False       
for item in [1, 2, 3, 4, 5]:
    if(item == 5):
        iAm5 = True
        print("I am 5",iAm5)
