primos = []
i = 0
n = 100

while i < 10:
    for k in range(2, n // 2):
        primo = True
        if (n % k) == 0:
            primo = False
            break
    if primo:
        primos.append(n)
        i = i + 1

    n = n + 1
t = tuple(primos)

for x in range(len(t)):
    print(t[x], end=' - ')
