n = int(input())

# Write code below here
# Print the n'th prime number

def is_prime(a):
    if a<2:
        return False
    
    for i in range(2, (a//2 + 1)):
        if a%i == 0:
            return False
    return True

def nthPrime(n):
    cnt = 0
    numerical_val = 2

    while True:
        if is_prime(numerical_val):
            cnt += 1
            if cnt ==n:
                return numerical_val
        numerical_val += 1

print(f"{n}-th prime number: {nthPrime(n)}")