import random
char = ['1','2','3','4','5','6','7','8','9','0',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','R','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
        '!','?','#','%']
print('Welcome to the Password Generator, please type generate to begin')
print('Please note that the password is 10 character long')
print('Please type cancel to cancel')
start = str(input(''))
if start == 'generate':
    pn1 = random.choice(char)
    pn2 = random.choice(char)
    pn3 = random.choice(char)
    pn4 = random.choice(char)
    pn5 = random.choice(char)
    pn6 = random.choice(char)
    pn7 = random.choice(char)
    pn8 = random.choice(char)
    pn9 = random.choice(char)
    pn10 = random.choice(char)
    password = [pn1,pn2,pn3,pn4,pn5,pn6,pn7,pn8,pn9,pn10]
    final = ''.join(password)
    print('Your code is :',final)
    print('Thank you, have a nice day')
    print('Do remember to save the password!')
elif start == 'cancel':
    print('Generator cancelled, have a nice day')
else:
    print('Invalid input. Please try again')

