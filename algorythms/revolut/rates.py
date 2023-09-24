"""
You are given:
1. two currencies (SRC and DST) in the format SRCDST e.g. GBPUSD
2. a dictionary, called rates, of currency pairs and their exchange
   rate, e.g.: ["GRPUSD": 1.35] means that 1 GBP = 1.35 USD

the goal is to write a function that, using exchange rates from the rates
dictionary, finds:
    - the exchange rate from SRC to DST performing the minimum possible number of exchanges
    - list of currencies that were exchanged to get from SRC to DST

   Example:
   You are given set of rates as following rates:
   [GBPRUB: 100, USDGBP: 0.7, GBPEUR: 0.83, EURRUB: 86.3]
   And you have to find the exchange rate from USD to RUB

   The resulting rate would be 70 and is obtained by exchanging USD->GBP->RUB
   USD to GBP => 1 USD = 0.7 GBP
   GBP to RUB => 0.7 GBP = 70 RUB
"""

import unittest
from collections import deque

def currency_rates(SRC, DST, exchange_rates):
    min_path = []
    min_rate = float('-inf')
    for currency, rate in exchange_rates.items():
        src, dst = currency[:3], currency[3:]
        visited = set()
        if src == SRC and currency not in visited:
            path = []
            queue = deque([(src, dst, rate, path + [src, dst])]) # [("USD", "GBP", 0.7)]
            
            while queue:
                current_currency, destination_currency, current_rate, current_path = queue.popleft()
                if current_currency in visited:
                    continue
                visited.add(current_currency)

                for pair, rate in exchange_rates.items():
                    src, dst = pair[:3], pair[3:]  # [("GBP", "RUB", 100)]
                    if src == destination_currency:
                        print(f"current_rate: {current_rate}, rate: {rate}, current_path: {current_path}")
                        new_rate = rate * current_rate
                        current_path = current_path + [dst]
                        print(f"new_rate: {new_rate}, current_path: {current_path}")
                        if dst == DST:
                            if not len(min_path) or len(min_path) > len(current_path):
                                min_path = current_path
                                min_rate = new_rate
                        queue.append((src, dst, new_rate, current_path))

    print(f"min_rate: {min_rate}, min_path: {min_path}")
    if min_rate < 0:
        min_rate = None
    return min_rate, min_path                    

class TestExchangeRates(unittest.TestCase):
    def test_find_exchange_rates(self):
        rates = {"GBPRUB": 100, "USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3}
        exchange_rate, exchange_path = currency_rates("USD", "RUB", rates)
        self.assertEqual(exchange_rate, 70)
        self.assertEqual(exchange_path, ["USD", "GBP", "RUB"])
    def test_does_not_find_exchange_rates(self):
        rates = {"GBPRUB": 100, "USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3}
        exchange_rate, exchange_path = currency_rates("USD", "PLN", rates)
        self.assertEqual(exchange_rate, None)
        self.assertEqual(exchange_path, [])  

if __name__ == "__main__":
    unittest.main()  
