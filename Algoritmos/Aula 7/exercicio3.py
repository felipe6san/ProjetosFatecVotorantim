num = int(input("Digite seu número: "))
primo = True
num_div = 0
for i in range(1, num + 1):
    if (num % i) == 0:
        num_div = num_div + 1
if num_div > 2:
    primo = False
if primo:
    print(f"O número {num} é primo!!")
else:
    print(f"O número {num} não é primo!!")
