with open("day3/input.txt") as file:
    input_list = file.read().splitlines()


total = 0
for i in range(len(input_list)):
    num1 = 0
    num2 = 0
    current = input_list[i]
    for j in range(len(current)):
        if int(current[j]) > num1:
            if num1 > num2: 
                num2 = num1
            num1 = int(current[j])
            
        elif int(current[j]) > num2:
            num2 = int(current[j])
    print(10*num1 + num2)
    total += 10*num1 + num2

print(total)