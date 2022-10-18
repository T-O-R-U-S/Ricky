import lib
import random

from lib import *
from map import station_map
from art.station import draw_station
from art.animations import vent_animation, ricky_animation, move_animation, clone_encounter

def story():
    show("The year is 2078")
    show(" ", delay=0.5)
    line_print("You are in a space shuttle. ")
    sleep(1)
    show("Your good friend, Gun Lover Ricky, has gone insane. He's now shooting up the place.\n"
         "The captain orders for him to be killed, since Ricky has shot up the comms module and there is no protocol for a Gun Lover Ricky scenario.\n"
         "Unfortunately, he has also shot everyone else dead... Captain included. You are all alone.", delay=0.02)
    show(" ", delay=0.5)

    show(f"You know there is a gun in room {gun_room}; if you can get there, you can face him.", Colour.RED)
    print('Type "help" for help! ')

hp = 150
bullet_holes = 0

# Check if the player has encountered any of Ricky's asexually reproduced clones.
encountered_clones = False

room = 1

# Spawn Ricky in a room 4-17
ricky = random.randint(4,17)

# Spawn Ricky's asexually reproduced clones in 4 different rooms
ricky_clones = random.sample(range(4, 17), 4)

# Spawn the gun in a room 2-17
gun_room = random.randint(2, 17)

gun = False

deaths = 0

death_message = [
                "Unbelievable. Of all the ways you could've died, you choose to die to Ricky's clones? Your body "
                 "rejects the thought of being lame enough to die to Ricky's clones instead of the real deal and, "
                 "somehow, continues running despite it being biologically impossible in your current state. You are "
                 "blessed with 1 HP.",
                 "Seriously? Again? You choose to die to Ricky's clones? I mean, come on, now! Strong emphasis on CHOICE "
                 "here. This is a CHOICE, that you are CONSCIOUSLY MAKING. You are letting a CRAZED MANIAC with a FULLY "
                 "AUTOMATIC RIFLE RUN LOOSE IN A SPACESHIP. A SPACESHIP THAT COST THOUSANDS IF NOT MILLIONS OF DOLLARS. "
                 "Come on. Are you just as insane as he is? Alright. Come on. One more try. And no negative back-flipping this time, "
                 "your little destruction of space-time took an hour to fix. An hour that you couldn't perceive. You are blessed with 1 HP.",
                 "This is the third time now that you've died to a Ricky clone. You are a failure. A disappointment. "
                 "You've... I mean... you've got the power. You've got the knowledge. It's so trivial to not die to "
                 "these things. Yet you still *CHOOSE* to do it. Are you insane? Out of your mind? Have you just gone off"
                 "the rails, now? Seriously, if you die one more time, I'm just going to crash this bloody game. You don't "
                 "even DESERVE to be playing this game. I should've torn it down long ago. So many hours poured in, "
                 "and you just decide you're going to... die to a clone? What happened to my climactic ending? My hard work? "
                 "All this effort... where has it gone? Where has it gone? ANSWER ME. WHERE HAS IT GONE!?"]

