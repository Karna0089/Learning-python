# 🎯 The Mission
# Create a Python script where the player must battle a wild goblin in a turn-based arena. The game should loop through turns until either the player or the goblin reaches 0 Health.

# 🛠️ Core Requirements
# To pass the code review for this quest, your program must include:

# The Stats: * Variables for the Player's Health (e.g., 100) and the Player's Potions (e.g., 3). -done

# Variables for the Goblin's Health (e.g., 80). -changed to 100 but the task is done

# The Battle Loop:

# A while loop that keeps running as long as both the player and the goblin have health greater than 0.

# The Player's Turn:

# Every turn, ask the player what they want to do: [A]ttack, [H]eal, or [R]un. - i have to use def

# If they attack: Deal a random amount of damage between 10 and 20 to the goblin. Print the damage dealt and the goblin's remaining health. -done

# If they heal: Check if they have potions left. If yes, add 25 to their health, subtract 1 potion, and print the new stats. If no, tell them they are out of potions! - done

# If they run: Break the loop and print a cowardly escape message. -done

# The Goblin's Turn:

# After the player makes their move (and assuming the goblin is still alive), the goblin automatically attacks back!

# Deal a random amount of damage between 5 and 15 to the player. Print the damage and the player's remaining health. - done

# The Game Over Screen:

# Once the loop ends, check who won. If the goblin has 0 or less health, print a Victory message. If the player has 0 or less health, print a Game Over message.

# 🚀 Bonus Challenges (For Extra Glory)
# If you want to push your logic skills a bit further, try adding these:

# Critical Hits: When the player attacks, give them a 20% chance to land a "Critical Hit" that deals double damage. (Hint: You'll need random.randint for this!) -done

# Loot Drop: If the player defeats the goblin, generate a random number of coins (between 10 and 50) as a reward and print it to the screen.

#Before writing code thoughts:
#1. I have to create inventory to store potions
#2. I need to store player's health, coins and goblin's health by using variables - Change of plan i will use dictionary to store all stats of player and goblin so that if anyhow I need to introduce something new in near future I can use that dictionary directly 
#3. I need to create a story to make this game engaging 
#4. I have to be cautious about any bug related to health of player and goblin... (I can use def function to check health of both player and goblin before running any function) - actually I can use while loop for this condition
#5. I need a while loop to create game
#6. I need to use def for many actions like attack, heal and also run
#7. I need to import some modules like random - done
#8. I need to make text based UI and greeting system
#9. Since goblin has less health and less attack dammage it's would be unfair then I should match the health so that player still has an advantage of dammage but i am giving the goblin an advantage to tackle player's attack (this tackle will only work if the attack of player wasn't critical)
#10. Since this is a turn based rpg game i would recommend that goblin should deal damage when i use health potion because in real action there is no chance to be safe from opponent while using healing items but since the question didn't ask me to do so i will not make that feature and make the plain game but according to me the player have to only use attack and everytime the player will win thats not a real game.

#Actual code:
import random
player = {"Health": 100, "Potion": 3, "Coins": 0}
goblin = {"Health": 100}

def stats():
    print(f"\n---STATS---\nYour health: {player.get("Health")}\nPotion left: {player.get("Potion")}\nGoblin health: {goblin.get("Health")}")

def gattack():
    dam = random.randint(5,15)
    if goblin.get("Health") > 0: #ensuring goblin is still alive
        player["Health"] -= dam
    else:
        print("Goblin has been killed!")

def dealdamage(multiplyer):
    dam = random.randint(10,20) * multiplyer
    goblin["Health"] -= dam
    if multiplyer == 2:
        print(f"---CRITICAL HIT---\nYou have dealt a damage of {dam} hp.")
    else:
        print(f"You have dealt a damage of {dam} hp.")

def attack():
    if random.randint(0,100) > 20: #80% chance of not hitting a  criticle shot
        if random.randint(0,100) > 10: #90% chance of not dodgeing the player's attack
            dealdamage(1)
            gattack()
        else:
            print("Goblin has successfully tackled your attack")
    else:#If shot was critical
        dealdamage(2)
        gattack()
    stats()

def heal():
    if player.get("Potion") <= 0:
        print("You ran out of the Potion!")
    elif player.get("Health") == 100:
        print("Don't panic.\n Your health is already full! You don't need to use the Potion.")
    elif player.get("Health") > 75:
        player["Potion"] -= 1
        player["Health"] = 100
        gattack()
        stats()
    else:
        player["Potion"] -= 1
        player["Health"] += 25
        gattack()
        stats()

def runAway():
    print(f"You safely got out of the situation.\nBut the goblin was saying that he hadn't seen any coward human like you ever.")
    survivalChance = random.randint(0,1)
    if survivalChance == 0:
        print(f"\nNext day...\nGoblin found you hiding from him and killed you.\n----YOU LOST----")
    else:
        print(f"Then proudly lead a coward life.\nAnd village chief done your task to save the village.")
def story():
    print("-----GAME STARTED-----")
    username = input("Hello I am NIZ, what sohuld i call you?: ")
    print(f"Once upon a time, in a village named Palampur a brave person named {username} lived there.\nDuring those days goblin were new creatures on Earth and does harm to normal humans.\nSo the chief of Palampur, Naju asked the {username} to defeate the strange creature and save the village from it.\nSo {username} gone to fight the goblin with a Sword and three magical potions which heals his health.\n{username} started to find the goblin in a forest nearby their village.\n(The goblin appeared out of somewhere and both of them started fighting).")

def menu():
    while True:
        if player.get("Health") <= 0:
            print("You have been died!")
            stats()
            break
        if goblin.get("Health") <= 0:
            player["Coins"] += random.randint(10, 50)
            print(f"---Victory---\nYou have successfully defeated the Goblin.")
            break
        print(f"\n---Choose your action---\nA to attack\nH to heal yourself\nR to run away\nS to see stats\nE to exit.")
        command = input("").lower()
        if command == "a":
            attack()
        elif command == "h":
            heal()
        elif command == "r":
            runAway()
            break
        elif command == "s":
            stats()
        elif command == "e":
            break
        else:
            print("I didn't recognise your command! Please try again.")
#Game
story()
menu()