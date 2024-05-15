print('*welcome to dice')
your_score = 0
cpu_score = 0
while True:
    import random
    user_choice =computer_choice = random.randint(1,6)
    
    
    import random
    computer_choice = random.randint(1,6)
    print()
    print('your choice',user_choice) 
    print('cpu_choice:',computer_choice)
    print()
    if computer_choice > user_choice:
        print('you lost')
        cpu_score+=1
    elif computer_choice < user_choice:
        print('you win')
        your_score+=1
    elif computer_choice == user_choice:
        print('its a tie')
    print('your_score:',your_score)
    print('computer score',cpu_score)
    print()
    repeat = input("play again?: (Y/N):").lower()
    while repeat != 'n' and repeat != 'y':
            repeat = input('invalid input! try again!').lower()
    if repeat == 'n':
                print ('thank you')
                break
    print('\n------------\n')
