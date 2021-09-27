players=['Blay','Prince','Elijah','Richmond','Cornelius','Bofa','Amartey','David','Henry']
random_activities=['Blanket','Bread','Stairs','Tablet','Shoes','Grass','Ice-cream','Fire Truck','Chair','Laptop','Pillow','Airplane','Guitar','Drums','Washing the Dishes','Fishing','Zoo','Sharpening a pencil','Ballet dancing','Playing pool/billiards','Shooting a bow and arrow','Music conductor','Michael Jackson Dancing','Driving a car','Applying lotion','Running/jogging','Chicken','Monkey','Cat','Dog','Brushing teeth','Taking a bath/shower','Combing/brushing hair']
print("""Welcome to today's game night
The game for today is pick and act.
In this game, a random player is selected to perform an activity.
The audience is to guess the activity.
The following are the rules!
When acting an activity, the player is not allowed to talk.
To quit the game, Input:Quit""")
code_breaker=str('quit')
response=input('Are we okay with the rules? ')
correct_response=['Yes','yes','Yes ','yes ',' Yes',' yes','Yeah','yeah',' Yeah','Yeah ','yeah ','y ','Y','y']
emoji_1=chr(9786)
emoji_2=chr(9787)
if response in correct_response:
    for i in range(100):

        print("Now that we are clear with the rules, let's proceede.")
        print("Let's see who will go first!{}" . format(emoji_1))
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
        import random
        player=random.choice(players)
        print()
        print("Let's start from {} {}" .format(player,emoji_2))
        import random
        activity=random.choice(random_activities)
        print("You're activity is '{}'" .format(activity))
        print('You have 30 seconds to act it out.')
        import time
        def countdown(t):

            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
        t = 15

        countdown(int(t))
        print()
        print("I hope they picked your act right?")
        reply=input()
        if reply in correct_response:
            print("Great. Let's move on to the next player")
        if reply==code_breaker:
            print("I guess we're done for the day")
            print('Thanks for playing.')
            break

else:
    print("Okay then come let's play later!!")
