colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'brown', 'black', 'white']

with open('wellert.txt', 'w+') as file:
    file.writelines(color + "\n" for color in colors)

    file.seek(0)
    for line in file:
        print(line, end="")