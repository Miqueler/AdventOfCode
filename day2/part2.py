with open("day2/input.txt") as sequence_file:
    id_list = sequence_file.read().split(",")


interval = str()
num = str()
start, end = int(), int()
current = 0
total = 0

for i in range(len(id_list)): #Loops over the different ranges
    #Get the range of values
    interval = id_list[i]
    start = int(interval.split("-")[0])
    end = int(interval.split("-")[1])
    current = start

    

    while end >= current: #loop over all numbers in the range
        flag = 0

        num = str(current)
        #Loop over all the possible groups of "sub numbers" (ex: 1111 -> 1-1-1-1, 11-11)
        for j in range(1, (len(num) // 2) + 1): #Try for every possible group of convs
            if len(num) % j != 0: 
                current += 1
                continue

            for i in range((len(num) // 2)):
                print(f"first: {num[i]} second: {num[i + j]}")
                if num[i] != num[i + j]:
                    flag = 1
                    break

            if flag == 0: 
                total += current
            flag = 0
            
            current += 1
            continue

        current += 1

print(total)