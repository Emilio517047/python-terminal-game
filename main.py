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

print(".....")
print("A wild Pokemon has appeared!")
# Create a Pokemon class to base Pokemon objects off of
class Pokemon:
    def __init__(self, name, type, level, health):
        self.name = name
        self.type = type
        self.level = level
        self.health = health
        # Moves will be an array consisting of two moves
        # self.moves = moves

    # Define an attack move to select a move from the trainer's and the wild Pokemon
    # The trainer can select a move to weaken the wild Pokemon, making it easier to catch
    def attack(self, wild_pokemon):
        if wild_pokemon.health <= 0:
            print("Pokemon has fainted and unable to battle")
            print("Battle ends")
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



class Trainer:
    # The roster the trainer has and the number of Pokeballs they have 
    def __init__(self, team, number_of_pokeballs, caught_pokemon):
        self.team = team
        self.number_of_pokeballs = number_of_pokeballs
        self.caught_pokemon = caught_pokemon

    def catch_pokemon(self, wild_pokemon, health):
        self.number_of_pokeballs = 15
        self.caught_pokemon = False
        self.number_of_pokeballs -= 1
        chance = 0
        self.health = health
        
        if self.number_of_pokeballs == 0:
            print("You are out of pokeballs")
            print("Go to a Pokemart to buy more.")
            print("Battle over.")
        else:
            if wild_pokemon.health == 100:
                chance = random.randint(0, 10)
                if chance == 1:
                    self.caught_pokemon = True
                    print("Congratulations! You caught a Pokemon!")
                else:
                    print("Darn! Try again!")
                    print("Maybe try attacking to weaken your opponent.")
            elif wild_pokemon.health > 80:
                chance = random.randint(0, 8)
                if chance == 1:
                    self.caught_pokemon = True
                    print("congratulations! You caught a Pokemon!")
                else:
                    print("Darn! Try again!")
                    print("Maybe try attacking to weaken your opponent.")
            elif wild_pokemon.health > 60:
                chance = random.randint(0, 6)
                if chance == 1:
                    self.caught_pokemon = True
                    print("congratulations! You caught a Pokemon!")
                else:
                    print("Darn! Try again!")
                    print("Maybe try attacking to weaken your opponent.")
            elif wild_pokemon.health > 40:
                chance = random.randint(0, 4)
                if chance == 1:
                    self.caught_pokemon = True
                    print("congratulations! You caught a Pokemon!")
                else:
                    print("Darn! Try again!")
                    print("Maybe try attacking to weaken your opponent.")
            elif wild_pokemon.health > 20:
                chance = random.randint(0, 2)
                if chance == 1:
                    self.caught_pokemon = True
                    print("congratulations! You caught a Pokemon!")
                else:
                    print("Darn! Try again!")
                    print("Maybe try attacking to weaken your opponent.")
            else:
                self.caught_pokemon = True
                print("congratulations! You caught a Pokemon!")
                 
pikachu = Pokemon("Pikachu", "electric", 5, 100)
rattata = Pokemon("Rattata", "normal", 3, 100)



class Battle:
    def __init__(self, pikachu, rattata):
        self.pikachu = pikachu
        self.rattata = rattata

    while rattata.health > 0 and Trainer.number_of_pokeballs > 0 and Trainer.caught_pokemon == False:
        print("What would you like to do?")
        decision = input("Fight or throw Pokeball? fight/throw: ")
        if decision == "fight":
            pikachu.attack(rattata)
            
        elif decision == "throw":
            Trainer.catch_pokemon(100, rattata)
            
        else:
            print("Please type: 'fight' or 'throw'")
    else:
        print("Battle is over!")

battle = Battle(pikachu, rattata)