import os
#write a code to clear the console before printing
os.system('cls' if os.name == 'nt' else 'clear')

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

input('\nPress enter to exit...\n')