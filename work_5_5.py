with open('random.txt', 'w', encoding='utf-8') as ran:
    ran.write(f"{' '.join([str(i) for i in range(1, 51)])}")
with open('random.txt', 'r', encoding='utf-8') as ran:
    numbers = [int(n) for n in ran.read().split()]
    print(sum(numbers))
