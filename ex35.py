from sys import exit

def gold_room():
    print "\nThis room is full of gold. How much do you take?\n"
    
    choice = raw_input("> ")
    if int(choice) <=10000000:
        numchoice = int(choice)
    else:        
        print "Type a number. \n"
        gold_room()

    if numchoice < 50:
        print "You aren't greedy!"
        win()
    elif numchoice > 50:
        dead("You're greedy!")

def bear_room():

    while bear_moved == False:
        print """
There is a bear, sitting in front of a door.
Will You...
1. Run Away?
2. Attack it?
3. Negotiate with it?\n
        """
        choice = raw_input('> ')
        if '1' in choice or 'run' in choice:
            print "You run away."
            start()
        elif '2' in choice or 'attack' in choice:
            print "You attack it!"
            dead('Bad idea.')
        elif '3' in choice or 'negotiate' in choice:
            print "You try to negotiate with the bear..."
            print "The bear agrees to move!"
            global bear_moved
            bear_moved = True
        else:
            error()

    while bear_moved == True:
        print "The bear isn't a problem anymore. Will you go to the next room, or back to the start?"
        choice = raw_input('> ')
        if 'start' in choice:
            start()
        elif 'next' in choice:
            gold_room()
        else:
            error()
            

def dead(reason):
    print reason, "Game Over."
    exit(0)

def start():
    print "\nYou are in a room with two doors. Which one?\n"
    choice = raw_input('> ')
    if 'first' in choice or '1' in choice:
        bear_room()
    elif 'second' in choice or '2' in choice:
        cthulu_room()
    else:
        print "Choose a door to go through."
        start()

def cthulu_room():
    print "\nYou have entered the room of Cthulu."
    print "What do you do?\n"
    choice = raw_input('> ')

    if 'leave' in choice:
        print "You leave.\n"
        start()
    else:
        dead('You go insane.')

def win():
    print "\nYou win! Congradulations!\n"
    exit(0)

def error():
    print "I don't get it."

bear_moved = False

start()
