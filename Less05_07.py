import json

with open('7.json', 'w') as f:
    with open('7.txt', encoding='utf-8') as f2:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f2}
        result = [profit, {'average_profit': round(sum([int(i) for i in profit.values() if int(i) > 0]) / len([int(i) for i in profit.values() if int(i) > 0]))}]

    json.dump(result, f, ensure_ascii=False, indent=4)
