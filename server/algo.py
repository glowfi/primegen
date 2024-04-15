# CheckPrime algo_V1
# T.C. -> O(n)
async def isPrime_V1(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# CheckPrime algo_V2
# T.C. -> O(sqrt(n))
async def isPrime_V2(n):
    for i in range(2, (int(n**0.5) + 1)):
        if n % i == 0:
            return False
    return True


# Algo V1
# T.C. -> O(upper*k)
async def algo_V1(lower, upper):
    out = []
    for i in range(lower, upper + 1):
        isPrime = await isPrime_V1(i)
        if isPrime:
            out.append(i)
    return out


# Algo V2
# T.C. -> O(upper*sqrt(k))
async def algo_V2(lower, upper):
    out = []
    for i in range(lower, upper + 1):
        isPrime = await isPrime_V2(i)
        if isPrime:
            out.append(i)
    return out


# Algo V3
# T.C. -> O(upper*log(log(upper)))
async def algo_V3(lower, upper):
    prime = [True for _ in range(upper + 1)]
    p = 2
    while p * p <= upper:
        if prime[p]:
            for i in range(p * p, upper + 1, p):
                prime[i] = False
        p += 1

    out = []
    for p in range(lower, upper + 1):
        if prime[p]:
            out.append(p)

    return out
