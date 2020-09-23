i = 34
count = 0
print('Welcome to NUMBER GUESSING game')
print('You have only 5 chances to guess the number')
print('The number is two digits\n')
while True:
    n = int(input('Enter a number:'))
    count += 1

    if count == 5:
        print('You lost!!! Better Luck Next Time')
        break
    if n == i:
        print('You Won!!!')
        break
    elif 30 < n < 40:
        print('You are close to answer')
    elif count == 4:
        print('Last guess remaining')
    elif n < i:
        print('Please increase your number')
    elif n > i:
        print('Please decrease your number')

