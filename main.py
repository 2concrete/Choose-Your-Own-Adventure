import time

# Player stats dictionary
stats = {
    "happiness": 5
}

# Display current stats
def show_stats():
    print(f"\n[Stats] Happiness: {stats['happiness']}/10\n")

# Get a valid choice from the user
def get_choice(prompt, options):
    while True:
        print(f"\n{prompt} {options}\n")
        show_stats()
        choice = input("> ").strip().lower()
        if choice in options:
            return choice
        print("\nInvalid Choice! Try again\n")

# Game introduction and get player's name
def intro():
    print("\nWelcome to your first day of highschool\n")
    time.sleep(1)
    print("\nIt's time for a new era\n")
    time.sleep(1)
    print("\nWhat's your name?\n")
    time.sleep(0.5)
    name = input("> ").capitalize()
    print(f"\nWell {name}, let's get started\n")
    time.sleep(1)
    return name

# Ask what the player wants for breakfast
def breakfast():
    return get_choice("What will you have for breakfast?", ["cereal", "beans"])

# Beans breakfast path
def beans():
    print("\nYou go to heat up the beans, put them in the microwave, and a minute in...\n")
    time.sleep(3)
    print("\nThe can EXPLODES! and the microwave BURSTS open\n")
    time.sleep(2)
    print("\nTheres beans all over the kitchen\n")
    time.sleep(2)
    print("\nYour gonna be late for school if you don't leave now!\n")
    time.sleep(2)
    stats["happiness"] -= 1
    show_stats()
    # Player chooses to clean or leave the mess
    return get_choice("Will you clean up and be late or leave the mess for someone else?", ["clean", "leave"])

# Cereal breakfast path
def cereal():
    print("\nYou eat a nice full bowl of cereal and are ready for the day!\n")
    stats["happiness"] += 1
    show_stats()

# Clean up the beans mess
def clean():
    time.sleep(1)
    print("\nIt takes 30 minutes to clean up\n")
    time.sleep(1)
    print("\nEvery thing is spotless\n")
    time.sleep(1)
    print("\nBut now you really better get going\n")
    time.sleep(1)
    stats["happiness"] += 1
    show_stats()

# Choose transportation: bike or bus
def leave():
    print("\nWell, its time to go\n")
    time.sleep(1)
    print("\nYou can take the bike or get the bus\n")
    time.sleep(1)
    show_stats()
    return get_choice("bike or bus?", ["bike", "bus"])

# Bike path: accident scenario
def bike():
    print("\nYou take off for school on your bike, only 15 minutes til school\n")
    time.sleep(2)
    print("\nYou're almost at school but...\n")
    time.sleep(2)
    print("\nYou're suddenly THROWN off your bike \n")
    time.sleep(1.5)
    print("\nYou messed up your knee pretty bad\n")
    stats["happiness"] -= 2
    show_stats()
    # Player chooses how to react to the accident
    return get_choice("Are you gonna cry, or walk it off", ["clean", "walk"])

# Bus path: choose where to sit
def bus():
    print("\nThe bus should be here any minute now\n")
    time.sleep(2)
    print("\nThe bus is here, you get on, but where are you going to sit?\n")
    time.sleep(2)
    print("\nIt seems like the cool kids are at the back, but theres someone sitting by himself\n")
    time.sleep(2)
    print("\nHe looks a bit sad\n")
    time.sleep(1)
    show_stats()
    # Player chooses who to sit with
    return get_choice("Are you going to sit with the cool kids, or the kid by himself?", ["cool", "alone"])

# Handle falling off the bike
def fall_off_bike():
    print("\nYou fall off your bike and hurt your knee.\n")
    time.sleep(1)
    show_stats()
    choice = get_choice("Are you going to cry or walk it off?", ["cry", "walk"])
    if choice == "cry":
        return get_bullied()
    else:
        return gain_confidence()

# If player cries, they get bullied
def get_bullied():
    print("\nSome kids see you crying and start to bully you.\n")
    time.sleep(1)
    stats["happiness"] -= 2
    show_stats()
    choice = get_choice("Tell a teacher or stay quiet?", ["tell a teacher", "stay quiet"])
    if choice == "tell a teacher":
        print("\nThe teacher tells off the bullies and helps you.\n")
        time.sleep(1)
        print("\nYou feel safer at school now.\n")
        stats["happiness"] += 2
        show_stats()
    else:
        print("\nYou stay quiet and go home early, feeling sad.\n")
        time.sleep(1)
        print("\nRemember, it's always okay to ask for help!\n")
        stats["happiness"] -= 1
        show_stats()

# If player walks it off, they gain confidence
def gain_confidence():
    print("\nYou walk it off and feel proud of yourself.\n")
    time.sleep(1)
    stats["happiness"] += 2
    show_stats()
    choice = get_choice("Try out for the sports team or start a club?", ["team", "club"])
    if choice == "team":
        print("\nYou make it onto the team and learn teamwork!\n")
        time.sleep(1)
        stats["happiness"] += 1
        show_stats()
    else:
        print("\nYou start a club and make new friends with similar interests.\n")
        time.sleep(1)
        stats["happiness"] += 1
        show_stats()

# Handle bus path choices
def bus_path():
    choice = bus()
    if choice == "cool":
        become_popular()
    else:
        good_friends()

