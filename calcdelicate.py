from sympy import isprime
# h1 and ok functions found on OEIS.org
# https://oeis.org/A050249
# Michael S. Branicky, Jun 19 2022

def h1(n): # hamming distance 1 neighbors of n
    s = str(n); d = "0123456789"; L = len(s)
    yield from (int(s[:i]+c+s[i+1:]) for c in d for i in range(L) if c!=s[i])

def ok(n): 
    return isprime(n) and all(not isprime(k) for k in h1(n) if k!=n)

# Calculate more Delicate Primes
with open("delicate-primes.txt", "r") as f:
    last_prime = int(f.readlines()[-1].strip())
    f.close()

with open("delicate-primes.txt", "a") as f:
    print(f"From: {last_prime} to {10**32}")
    for k in range(last_prime+1, 10**32):
        if ok(k):
            f.write(str(k)+"\n")
            print(k)