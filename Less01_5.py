
profit = int(input("Введите доход: "))
costs = int(input("Введите расходы: "))
if profit > costs:
    profitability = profit-costs
    rent = profitability/profit
    print(f"{profitability} рентабельность!")
    worker = int(input("Сколько у вас работников: "))
    print(f"Рентабельность:{profitability/worker} на одного работника!")
elif profit == costs:
    print("Не плохо, вы держитесь на плаву")
else:
    print("Удачи")