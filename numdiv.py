yournumber = int(input("What is your number? "))
howmanydivisors = yournumber
howmanydivisors = howmanydivisors + 1
alldivisors = []
divisors = []
for i in range(howmanydivisors):
    if i != 0:
        alldivisors.append(i)
for i in alldivisors:
    if i == 0:
        alldivisors.remove
for i in alldivisors:
    oddoreven = yournumber % i
    if oddoreven == 0:
        divisors.append(i)
print("The divisors of your number are", divisors)