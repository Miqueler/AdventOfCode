with open("day3/input.txt") as file:
    input_list = file.read().splitlines()


total = 0
for i in range(len(input_list)):
    max = 0
    check = 0
    current = input_list[i]
    for j in range(len(current) - 1): #problem is that if a number is bigger but it's after the number in 2 you get n impossible number due to not being able to reorder the string
        if max // 10 < int(current[j]):
            max = int(current[i]) * 10
            for k in range(len(current) - 1 - j):
                if int(current[j + 1 + k]) > check:
                    check = int(current[j + 1 + k])
    


    total += max + check

print(total)