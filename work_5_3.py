with open('salary.txt', 'r', encoding='utf-8') as n:
    subnames = []
    aver_income = 0
    num = 0
    for line in n:
        num += 1
        subname, income = (i for i in line.split())
        income = int(income)
        if income <= 20000:
            subnames.append(subname)
        aver_income += income
    aver_income /= num
print(*subnames, aver_income, sep='\n')