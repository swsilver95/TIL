N = int(input())
numbers = list(map(int, input().split()))

def find_prime(N):
    prime_numbers = set()
    check = [True] * (N + 1)
    check[0] = False
    check[1] = False

    n = int(N ** 0.5)
    for i in range(2, n + 1):
        if check[i]:
            for j in range(2 * i, N + 1, i):
                check[j] = False

    for k in range(2, N + 1):
        if check[k]:
            prime_numbers.add(k)

    return prime_numbers


prime = find_prime(1000)
answer = 0
for number in numbers:
    if number in prime:
        answer += 1

print(answer)

