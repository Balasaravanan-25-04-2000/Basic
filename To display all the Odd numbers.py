#To display all the Odd numbers starting from an assigned number
y = int(input('Enter a number:'))
if y % 2 == 0:
 x = range(y+1, 100, 2)
else:
 x = range(y, 100, 2)
x = list(x)
print(x)
#Output:Enter a number:87
#[87, 89, 91, 93, 95, 97, 99]