# If player sits with cool kids
def become_popular():
    print("\nYou sit with the cool kids and become popular.\n")
    time.sleep(1)
    stats["happiness"] += 2
    show_stats()
    choice = get_choice("Sneak out of school or stay for class?", ["sneak out", "stay at school"])
    if choice == "sneak out":
        print("\nYou get caught and have to talk to the principal about choices.\n")
        time.sleep(1)
        stats["happiness"] -= 2
        show_stats()
    else:
        print("\nEveryone gets caught skipping class and learns a lesson about honesty.\n")
        time.sleep(1)
        stats["happiness"] -= 1
        show_stats()

# If player sits with the loner
def good_friends():
    print("\nYou sit with the loner and become good friends.\n")
    time.sleep(1)
    stats["happiness"] += 2
    show_stats()
    choice = get_choice("Start a band or study together?", ["band", "study"])
    if choice == "band":
        print("\nYou win the school talent show and learn about creativity!\n")
        time.sleep(1)
        stats["happiness"] += 2
        show_stats()
    else:
        print("\nYou ace your exams and learn the value of teamwork and hard work.\n")
        time.sleep(1)
        stats["happiness"] += 1
        show_stats()

# Player sees a teacher struggling
def help_teacher():
    print("\nYou see a teacher struggling with books.\n")
    time.sleep(1)
    show_stats()
    choice = get_choice("Will you help or ignore?", ["help", "ignore"])
    if choice == "help":
        print("\nThe teacher thanks you and you feel good about helping others.\n")
        time.sleep(1)
        stats["happiness"] += 2
        show_stats()
        ending_kindness()
    else:
        print("\nYou walk away, but later wish you had helped.\n")
        time.sleep(1)
        stats["happiness"] -= 1
        show_stats()
        ending_reflection()

# Player chooses how to spend free time before class
def library_path():
    print("\nYou have free time before class.\n")
    time.sleep(1)
    show_stats()
    choice = get_choice("Go to the library or hang in the hallway?", ["library", "hallway"])
    if choice == "library":
        print("\nYou read a book and learn something new.\n")
        time.sleep(1)
        stats["happiness"] += 1
        show_stats()
        ending_learning()
    else:
        print("\nYou chat with friends but miss out on learning.\n")
        time.sleep(1)
        stats["happiness"] -= 1
        show_stats()
        ending_reflection()

# Player finds a lost wallet
def lost_item():
    print("\nYou find a lost wallet in the hallway.\n")
    time.sleep(1)
    show_stats()
    choice = get_choice("Return it or keep it?", ["return", "keep"])
    if choice == "return":
        print("\nYou return it and the owner is grateful.\n")
        time.sleep(1)
        stats["happiness"] += 2
        show_stats()
        ending_honesty()
    else:
        print("\nYou keep it but feel guilty all day.\n")
        time.sleep(1)
        stats["happiness"] -= 2
        show_stats()
        ending_guilt()

# Group project scenario
def group_project():
    print("\nYou are assigned a group project.\n")
    time.sleep(1)
    show_stats()
    choice = get_choice("Do all the work or share tasks?", ["all", "share"])
    if choice == "all":
        print("\nYou get tired and stressed. Sharing is better.\n")
        time.sleep(1)
        stats["happiness"] -= 1
        show_stats()
        ending_teamwork()
    else:
        print("\nYou share tasks and finish quickly. Teamwork helps!\n")
        time.sleep(1)
        stats["happiness"] += 1
        show_stats()
        ending_teamwork()

# Lunch time scenario
def lunch_time():
    print("\nIt's lunch time.\n")
    time.sleep(1)
    show_stats()
    choice = get_choice("Eat alone or join others?", ["alone", "join"])
    if choice == "alone":
        print("\nYou feel lonely. It's good to make friends.\n")
        time.sleep(1)
        stats["happiness"] -= 2
        show_stats()
        ending_reflection()
    else:
        print("\nYou make new friends and enjoy lunch.\n")
        time.sleep(1)
        stats["happiness"] += 2
        show_stats()
        ending_friendship()

# Various ending functions
def ending_kindness():
    print("\nEnding 1: You learned kindness is important.\n")
    show_stats()
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_learning():
    print("\nEnding 2: You learned the value of learning.\n")
    show_stats()
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_teamwork():
    print("\nEnding 3: You learned teamwork is key.\n")
    show_stats()
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_friendship():
    print("\nEnding 1: You learned friendship matters.\n")
    show_stats()
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_honesty():
    print("\nEnding 2: You learned honesty is best.\n")
    show_stats()
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_guilt():
    print("\nEnding 3: You learned guilt is not worth it.\n")
    show_stats()
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_reflection():
    print("\nEnding 1: You learned to reflect on your choices.\n")
    show_stats()
    time.sleep(1)
    print("\nTHE END\n")
    exit()

# Main game flow
def main():
    name = intro()
    cereal_beans = breakfast()
    if cereal_beans == "beans":
        clean_leave = beans()
        if clean_leave == "clean":
            clean()
            bike_bus = leave()
        else:
            bike_bus = leave()
    else:
        cereal()
        bike_bus = leave()

    if bike_bus == "bike":
        fall_off_bike()
        help_teacher()
    elif bike_bus == "bus":
        bus_path()
        library_path()

    lost_item()
    group_project()
    lunch_time()

main()