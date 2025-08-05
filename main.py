import time

def get_choice(prompt, options):
    while True:
        print(f"\n{prompt} {options}\n")
        choice = input("> ").strip().lower()
        if choice in options:
            return choice
        print("\nInvalid Choice! Try again\n")

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

def breakfast():
    return get_choice("What will you have for breakfast?", ["cereal", "beans"])

def beans():
    print("\nYou go to heat up the beans, put them in the microwave, and a minute in...\n")
    time.sleep(3)
    print("\nThe can EXPLODES! and the microwave BURSTS open\n")
    time.sleep(2)
    print("\nTheres beans all over the kitchen\n")
    time.sleep(2)
    print("\nYour gonna be late for school if you don't leave now!\n")
    time.sleep(2)
    return get_choice("Will you clean up and be late or leave the mess for someone else?", ["clean", "leave"])

def cereal():
    print("\nYou eat a nice full bowl of cereal and are ready for the day!\n")

def clean():
    time.sleep(1)
    print("\nIt takes 30 minutes to clean up\n")
    time.sleep(1)
    print("\nEvery thing is spotless\n")
    time.sleep(1)
    print("\nBut now you really better get going\n")
    time.sleep(1)

def leave():
    print("\nWell, its time to go\n")
    time.sleep(1)
    print("\nYou can take the bike or get the bus\n")
    time.sleep(1)
    return get_choice("bike or bus?", ["bike", "bus"])

def bike():
    print("\nYou take off for school on your bike, only 15 minutes til school\n")
    time.sleep(2)
    print("\nYou're almost at school but...\n")
    time.sleep(2)
    print("\nYou're suddenly THROWN off your bike \n")
    time.sleep(1.5)
    print("\nYou messed up your knee pretty bad\n")
    return get_choice("Are you gonna cry, or walk it off", ["clean", "walk"])

def bus():
    print("\nThe bus should be here any minute now\n")
    time.sleep(2)
    print("\nThe bus is here, you get on, but where are you going to sit?\n")
    time.sleep(2)
    print("\nIt seems like the cool kids are at the back, but theres someone sitting by himself\n")
    time.sleep(2)
    print("\nHe looks a bit sad\n")
    time.sleep(1)
    return get_choice("Are you going to sit with the cool kids, or the kid by himself?", ["cool", "alone"])

def fall_off_bike():
    print("\nYou fall off your bike and hurt your knee.\n")
    time.sleep(1)
    choice = get_choice("Are you going to cry or walk it off?", ["cry", "walk"])
    if choice == "cry":
        return get_bullied()
    else:
        return gain_confidence()

def get_bullied():
    print("\nSome kids see you crying and start to bully you.\n")
    time.sleep(1)
    choice = get_choice("Tell a teacher or stay quiet?", ["tell a teacher", "stay quiet"])
    if choice == "tell a teacher":
        print("\nThe teacher tells off the bullies and helps you.\n")
        time.sleep(1)
        print("\nYou feel safer at school now.\n")
    else:
        print("\nYou stay quiet and go home early, feeling sad.\n")
        time.sleep(1)
        print("\nRemember, it's always okay to ask for help!\n")

def gain_confidence():
    print("\nYou walk it off and feel proud of yourself.\n")
    time.sleep(1)
    choice = get_choice("Try out for the sports team or start a club?", ["team", "club"])
    if choice == "team":
        print("\nYou make it onto the team and learn teamwork!\n")
        time.sleep(1)
    else:
        print("\nYou start a club and make new friends with similar interests.\n")
        time.sleep(1)

def bus_path():
    choice = bus()
    if choice == "cool":
        become_popular()
    else:
        good_friends()

def become_popular():
    print("\nYou sit with the cool kids and become popular.\n")
    time.sleep(1)
    choice = get_choice("Sneak out of school or stay for class?", ["sneak out", "stay at school"])
    if choice == "sneak out":
        print("\nYou get caught and have to talk to the principal about choices.\n")
        time.sleep(1)
    else:
        print("\nEveryone gets caught skipping class and learns a lesson about honesty.\n")
        time.sleep(1)

def good_friends():
    print("\nYou sit with the loner and become good friends.\n")
    time.sleep(1)
    choice = get_choice("Start a band or study together?", ["band", "study"])
    if choice == "band":
        print("\nYou win the school talent show and learn about creativity!\n")
        time.sleep(1)
    else:
        print("\nYou ace your exams and learn the value of teamwork and hard work.\n")
        time.sleep(1)

def help_teacher():
    print("\nYou see a teacher struggling with books.\n")
    time.sleep(1)
    choice = get_choice("Will you help or ignore?", ["help", "ignore"])
    if choice == "help":
        print("\nThe teacher thanks you and you feel good about helping others.\n")
        time.sleep(1)
        ending_kindness()
    else:
        print("\nYou walk away, but later wish you had helped.\n")
        time.sleep(1)
        ending_reflection()

def library_path():
    print("\nYou have free time before class.\n")
    time.sleep(1)
    choice = get_choice("Go to the library or hang in the hallway?", ["library", "hallway"])
    if choice == "library":
        print("\nYou read a book and learn something new.\n")
        time.sleep(1)
        ending_learning()
    else:
        print("\nYou chat with friends but miss out on learning.\n")
        time.sleep(1)
        ending_reflection()

def lost_item():
    print("\nYou find a lost wallet in the hallway.\n")
    time.sleep(1)
    choice = get_choice("Return it or keep it?", ["return", "keep"])
    if choice == "return":
        print("\nYou return it and the owner is grateful.\n")
        time.sleep(1)
        ending_honesty()
    else:
        print("\nYou keep it but feel guilty all day.\n")
        time.sleep(1)
        ending_guilt()

def group_project():
    print("\nYou are assigned a group project.\n")
    time.sleep(1)
    choice = get_choice("Do all the work or share tasks?", ["all", "share"])
    if choice == "all":
        print("\nYou get tired and stressed. Sharing is better.\n")
        time.sleep(1)
        ending_teamwork()
    else:
        print("\nYou share tasks and finish quickly. Teamwork helps!\n")
        time.sleep(1)
        ending_teamwork()

def lunch_time():
    print("\nIt's lunch time.\n")
    time.sleep(1)
    choice = get_choice("Eat alone or join others?", ["alone", "join"])
    if choice == "alone":
        print("\nYou feel lonely. It's good to make friends.\n")
        time.sleep(1)
        ending_reflection()
    else:
        print("\nYou make new friends and enjoy lunch.\n")
        time.sleep(1)
        ending_friendship()

def ending_kindness():
    print("\nEnding 1: You learned kindness is important.\n")
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_learning():
    print("\nEnding 2: You learned the value of learning.\n")
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_teamwork():
    print("\nEnding 3: You learned teamwork is key.\n")
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_friendship():
    print("\nEnding 1: You learned friendship matters.\n")
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_honesty():
    print("\nEnding 2: You learned honesty is best.\n")
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_guilt():
    print("\nEnding 3: You learned guilt is not worth it.\n")
    time.sleep(1)
    print("\nTHE END\n")
    exit()

def ending_reflection():
    print("\nEnding 1: You learned to reflect on your choices.\n")
    time.sleep(1)
    print("\nTHE END\n")
    exit()

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