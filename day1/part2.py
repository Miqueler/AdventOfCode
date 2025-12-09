with open("day1/input.txt") as sequence_file:
    sequence = sequence_file.read().splitlines()

pos = 50
past_pos = pos
counter = 0

for current in sequence:
    if not current:
        continue

    # signed distance
    if current[0] == "L":
        dis = -int(current[1:])
    elif current[0] == "R":
        dis = int(current[1:])
    else:
        continue  # just in case

    # count full 100-click rotations (each hits 0 once)
    full_turns = abs(dis) // 100
    counter += full_turns

    # remainder in the same direction
    if dis >= 0:
        dis = dis % 100
    else:
        dis = -((-dis) % 100)

    # apply remainder
    pos += dis

    # handle at most one extra crossing for the remainder
    if pos == 0:
        counter += 1
    elif pos > 99:
        counter += 1
        pos -= 100
    elif pos < 0:
        if past_pos != 0:
            counter += 1
        pos = 100 + pos

    past_pos = pos

print(counter)