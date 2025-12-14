salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0

cur_spend = spend

for _ in range(months):
    deficit = cur_spend - salary
    if deficit > 0:
        money_capital += deficit

    cur_spend *= (1 + increase)  # рост цен со следующего месяца

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
