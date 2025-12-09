with open("day1/input.txt") as sequence_file:
    sequence = sequence_file.read().split("\n")

pos = 50
current = str()
counter = 0
for i in range(len(sequence)-1):
    current = sequence[i]
    if current[0] == "L":
        pos -= int(current[1:])
    elif current[0] == "R":
        pos += int(current[1:])
    

    if pos % 100 == 0: 
        pos = 0
        counter += 1
    elif pos > 99:

        pos -= 100 * (pos // 100)
    elif pos < 0:
        pos = (100 * ((abs(pos) // 100)+1)) + pos


print(counter)