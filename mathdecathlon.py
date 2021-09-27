name=input('Enter your name to costomize your personal Maths quiz decathlon:')
print(name,"""'s Maths quiz decathlon
Answer as many questions as possible to attain the maximum points""")
print('''USERS MANUAL
OPERATORS:
    + ==- ADDITION
    - ==- SUBSTRACTION
    x ==- MULTIPLICATION
    / ==- DIVISION''')
respond=input('Are you ready to do some Maths?(Yes or No):')
correct_response=['Yes','yes','Yes ','yes ',' Yes',' yes']
score_sheet=0

if respond in correct_response:
    print("Let's get our Maths pants on!")
    print('Test begins after countdown')
    import time
    def countdown(t):

        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
    t = 3

    countdown(int(t))
    emoji=chr(9786)
    for i in range(10):
        import random
        num_1=random.randint(-100,100)
        num_2=random.randint(1,10)
        import random
        list_of_operators=['plus','minus','multiplied by','divided by']
        operator=random.choice(list_of_operators)
        print('Compute ({}) {} ({})' .format(num_1,operator,num_2))
        if operator==list_of_operators[0]:
            answer_1=num_1+num_2
            user_reply=int(input('Enter your answer here:'))

        if operator==list_of_operators[1]:
            answer_1=num_1-num_2
            user_reply=int(input('Enter your answer here:'))

        elif operator==list_of_operators[2]:
            answer_1=num_1*num_2
            user_reply=int(input('Enter your answer here:'))

        elif operator==list_of_operators[3]:
            answer_2=num_1/num_2
            answer_1=round(answer_2, 2)
            user_reply=float(input('Enter your answer here:'))
        if answer_1==user_reply:
            score_sheet=score_sheet+10
            print("Excellent job!.You're a genius")
            #for i in range(10):
            print('You have {} points!' .format(score_sheet))
        else:

            print('That is incorrect!')
            print('The right answer is',answer_1)
            print("You've failed the math quiz decathlon.")
            print('Try again later!')
            print('Your final score is {} {}' .format(score_sheet,emoji))
            break

else:
    print("Let's try again some other time")
