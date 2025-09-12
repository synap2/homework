# q4 print the sum of all odd numbers from a given number from 1
total = 0
num = input( ' give me a number ')
num = int(num)
for i in range(num):
    if i%2 != 0:
        total=total+i
print(total)