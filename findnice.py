# This checks the sums of every digit in the prime. Just for fun. Dont worry about it.

with open("delicate-primes.txt", "r") as file:
    data = file.read()
fileLines = data.splitlines()

currentCount = 0
for i in range(len(fileLines)):
    primeSum = sum(int(ch) for ch in fileLines[i])
    currentCount += primeSum
    if ((i+1) % 1000 == 0):
        print(f"Average for {i-999}-{i+1} = {currentCount/1000}")
        currentCount = 0
