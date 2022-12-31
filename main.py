# A basic Pokemon catching game

# Import random module
import random


# Set up variables that the user inputs to create their own character
name = input("Enter your name: ")
age = input("Enter your age: ")
location = input("Enter where you're from: ")

# Intro dialogue to give some context
print(
    "Hello {name}, you are a  {age} year old Pokemon trainer from {location}.".format(name=name, age=age, location=location)
    )
print("My name is Oak, but everyone calls me the professor. I'm a leading expert on Pokemon and I research them with a device called the Pokedex.")
print("You're about to start your very own adventure.")
print(".........")
print("It seems this Pikachu has taken a liking to you and wants to join you on your adventure.")
print("In order to get stronger you'll need to catch and train more pokemon.")
print("Let's go and catch your very first Pokemon!")


# Create a Pokemon class to base Pokemon objects off of
class Pokemon:
    def __init__(self, name, type, level):
        self.name = name
        self.type = type
        self.level = level
        # Moves will be an array consisting of two moves
        # self.moves = moves
    def pokemon_health(self):
        health = 100
        if health <= 0:
            print("Pokemon has fainted and unable to battle")
            print("Battle ends")
    # Define an attack move to select a move from the trainer's and the wild Pokemon
    # The trainer can select a move to weaken the wild Pokemon, making it easier to catch
    def attack(self, wild_pokemon):
        # Try to use a random integer to determine wild Pokemon attack
        # Use a random number to select move
        random_number = random.randint(0, 6)
        # move = moves[random_index]
        if random_number == 1 or random_number == 4:
            print(random_number)
            print("Pikachu has dealt normal damage")
            wild_pokemon.health -= 10
            print(wild_pokemon.health)
        elif random_number == 2 or random_number == 5:
            print(random_number)
            print("Pikachu has dealt double damage!")
            wild_pokemon.health -= 20
            print(wild_pokemon.health)
        elif random_number == 3:
            print(random_number)
            print("Pikachu has dealt non-effective damage")
            wild_pokemon.health -= 5
            print(wild_pokemon.health)
        else:
            print(random_number)
            print("Pikachu missed")
            print(wild_pokemon.health)

pikachu = Pokemon("Pikachu", "electric", 5)
rattata = Pokemon("Rattata", "normal", 3)

class Trainer:
    # The roster the trainer has and the number of Pokeballs they have 
    team = [pikachu]
    number_of_pokeballs = 15

    def catch_pokemon(self, number_of_pokeballs, wild_pokemon):
        self.number_of_pokeballs -= 1
        chance = 0
        if wild_pokemon.health == 100:
            chance = random.randint(0, 10)
            if chance == 1:
                print("Congratulations! You caught a Pokemon!")
            else:
                print("Darn! Try again!")
                print("Maybe try attacking to weaken your opponent.")
        elif wild_pokemon.health > 80:
            chance = random.randint(0, 8)
            if chance == 1:
                print("congratulations! You caught a Pokemon!")
            else:
                print("Darn! Try again!")
                print("Maybe try attacking to weaken your opponent.")
        elif wild_pokemon.health > 60:
            chance = random.randint(0, 6)
            if chance == 1:
                print("congratulations! You caught a Pokemon!")
            else:
                print("Darn! Try again!")
                print("Maybe try attacking to weaken your opponent.")
        elif wild_pokemon.health > 40:
            chance = random.randint(0, 4)
            if chance == 1:
                print("congratulations! You caught a Pokemon!")
            else:
                print("Darn! Try again!")
                print("Maybe try attacking to weaken your opponent.")
        elif wild_pokemon.health > 20:
            chance = random.randint(0, 2)
            if chance == 1:
                print("congratulations! You caught a Pokemon!")
            else:
                print("Darn! Try again!")
                print("Maybe try attacking to weaken your opponent.")
        else:
            print("congratulations! You caught a Pokemon!")
            
            

