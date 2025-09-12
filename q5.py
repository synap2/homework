#q5 adrian print the multiplication table for a given number

number = input ('give me a number')
number = int(number)
for i in range (1, 13):
    print(number, 'x', i, '=', number*i)