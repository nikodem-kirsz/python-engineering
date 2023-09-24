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

def currency_rates(SRC, DST, rates):

    def find_rate(SRC, visited):
        if SRC == DST:
            print(f"inside return path: {[SRC]}")
            return 1.0, [SRC]
        visited.add(SRC)
        min_rate = float('-inf')
        min_path = []
        
        for exchange, rate in rates.items():
            src, dst = exchange[:3], exchange[3:] # GBP, RUB
            if src == SRC and dst not in visited: # to prevent cyclic graph dfs
                local_rate, local_path = find_rate(dst, visited)
                print(f"local_rate: {local_rate}, local_path: {local_path}")
                if min_rate < local_rate * rate:
                    min_rate = local_rate * rate
                    min_path = [src] + local_path
        
        visited.remove(SRC)
        return min_rate, min_path
    
    rate, best_path = find_rate(SRC, set())

    if (rate < 0): rate = None

    return rate, best_path


class TestCurrencyExchange(unittest.TestCase):
    def test_exchange_rate(self):
        rates = {"GBPRUB": 100, "RUBUSD": 10, "USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3, "EURPLN": 12}
        exchange_rate, _ = currency_rates("USD", "RUB", rates)
        print(f"\nCurrency exchange for rates: USD => RUB: {exchange_rate}\n")
        self.assertEqual(exchange_rate, 70)

        exchange_rate, _ = currency_rates("USD", "EUR", rates)
        print(f"\nCurrency exchange for rates: USD => EUR: {exchange_rate}\n")
        self.assertEqual(exchange_rate, 0.7 * 0.83)

        exchange_rate, _ = currency_rates("GBP", "PLN", rates)
        print(f"\nCurrency exchange for rates: GBP => PLN: {exchange_rate}\n")
        self.assertEqual(exchange_rate, 0.83 * 12)

        exchange_rate, _ = currency_rates("GBP", "GRU", rates)
        print(f"\nCurrency exchange for rates: GBP => GRU: {exchange_rate}\n")
        self.assertEqual(exchange_rate, None)

    def test_currency_path(self):
        rates = {"GBPRUB": 100, "USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3}
        _, exchange_path = currency_rates("USD", "RUB", rates)
        print(f"\nCurrency path for rates: USD => RUB: {exchange_path}")
        self.assertEqual(exchange_path, ["USD", "GBP", "RUB"])

if __name__ == "__main__":
    unittest.main()