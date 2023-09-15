import time
import random
import sUserData

def print_pins(pin_positions):
    print("\nLockpicking progress:")
    for i, position in enumerate(pin_positions, start=1):
        print(f"Pin {i}: {'*' if position >= 1 else '_'}")
        
def main_enhanced_lockpicking():
    print("Welcome to the Enhanced Lockpicking Challenge!")
    print("Manipulate the pins to unlock the chest, while managing tension and avoiding breakage.")

    pin_positions = [random.uniform(0.3, 0.7) for _ in range(3)]  # Changed to 3 pins
    tension = 0.5
    lockpick_health = 100
    chest_unlocked = False

    while not chest_unlocked and tension < 1:
        print_pins(pin_positions)
        print("\nTension:", tension)
        print("Lockpick health:", lockpick_health)

        pin_to_move = int(input("\nSelect a pin to move (1-3): ")) - 1  # Changed to 3 pins

        if 0 <= pin_to_move < 3:  # Changed to 3 pins
            amount_to_move = float(input("Enter amount to move the pin (0.1 - 0.5): "))

            tension += amount_to_move * random.uniform(0.5, 1.5)

            if random.random() < tension * 0.5:
                lockpick_health -= 20
                print("Your lockpick almost broke!")

            pin_positions[pin_to_move] += amount_to_move
            if all(position >= 1 for position in pin_positions):
                chest_unlocked = True
                print("\nChest unlocked! You obtained the item.")
                return True
            else:
                print("\nPin moved. Keep working on unlocking the chest.")

            tension -= random.uniform(0.1, 0.3)
            tension = max(0, min(1, tension))

            if lockpick_health <= 0:
                print("\nYour lockpick broke! Game over.")
                return False
                break

        else:
            print("\nInvalid pin selection. Try again.")

    if tension >= 1:
        print("\nYou applied too much tension and the lock broke. Game over.")

    print("\nGame over.")

###############################################################################################################

class Substance:
    def __init__(self, name, icon, color):
        self.name = name
        self.icon = icon
        self.color = color

substances = [
    Substance("Red Powder", "🔴", "red"),
    Substance("Blue Liquid", "🔵", "blue"),
    Substance("Green Crystal", "💚", "green"),
    Substance("Yellow Gas", "💛", "yellow"),
    Substance("Purple Elixir", "💜", "purple"),
]

reactions = {
    ('Red Powder', 'Blue Liquid'): Substance("Purple Potion", "🟣", "purple"),
    ('Blue Liquid', 'Yellow Gas'): Substance("Green Mixture", "🟢", "green"),
    ('Yellow Gas', 'Red Powder'): Substance("Orange Solution", "🟠", "orange"),
}

max_attempts = 5

def main_deductive_alchemy():
    flag = False
    print("Welcome to the Deductive Alchemy Challenge!")
    print("Experiment, deduce, and combine substances to unlock the chest.")

    target_concoction = generate_target_concoction(substances)
    attempts = max_attempts

    while attempts > 0:
        print("\nAvailable substances:")
        display_substances(substances)
        print(f"Attempts remaining: {attempts}")

        player_concoction = input("Enter your concoction (e.g., RBG): ").upper()

        feedback = get_feedback(player_concoction, target_concoction)
        print("Feedback:", feedback)

        if feedback == "CORRECT":
            print("Congratulations! Your concoction unlocks the chest.")
            flag = True
            break
        else:
            print("Concoction failed. Keep experimenting, deducing, and using strategy.")
            attempts -= 1

    if attempts == 0:
        print("You've run out of attempts. The chest remains locked.")
        return False
    if flag == True:
        return True

def generate_target_concoction(substances):
    return ''.join(random.sample([substance.name[0] for substance in substances], 3))

def display_substances(substances):
    for substance in substances:
        print(f"{substance.icon} - {substance.name}")

def display_concoction(concoction):
    for char in concoction:
        substance = next(substance for substance in substances if substance.name.startswith(char))
        print(f"{substance.icon} ", end='')
    print()

def get_feedback(player_concoction, target_concoction):
    if player_concoction == target_concoction:
        return "CORRECT"
    
    feedback = []
    for i in range(len(player_concoction)):
        if player_concoction[i] == target_concoction[i]:
            feedback.append("Correct")
        elif player_concoction[i] in target_concoction:
            feedback.append("In target")
        else:
            feedback.append("Incorrect")
    
    return ', '.join(feedback)

###############################################################################################################

def main_reaction_time_game():  
    print("REACTION    TIME    MINIGAME    \n")
    time.sleep(1)
    print("When you see the 'GO!' prompt, press Enter as quickly as possible.")
    print("Be ready for changing patterns and decreasing delays!")

    input("Press Enter to start...")

    num_prompts = 5
    max_delay = 3.0
    total_time = 0
    req = 0.4000
    temp_req = 0.400

    for _ in range(num_prompts):
        print(total_time)
        reaction_time = 0
        delay = random.uniform(0.5, max_delay)
        time.sleep(delay)

        prompt_type = random.choice(["GO!", "IGNORE!"])
        print("\n" + prompt_type)

        if prompt_type == "IGNORE!":
            wait_time = time.time()
            input("Press Enter after one second!")
            ignore_time = time.time()
            if ignore_time - wait_time <1:
                total_time += ignore_time - wait_time
            
        if prompt_type == "GO!":
            start_time = time.time()
            input()
            end_time = time.time()
            reaction_time = end_time - start_time
            total_time += reaction_time
            if reaction_time < 0.1:
                total_time += 1

        

        if prompt_type == "GO!":
            req = req + temp_req
            max_delay -= 0.3  # Decrease the max delay for next prompt

    print("DONE!")
    time.sleep(1)
    print(f"Total Reaction Time: {total_time:.3f} seconds")
    print(f"Required Reaction Time: {req} seconds")
    if total_time > req:
        print('You failed! (lmao)')
        return False
    else:
        print('You passed!')
        return True
        
def mG(rank):
    temp = random.randint(1,3)
    if temp == 1:
        x = main_enhanced_lockpicking()
    elif temp == 2:
        x = main_deductive_alchemy()
    else:
        x = main_reaction_time_game()
    if x == True:
        sUserData.mG_win(rank)
        