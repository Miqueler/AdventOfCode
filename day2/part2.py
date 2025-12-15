with open("day2/input.txt") as sequence_file:
    id_list = sequence_file.read().split(",")


interval = str()
num = str()
start, end = int(), int()
current = 0
total = 0
flag = 0

for i in range(len(id_list)): #Loops over the different ranges
    #Get the range of values
    interval = id_list[i]
    start = int(interval.split("-")[0])
    end = int(interval.split("-")[1])
    current = start

    

    while end >= current: #loop over all numbers in the range
        num = str(current)
        #Loop over all the possible groups of "sub numbers" (ex: 1111 -> 1-1-1-1, 11-11)
        for j in range(1, (len(num) // 2) + 1): #Try for every possible group of convs
            if len(num) % j != 0: 
                continue
            #Try current conv
            for i in range((len(num) // j)):
                
                if ((i+2)*j) > len(num): break
                
                if num[(i * j):((i+1)*j)] != num[((i+1)*j):((i+2)*j)]:
                    flag = 1
                    #print(True)
                    break
                #else:
                #    print(False)
            if flag == 0: 
                total += current
                break
            flag = 0
        #print(total)
        current += 1

print(total)