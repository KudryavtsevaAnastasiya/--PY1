money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while True: # пока справедливо
    delta = spend - salary # разница = расходы - зарплата
    if delta > money_capital: # если разница превышает финансовую подушку безопасности
        break

    month += 1
    money_capital -= delta
    spend *= 1 + increase

print(month)  # 8
