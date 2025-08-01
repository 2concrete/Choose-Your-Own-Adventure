import time

# intro

print("\nWelcome to your first day of highschool\n")
time.sleep(1)
print("It's time for a new era\n")
time.sleep(1)
print("What's your name?\n")
time.sleep(0.5)

name = input("> ").capitalize()

print(f"\nWell {name}, let's get started\n")
time.sleep(1)
print(f"What will you have for breakfast?\n")
time.sleep(1)

# decision 1 | cereal or beans

while True:
  print(f"Cereal or beans?")  
  time.sleep(0.5)
  cereal_beans = input("\n> ").lower()
  if cereal_beans in ["beans", "cereal"]:
    print(f"\n{cereal_beans.capitalize()} it is!\n")
    time.sleep(1)
    break
  print("\nInvalid Choice! Try again\n")

  print(f"\n{cereal_beans.capitalize()} it is!\n")
  time.sleep(1)

# choice beans | explosion

if cereal_beans == "beans":
  print("You go to heat up the beans, put them in the microwave, and a minute in...\n")
  time.sleep(3)
  print("The can EXPLODES! and the microwave BURSTS open\n")
  time.sleep(2)
  print("Theres beans all over the kitchen\n")
  time.sleep(2)
  print("Your gonna be late for school if you don't leave now!\n")
  time.sleep(2)
  print("Will you clean up and be late or leave the mess for someone else?\n")
  time.sleep(1)
  
# decision 1 | beans or cereal
  
if cereal_beans == "cereal":
  print("You eat a nice full bowl of cereal and are ready for the day!")
  
if cereal_beans == "beans":
  while True:
    print("Clean or Leave\n") 
    time.sleep(0.5)
    clean_leave = input("> ").lower()
    if clean_leave in ["clean", "leave"]:
      break
    print("\nInvalid Choice! Try again\n")
  
# decision 2 | bike or bus

time.sleep(1)
print("\nNow, how are you going to get to school?\n")
time.sleep(1)

while True:
  print("You can bike or get the bus")  
  time.sleep(0.5)
  bike_bus = input("\n> ").lower()
  if bike_bus in ["bike", "bus"]:
    break
  print("\nInvalid Choice! Try again\n")
  
# decision 3 | cry or walk it off
  
if bike_bus == "bike":
  print("\n You take off for school on your bike, only 15 minutes til school\n")
  time.sleep[2]
  print("Your almost at school but...\n")
  time.sleep(2)
  print("Your suddenly THROWN off your bike \n")
  time.sleep(1.5)
  print("You messed up your knee pretty bad")

  while True:
    print("Are you gonna cry, or walk it off")
    time.sleep(0.5)
    print("[1][2]")
    time.sleep(0.5)
    bike_bus = input("\n> ").lower()
    if bike_bus in ["1", "2"]:
      break
    print("\nInvalid Choice! Try again\n")
  
# 

if bike_bus == "bus":
  print("\nGreat choice! The bus should be here any minute now\n")
  time.sleep(2)
  print("The bus is here, you get on, but where are you going to sit?\n")
  time.sleep(2)
  print("It seems like the cool kids are at the back, but theres someone sitting by himself\n")
  time.sleep(2)
  print("He looks a bit sad\n")
  time.sleep(1)
  
  while True:
    print("Sit with the cool kids, or sit with the guy by himself?")  
    time.sleep(0.5)
    print("[1][2]")
    time.sleep(0.5)
    bus = input("\n> ").lower()
    if bus in ["1", "2"]:
      break
    print("\nInvalid Choice! Try again\n")
    
