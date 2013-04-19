from sys import exit

def start():
    print "You are in a room with three doors. Which one?"
    
    while True:
        choice = raw_input('> ')
        
        if '1' in choice:
            print "You go through the first."
            orange()
        elif '2' in choice:
            print "You go through the second."
            water_room()
        elif '3' in choice:
            print "You go through the third."
            third()
        else:
            print "I don't get it."




def orange():
    print "This is the first room. You can go back to the start, or continue through the door at the back."
    
    if ate_orange == False:
        orange_question()
    
    print "What do you want to do?"
    
    while True:    
        choice = raw_input('> ')

        if 'back' in choice or 'start' in choice:
            print "You do back to the start."
            start()
        elif 'continue' in choice or 'door' in choice:
            print "You continue through the door in the back."
            orange_end()
        else:
            print "I don't get it."

def orange_end():
    print "You find yourself in a room with a giant bear. What do you do?"
    choice = raw_input('> ')
    
    if 'run' in choice:
        print "You run."
        orange()    
    else:
        lose('The bear mauled your face off.')

def orange_question():
    print "There's tons of oranges in this room."
    print "Eat one?"
    choice = raw_input('> ')
    
    if 'yes' in choice:
        print "You eat an orange."
        global ate_orange
        ate_orange = True
    elif 'no' in choice:
        print "You decide not to."
    else:
        print "It's a yes or no answer."
        orange_question()

def water_room():
    print "You're in the water room."
    
    while pool_drained == False:
        pool_question()

    print "What do you do? Continue, or go back?"
    choice = raw_input('> ')

    while pool_drained == True:
        if 'back' in choice:
            print "You go back to the start."
            start()
        elif 'continue' in choice:
            print "You go to the next room."
            water_end()
        else:
            print "I don't get it."

def pool_question():
    print "A pool of water is in your way. What do you do?"
    choice = raw_input('> ')

    if 'jump' in choice:
        print "You jump over the pool."
        print "Pull the switch?"
        choice = raw_input('> ')
        
        if 'yes' in choice:
            print "The pool of water empties."
            global pool_drained
            pool_drained = True
        elif 'no' in choice:
            print "You decide not to."
            print "You continue through the door."
            water_end()
        else:
            print "I don't get it."
    elif 'swim' in choice:
        lose('You drown.')
    else:
        print "It looks like you can either jump or swim."

def water_end():
    print "This room is empty."
    print "You leave."
    water_room()

def win(reason):
    print reason, "You win!"
    exit(0)

def lose(reason):
    print reason, "You lose!"
    exit(0)

ate_orange = False
pool_drained = False

start()
