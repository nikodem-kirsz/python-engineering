from collections import deque

def maximize_conversion(exchange_rates, source_currency):
    max_amounts = {}
    print(max_amounts)
    queue = deque([(source_currency, 1.0)])

    while(queue):
        print(queue)
        current_currency, current_amount = queue.popleft()
        queue.pop

        for pair, rate in exchange_rates.items():
            src, dst = pair[:3], pair[3:]
            if src == current_currency:
                new_amount = current_amount * rate
                if dst not in max_amounts.keys():
                    # print("MAX", max_amounts[dst])
                    max_amounts[dst] = new_amount
                elif new_amount > max_amounts[dst]:
                    max_amounts[dst] = new_amount
                queue.append((dst, new_amount))

    destination = max(max_amounts, key=max_amounts.get) 
    amount = max_amounts[destination]

    return destination, amount       

exchange_rates = {"USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3}
source_currency = "USD"
destination, amount = maximize_conversion(exchange_rates, source_currency)
print(f"The destination currency that maximizes the amount is {destination} with {amount} money.")
