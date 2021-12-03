input_file = 'C:/Users/TechMatt/Documents/Programming/Python/advent_of_code_21/day_2/input.txt'

# Coordinates system
#-------------------> x
#|
#|
#|
#|
#V
#y

#X, Y coordinates
x = 0
y = 0

with open(input_file, "r") as f:
    data = f.readlines()
    for elem in data:
        commands = elem.split()
        command = commands[0]
        value = int(commands[1])

        if command == "forward":
            x += value
        elif command == "down":
            y += value

        elif command == "up":
            y -= value

print(x * y)    



