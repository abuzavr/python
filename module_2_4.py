numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for var1 in numbers:
    if var1 == 1:
        continue
    its_prime = True

    for i in range(2, var1):
        if var1 % i == 0:
            its_prime = False
            break

    if its_prime:
        primes.append(var1)

    else:
        not_primes.append(var1)

print("Primes:", primes)
print("Not Primes:", not_primes)
