def collatz(num):
    if num % 2 == 0:
        return num//2
    else:
        return 3*num+1

print('Type in a number:')
number = input()
try:
    number = int(number)
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('Needs to be an integer')

    
