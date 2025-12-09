with open("day2/input.txt") as sequence_file:
    id_list = sequence_file.read().split(",")


interval = str()
num = str()
start, end = int(), int()
current = 0
total = 0

for i in range(len(id_list)):
    interval = id_list[i]
    start = int(interval.split("-")[0])
    end = int(interval.split("-")[1])
    current = start

    while end >= current:
        num = str(current)
        if len(num) % 2 != 0:
            current += 1
            continue
        if num[:(len(num) // 2)] == num[(len(num)//2):]:
            total += current
        
        print(f"{num[:(len(num) // 2)]} // {num[(len(num) // 2):]}, current {current}")
        print(len(num))
        current += 1

print(total)