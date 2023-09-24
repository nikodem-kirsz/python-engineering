"""
Write a Python function that takes a set of currency exchange rates and finds the arbitrage opportunity, 
if any, in a given set of currencies. An arbitrage opportunity is a situation where you can make a risk-free profit 
by exploiting differences in exchange rates between multiple currencies. 
Your function should detect whether such an opportunity exists and, 
if so, return the sequence of currency conversions that lead to the arbitrage profit.
"""

import unittest
from collections import deque

def arbitrage_opportunity(exchange_rates):
    for start_currency, start_rate in exchange_rates.items():
        start_path = [start_currency[:3], start_currency[3:]]
        queue = deque([(start_currency[:3], start_currency[3:], start_rate, start_path)]) # (initial_currency, current_currency, destination_currency, rate, path)
        visited = set()
        
        while queue:
            initial_currency, current_currency, current_rate, current_path = queue.popleft() # "USDGBP": 0.7"

            if current_currency in visited:
                continue
            visited.add(current_currency)

            for pair, rate in exchange_rates.items():
                if pair not in visited:
                    src, dest = pair[:3], pair[3:] # "GBPEUR": 0.83"
                    if src == current_currency:
                        print(f"Calculating new rate: {current_rate} * {rate} = {current_rate * rate}")
                        current_rate = current_rate * rate
                        current_path = current_path + [dest]
                        if dest == initial_currency: # arbitrage detected
                            print(f"Arbitrary detected: {dest}")
                            if current_rate > 1.0:
                                return current_rate, current_path
                        queue.append((initial_currency, dest, current_rate, current_path))
    return False                         


class TestArbitrageOpportunity(unittest.TestCase):
    def test_is_arbitrage_opportunity(self):
        exchange_rates = {"USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3, "RUBUSD": 200}
        current_rate, current_path = arbitrage_opportunity(exchange_rates)
        self.assertEqual(current_rate, 0.7 * 0.83 * 86.3 * 200)
        self.assertEqual(current_path, ["USD", "GBP", "EUR", "RUB", "USD"])

    def test_no_arbitrage_opportunity(self):
        exchange_rates = {"USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3}
        opportunity = arbitrage_opportunity(exchange_rates)
        self.assertEqual(opportunity, False)


if __name__ == "__main__":
    unittest.main()