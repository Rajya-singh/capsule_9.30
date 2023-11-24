i= int(input('enter a number: '))
orig=i # store the original number
sum=0  # initaialize sum to 0
while(i>0):
    sum=sum+(i%10)**3
    i=i//10
if sum==orig:
    print('armstrong')
else:
    print('not armstorng')