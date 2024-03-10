# OOP
class PlayerCharacter:
    
    # Class Object Attribute => self.attribute
    # NOT change across objects built with same Class
    membership = True
    
    # __init__ is called whenever we instantiate
    # self refers to PlayerCharacter
    
    def __init__(self, name, age):  
        
        # If this.membership = True
        if (self.membership):
            self.name = name # attributes / properties
            self.age = age # attributes / properties
        
    def run(self, hello):
        print(f'{hello} {self.name} is running :D')
        return 'done'
    
    def shout(self):
        print(f'My name is: {self.name}')


# Instantiate player1 using class    
player1 = PlayerCharacter('Player1', 20)
#help(player1)
print(f'player1:\n{player1}')
print(f'player1.name: {player1.name}') 
print(f'player1.age: {player1.age}')
print(f'\n')
print(f'player1.run(): {player1.run("OMG!")}')

print(f'\n')
print(f'\n')
player2 = PlayerCharacter('Player2', 24)
player2.attack = 50

print(f'player1.membership: {player1.membership}')
print(f'player2.membership: {player2.membership}')
print(f'\n')
print(f'player1.shout(): {player1.shout()}')
print(f'player2.shout(): {player2.shout()}')
#print(f'player2:\n{player2}')
#print(f'player2.name: {player2.name}')
#print(f'player2.age: {player2.age}')
#print(f'player2.attack: {player2.attack}')