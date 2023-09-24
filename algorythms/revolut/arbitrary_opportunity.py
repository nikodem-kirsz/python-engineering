import unittest
from collections import deque

"""
1.Iterate over all pairs to find arbitrage
"""

def find_arbitrage_opportunity(exchange_rates):
    for start_currency in exchange_rates:
        queue = deque([(start_currency[:3], start_currency[:3], 1.0)])
        # print('Queue', queue)
        visited = set()
        while queue:
            # print('Poping from queue', queue)
            initial_currency, current_currency, current_rate = queue.popleft()
            
            if current_currency in visited:
                continue

            visited.add(current_currency)

            for pair, rate in exchange_rates.items():
                src, dst = pair[:3], pair[3:]
                print(f"{src}, {current_currency}")
                if src == current_currency:
                    new_rate = current_rate * rate # Calculate exchange rate
                    print(f"max_rate after calc: {new_rate}")
                    print(f"{dst}, {start_currency}")
                    if dst == initial_currency:
                        print(f"Reaching arbitrary currency: {dst}")
                        print(f"New rate is: {new_rate}")
                        if new_rate > 1.0:
                            print(f"Arbitrage opportunity found: {start_currency} => {initial_currency} with rate {new_rate}")
                            return True
                    queue.append((initial_currency, dst, new_rate))   

    return False                    

exchange_rates = {"USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3, "RUBUSD": 112}

print(find_arbitrage_opportunity(exchange_rates))


class TestArbitraryOpportunity(unittest.TestCase):
    def arbitraty_opportunity(self):
        exchange_rates = {"USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3, "RUBUSD": 0.012}
        self.assertEqual(find_arbitrage_opportunity(exchange_rates), True)

    def no_arbitraty_opportunity(self):
        exchange_rates = {"USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3}
        self.assertEqual(find_arbitrage_opportunity(exchange_rates), False)


if __name__ == "__main__":
    unittest.main()