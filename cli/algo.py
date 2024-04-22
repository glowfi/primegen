# CheckPrime algo_V1
# T.C. -> O(n)
def isPrime_V1(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# CheckPrime algo_V2
# T.C. -> O(sqrt(n))
def isPrime_V2(n):
    """
    Reason for stopping at sqrt(n)
    Example n = 36 ,

    For every numbers after sqrt(n) its just the replication of the first half in inverse form.

    On writing the Divisor Pair,

    36 = 1*36
    36 = 2*18
    36 = 3*12
    36 = 4*9
    36 = 6*6
    ------------------
    36 = 9*4
    36 = 12*3
    36 = 18*2
    36 = 36*1
    """

    for i in range(2, (int(n**0.5) + 1)):
        if n % i == 0:
            return False
    return True


# Algo V1
# T.C. -> O(upper*k)
# S.C -> O(1)
def algo_V1(lower, upper):
    out = []
    for i in range(lower, upper + 1):
        if isPrime_V1(i):
            out.append(i)
    return out


# Algo V2
# T.C. -> O(upper*sqrt(k))
# S.C -> O(1)
def algo_V2(lower, upper):
    out = []
    for i in range(lower, upper + 1):
        if isPrime_V2(i):
            out.append(i)
    return out


# Algo V3 [Sieve of Erasthothenes]
# T.C. -> O(upper*log(log(upper)))
# S.C  -> O(upper)
def algo_V3(lower, upper):
    # Create an array till upper+1
    prime = [True for _ in range(upper + 1)]

    # Mark the multiples of the current i as False
    for i in range(2, int(upper**0.5) + 1):
        if prime[i]:
            for j in range(i * i, upper + 1, i):
                prime[j] = False

    # Find the primes marked as 1
    out = []
    for i in range(lower, upper + 1):
        if prime[i]:
            out.append(i)

    return out
