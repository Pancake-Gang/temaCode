def SeiveOfEratosthenes(nth):
    list = [True] * (nth + 1)
    list[0] = list[1] = False  # Handle 0 and 1 separately
    
    for i in range(2,int(nth**0.5) + 1):
        if list[i]:
            for j in range(i*i,nth+1,i):
                list[j] = False
    
    primes = []
    for x in range(len(list)):
        if list[x]:
            primes.append(x)
    
    return primes

prime_list = SeiveOfEratosthenes(2_000_000)

summation = 0
for prime in prime_list:
    if prime > 2_000_000:
        break
    summation += prime

print(summation)

