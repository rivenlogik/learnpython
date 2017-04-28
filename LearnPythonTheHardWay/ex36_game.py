from sys import exit
#  MAP DETAILS
#          ______
#  ______| Alli   |________________
# | Bear | Start  | forest | Gold |
#        | Desert | Kerb   | Death|
#        | Cthulu |
#
# Practice coding from Learn python the hard way (exercise 36)

### ROOMS ###
# The alligator room is the top room in the map
def alligator_room():
    print "This room has an alligator in a swamp.  He eyes you suspiciously."
    print "What do you do?  (taunt, run, attack)"

    choice = raw_input("> ")
    if choice == "taunt":
        dead("The alligator bit your face off, better luck next time!")
    elif choice == "run":
        print "You run away, sissy."
        startroom()
    elif choice == "attack":
        dead("You attack the alligator, he eats your face off.")
    else:
        dead('While contemplating what to do, the alligator attacked and ' \
         'ate your genitals.')

# The gold room is the end of the game.
def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

# The bear room is usually death.
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "What do you want to do?  (taunt bear, take honey, run)"

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear":
            dead("The bear claws your face off.")
        elif choice == "run":
            print 'The bear gets pissed and charges after you, and you barely ' \
            'escape to whence you came.'
            startroom()
        else:
            print "I got no idea what that means."

# The forest room contains a puzzle.
def forest_room():
    print """You find yourself in an expansive forest. \
It is dark. You hear birds chirping in the distance.\n
Ahead of you is a door with three symbols lit by the moon. \
On the door it reads: \'My tale is silent without nightvision.\'\n
There are 3 symbols that look like they need to be placed in order. \
An owl, a whale, and a mouse"""
    print "There is also a doorway to your right."
    print "What do you want to do? (play, right, run)"

    choice = raw_input("> ")
    if choice == "run":
        print "You exit back whence you came."
        startroom()
    elif choice == "right":
        kerberos_room()
    elif choice == "play":
        print """Choose the appropriate order for the symbols by \
typing the numbers in order
\t 1 - owl
\t 2 - whale
\t 3 - mouse
ie. 123 or 321 or 213
"""
        firedeath = 0
        while True:
            if firedeath > 1:
                dead("You burst into flames.")
            gamechoice = raw_input("> ")
            if gamechoice == "123" or gamechoice == "321":
                    print "A fire flares above the door."
                    firedeath += 1
            elif gamechoice == "213":
                print "The door opens and you enter."
                gold_room()
            else:
                dead("A fire ignites above the door and engulfs you.")
    else:
        dead("A fire ignites above the door and engulfs you.")

# The desert room can be deadly if you linger
def desert_room():
    print "You enter a vast dry desert with the sun in the distance."
    print "There seems to be water to your right in an oasis."
    print "To your left and front of you there are doorways."
    print "What do you do? (drink, front, left)"

    drank = 0
    while True:
        choice = raw_input("> ")
        if drank > 2:
            dead("You die of dysentery.")
        if choice == "drink":
            drank += 1
            print "The water is cold and soothing."
        elif choice == "front":
            cthulu_room()
        elif choice == "left":
            kerberos_room()
        else:
            dead("The sun beats down on you and you die of thirst.")

# The cthulu room causes insanity
def cthulu_room():
    print "Here, you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head? (flee, head)"

    choice = raw_input("> ")

    if "flee" in choice:
        desert_room()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()

# The Kerberos room has a dog with 3 heads, rock it out!
def kerberos_room():
    def choose_room():
        print "Will you take door 1 or 2?"

        choice = raw_input("> ")

        if choice == "1":
            forest_room()
        elif choice == "2":
            death_room()
        else:
            dead("Kerberos grew tired with your indecision and smashed you.")

    print "You enter a room with the mythical dog Kerberos guarding two doors."
    print "It looks at you, pumping one paw in the air."
    print "Quick! You see a guitar next to the door you came in from."
    print "What style do you play? (death, doom, core, black, thrash)"

    choice = raw_input("> ")

    if choice == "black":
        print "Pleased with your life choices, he moves out of your way."
        choose_room()
    elif choice == "core":
        dead("Kerberos looks happy, but quickly realizes what you're " \
        "playing is total shit and he hates breakdowns.  He breaks your neck.")
    elif choice == "doom":
        print "Kerberos falls asleep, what is this shit? Slower than Ahab?"
        choose_room()
    elif choice == "death":
        dead("Kerberos forms a mosh pit with you under him.")
    elif choice == "thrash":
        print "Kerberos reminds you this is post 1990 and kicks you back in" \
        "time to the start of the game where you belong."
        startroom()

def death_room():
    print "You enter a room with death standing in front of you."
    print "He is pointing at you, then at the door to his right."
    print "What do you do? (attack, run, pray)"

    choice = raw_input("> ")

    if choice == "attack":
        dead("Death laughs, and touches you.")
    elif choice == "run":
        kerberos_room()
    elif choice == "pray":
        print "Death looks confused, wondering what you're doing."
        dead("He touches you anyway.")
    else:
        print "%s is not a bad idea, but..." % choice
        dead("Death touches you.")

def dead(why):
    print why, "Good job! You\'re dead."
    exit(0)

def startroom():
    print "You are in a dark room."
    print "There are doors on your left and right, front and back."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        forest_room()
    elif choice == "front":
        alligator_room()
    elif choice == "back":
        desert_room()
    else:
        dead("You stumble around the room until you starve.")

startroom()
