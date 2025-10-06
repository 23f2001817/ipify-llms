"""
Prime number computation using trial division.
This module computes the first 10 prime numbers and prints the 10th one.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    """Find the nth prime number."""
    count = 0
    candidate = 2
    while count < n:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 1
    return candidate

if __name__ == "__main__":
    print(find_nth_prime(10))
