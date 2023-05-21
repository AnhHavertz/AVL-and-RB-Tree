import random
import math

randomN = random.randint(990000, 1000000)  # Min-max of N (~10^6)
randomNumber = random.randint(10000, 10000000)  # Min-max of elements in tree

with open("logN_145logN.txt", "w") as fo:
    for i in range(1, 11):
        filename = "filedata" + str(i) + ".txt" 
        with open(filename, "w") as file:
            N = randomN
            file.write(str(N) + '\n')

            if i < 3:
                uniqueNumbers = set()
                while len(uniqueNumbers) < N:
                    uniqueNumbers.add(randomNumber)
                    randomNumber = random.randint(10000, 10000000)
                if i == 1:  # tăng dần / ascending
                    for num in sorted(uniqueNumbers):
                        file.write(str(num) + ' ')
                else:  # giảm dần / descending
                    for num in sorted(uniqueNumbers, reverse=True):
                        file.write(str(num) + ' ')
            else:  # ngẫu nhiên / random
                uniqueNumbers = set()
                while len(uniqueNumbers) < N:
                    uniqueNumbers.add(randomNumber)
                    randomNumber = random.randint(10000, 10000000)
                for num in uniqueNumbers:
                    file.write(str(num) + ' ')

            fo.write(str(math.log2(N)) + ' ' + str(1.45 * math.log2(N)) + '\n')
