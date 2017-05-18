import math


def find_binary_of(num):
    num = int(num)
    count = 0
    binary = []
    numholder = 1
    while numholder > 0:
        print('running for the ', count, ' time')
        count += 1
        numholder = math.trunc(num / 2)
        binaryholder  = num % 2
        num = numholder
        binary.append(binaryholder)

    answer = ""
    for i in reversed(binary):
        answer += str(i)

    return answer


def find_num_of_binary(binary):
    binary = int(binary)
    count = 0
    numberholder = 0
    while len(str(binary)) > count:
        numberholder =  (numberholder * 2) + int(str(binary)[count])
        count += 1
    return numberholder


while True:
    ask = input("num? \n")
    final_answer = find_binary_of(ask) #find_num_of_binary(ask)
    print(final_answer)
