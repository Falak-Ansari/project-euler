def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor = factor + 1
    return n

n = 600851475143
print("Largest prime factor:", largest_prime_factor(n))