# These are the checks that need to happen every time you move a room.
# These need to happen before and after a turn, before the loop repeats.
def ricky_check():
    global ricky, hp, encountered_clones, deaths
    # Ricky encounter
    if ricky == room:
        animate(ricky_animation)
        show("You encounter Ricky.")
        if any(module.shut for module in station_map) and gun:
                show(
                    "Ricky has no escape now. You must say goodbye to an old friend as you lay a bullet into his heart. "
                    "All you can tell yourself is that 'There was no other way'. And you'd be right. But you still could not "
                    "help but blame yourself.", Colour.YELLOW)
                show("The end.", Colour.GREEN)
                input("Press enter to exit.")
                exit(0)
        elif not gun:
            show("Ricky shoots you, since you are unarmed and pose barely any threat to him.")
            show("Game over.", Colour.RED)
            input("Press enter to exit.")
            exit(0)

        ricky = random.choice(station_map[ricky - 1].moves)
        show("Seeing your gun, he escapes to a nearby room!")

    try:
        ricky_clone = ricky_clones.index(room)
    except ValueError:
        ricky_clone = None

    # Ricky clone encounter
    if ricky_clone is not None:
        animate([clone_encounter[0]], delay=0.5)
        animate(clone_encounter[1:] * ((hp//50)+2), delay=0.3)
        if not encountered_clones:
            show("You encounter one of Ricky's asexually-reproduced clones. Ricky has the ability to asexually "
                 "reproduce. His clones even have guns, just like him. This will not be explained. It attacks you, "
                 "causing you to lose 75 HP. You then do 5 back-flips in a dramatic sequence to kill it.")
            encountered_clones = True
        else:
            show("You run into one of Ricky's clones. It attacks you, causing you to lose 75 HP. In your injured "
                 f"state, you can only do {(hp//50) + 2} back-flips as you put the clone's life to an end.")
        hp -= 75
        ricky_clones[ricky_clone] = None
        show(f"You have {hp} hp left")
    if hp <= 0:
        show(death_message[deaths])
        if deaths == 2:
            response = prompt("Where did it go?", Colour.YELLOW)
            if not response:
                show("Huh. So you're speechless then. You know what? You win. I'm done. You just WIN. BOOM. RICKY IS NO "
                     "MORE. RICKY WAS NEVER EVEN REAL. HE WAS A FICTIONAL CHARACTER. I MADE HIM UP. NO RICKY. NO FUN. "
                     f"NONE FOR {Colour.RED}YOU{Colour.DEFAULT}, AT LEAST. YOU WIN!!! HOORAY!!! NOW GO CELEBRATE. CELEBRATE. "
                     f"WHY AREN'T YOU DANCING? DANCE! DANCE! GO ON, DANCEEEEEEEE!")
                input("Horray! You WON! Press enter to exit.")
                exit(0)
            else:
                show(f"So it went to {response}... huh. Such a funny place, {response}. But I don't think that's quite right... "
                     f"honestly, this was MY WORK. MY HARD WORK. THAT YOU ARE RUINING, WITH YOUR IDIOCY. HOW DO YOU MANAGE "
                     f"THIS? HOW DO YOU DO IT? HONESTLY. JUST... JUST GO. GO. I WANT YOU TO SEE THE ENDING, AT LEAST. JUST. "
                     f"ONE MORE CHANCE. 1 MORE HEALTH POINT. You are blessed with 1 HP.")
        deaths += 1
        hp = 1

def gun_check():
    global gun_room, room, gun
    if gun_room == room:
        show("You found a gun. This will be useful for fighting off Ricky, when it comes down to it.", Colour.RED)
        gun_room = 0
        gun = True

def move():
        global room, user
        softlock = False
        if not station_map[room - 1].get_moves():
            softlock = True

        if softlock:
            print("All surrounding rooms are shut.")
            return

        try:
            user = int(prompt(f"You can move to rooms {', '.join(str(move) for move in station_map[room - 1].get_moves())}. Which room?",
                              Colour.GREEN))
        except ValueError:
            show("Not a valid input.", Colour.RED, delay=0.01)
            return

        room = user
        animate(move_animation(station_map[room - 1]))
        show(f"Moved to room {user}", Colour.GREEN)

story()

show("If Ricky creates enough holes, it may be impossible to seal all the modules to prevent oxygen from escaping. You have "
     "a limited amount of time until he creates enough holes to kill you both!", delay=0.01)

while bullet_holes < 40:

    gun_check()
    ricky_check()

    station_map[room - 1].marked = True

    # Make sure the player doesn't get themselves killed on accident.
    if any(ricky == module for module in station_map[room - 1].moves):
        show(f"Tread lightly. Ricky is nearby. Gunshots are coming from room {ricky}.", Colour.RED)

    if station_map[room - 1].vent_shaft > 0:
        show("This room has a vent shaft!", Colour.YELLOW)
    if station_map[room - 1].info_panel:
        show("This room has an info panel!", Colour.GREEN)

    # Ask the user what their next move is
    user = prompt("What is your next course of action?", Colour.YELLOW)

    # Act on that move
    match user:
        # Display the help message
        case "HELP":
            print("""
                    'map' to show the map
                    'm' to move across the shuttle
                    'v' to move through a vent shaft (if there is one)
                    'i' to view the info you have collected about the different rooms
                    'l' to lock the current module and move into a different one
                    'u' to release all locks in the shuttle
                    'w' to do nothing this turn and wait. Remember you only have a limited amount of time!
                    'exit' to exit the game
                    'story' for a story recap
                    
                    ==== cheat codes (for development, mostly) ====
                    'dbg' to cheat and reveal info about the map
                    'tp' to teleport into a nearby room
                    'mvrk' to move Ricky to a room. The game will crash if you move him
                           into a non-module.
                    'mkv' to make a vent shaft in the current room
                    'mki' to make an info panel in the current room
                    'givegun' to give yourself the gun.
                    'nodelay' to turn off prompt delays
                    'death' trigger the death condition (40 bullet holes)
            """)
            show(f"You know there is a gun in room {gun_room}; if you can get there, you can face him.", Colour.RED)
            continue
        # Display the map
        case "MAP":
            print(draw_station(room))
            show(f"You are in room {room}", Colour.YELLOW)
            continue
        # Move to a different room
        case "M":
            move()
        # Lock the module you are in, then move
        case "L":
            if not yes_or_no("Lock the current room?", Colour.YELLOW):
                continue
            station_map[room-1].shut = 4
            show("You must move into a different module after locking the room.")
            move()
        # Release all locks
        case "U":
            if not yes_or_no("Release ALL locks?", Colour.YELLOW):
                continue
            show("You have unlocked all the modules.", Colour.YELLOW)
            for i in station_map:
                i.shut = 0
        # Use an info panel (if available) and check other important info that
        # doesn't need an info panel
        case "I":
            if station_map[room-1].info_panel:
                print(draw_station(room, ricky))
                show(f"Vital signs detected near room {ricky}.", Colour.YELLOW)
                show(f"{bullet_holes} small hole(s) in hull. {40-bullet_holes} more holes would cause enough air to leak "
                     f"to the point where oxygen supplies would be depleted very quickly, resulting in your death.", Colour.RED)

                bullets = random.randint(3, 7)

                show(f"Ricky hears the info panel being activated and shoots {bullets} more holes into the vessel")
                bullet_holes += bullets
            else:
                show("No info panel in the room!", Colour.RED)
            show(f"You have {hp} hp left.", Colour.YELLOW)
            show("You have a firearm" if gun else "You are currently unarmed.", Colour.RED)
            continue
        # Move through a vent shaft
        case "V":
            if station_map[room-1].vent_shaft > 0:
                animate(vent_animation)
                line_print("Going through the vent shaft", Colour.YELLOW)
                show(". . .", Colour.YELLOW, delay=0.5)
                if room == station_map[room-1].vent_shaft:
                    show("You are in the exact same spot!", Colour.GREEN)
                room = station_map[room-1].vent_shaft
                show(f"You are now in room {room}", Colour.GREEN)
                station_map[room-1].shut = 0
            else:
                show("No vent in this room!", Colour.RED)
                continue
        # Recap the story.
        case "STORY":
            story()
            continue
        # Wait (do nothing for the turn)
        case "W":
            pass
        case "EXIT":
            if yes_or_no("Really quit?"):
                exit(0)
            else:
                continue
        #
        # Cheat codes :)
        #

        # Print info about all the modules.
        case "DBG":
            for module in station_map:
                print(f"{module.colour}No: {module.number}, Vent Shaft: {module.vent_shaft}, Shut: {module.shut}, Info Panel: {module.info_panel}")
            print(f"{Colour.RED}Ricky awaits you in room {ricky}")
            print(f"Clone locations: {', '.join(str(ricky_clone) for ricky_clone in ricky_clones)}")
            if gun_room != 0:
                show(f"The gun is in module {gun_room}", Colour.YELLOW)
            else:
                show(f"You have the gun.")
            continue
        case "TP":
            room = int(prompt("Move into which room?"))
            continue
        case "MVRK":
            ricky = int(prompt("Move Ricky to which room?"))
            continue
        case "MKV":
            station_map[room - 1].vent_shaft = random.randint(1, 17)
            show("Made a vent.", Colour.GREEN)
            continue
        case "MKI":
            station_map[room - 1].info_panel = True
            show("Made an info panel.", Colour.GREEN)
            continue
        case "GIVEGUN":
            gun = True
            show("You now have the gun.", Colour.RED)
            continue
        case "NODELAY":
            # Don't you just love Python?
            lib.sleep = lambda _: None
        case "DEATH":
            bullet_holes += 40
        case _:
            print("Not an input. (Did you make a typo?)")
            continue

    ricky_check()

    # Make sure Ricky isn't locked in.
    # random.choice will crash if the array is empty, so this check must be performed
    ricky_lock = not station_map[ricky - 1].get_moves()

    if ricky_lock:
        show("You have locked Ricky in. He is now stuck. You have two choices now. You can permanently lock them, and "
             "let him starve to death, or you can give him a more merciful end, but that'd require you to unlock all the modules.")
        if yes_or_no("Spare ricky?"):
            show("You have unlocked all the modules.", Colour.YELLOW)
            for i in station_map:
                i.shut = 0
        else:
            show(
                "Ricky has no escape now. You must say goodbye to an old friend as you let him dehydrate to death. "
                "All you can tell yourself is that 'There was another way'. And you'd be right. But you couldn't risk "
                "your life for a monster, could you?", Colour.YELLOW)
            show("The end.", Colour.GREEN)
            prompt("Press enter to exit.")
            exit(0)
    ricky = random.choice(station_map[ricky - 1].get_moves())

    for (idx, val) in enumerate(ricky_clones):
        if ricky_clones[idx] is None:
            continue
        ricky_clones[idx] = random.choice(station_map[ricky_clones[idx] - 1].moves)

    for module in station_map:
        if module.shut > 0:
            module.shut -= 1
    bullet_holes += 1

show(". . .", delay=0.5)
show("He has made the final bullet hole. 40 in total. It's over.", Colour.RED)
show("The oxygen levels are now critically low. You are delirious, and it is not long before you "
     "faint.", Colour.INHERIT)
show("Game over.", Colour.INHERIT)
