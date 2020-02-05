# Colm O Caoimh
# Check if a number is prime.
#The primes are 2, 3, 5, 7, 11, 13, ...

p = 347
m = 2
is_prime = True

while m < p:
    if p % m == 0:
        is_prime = False
    m = m + 1

if is_prime:
    print(p, "is a prime number")
else:
    print(p, "is not prime.")
