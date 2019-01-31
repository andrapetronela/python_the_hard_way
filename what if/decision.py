print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input('> ')

if door == '1':
    print("""There is a wolf eating a banana here.
    What do you do?
    1. Take the banana.
    2. Start talking with it.""")
    
    wolf = input('> ')
    
    if wolf == 1:
        print('That\'t great! The wolf has eaten your arm.')
    elif wolf == 2: 
        print('You do know how to discuss with animals.')
    else: 
        print(f'Well, doing {wolf} is probably better. The wolf runs away.')
        
elif door == '2':
    print("""You have found a jar full of honey, but a giant bear is looking at your. What do you do?
    1. Hit the bear with the jar.
    2. Open the jar and offer it to your new frind.""")
    
    jar = input('> ')
    
    if jar == '1':
        print('You should\'ve tried this before with a ball. Now, the bear is angry.')
    elif jar == '2':
        print('You are so kind! The bear is now really happy and will eat you after he finishes the honey.')
    else:
        print(f'You should be right here. There is only {jar} left to do.')

else:
    print('You don\'t have the adventure spirit required and we think you are not ready to be part of our team. You should go home at your toys.')
    