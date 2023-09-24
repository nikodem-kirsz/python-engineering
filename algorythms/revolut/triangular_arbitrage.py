import unittest
from collections import deque

def triangular_arbitrage(exchange_rates):
    for start_currency, start_rate in exchange_rates.items():
        queue = deque([(start_currency[:3], start_currency[4:], start_rate, [start_currency[:3], start_currency[4:]])])
        visited = set()
        while queue:
            start_currency, current_currency, current_rate, current_path = queue.popleft() #  "USD_EUR"

            if current_currency in visited:
                continue
            visited.add(current_currency)

            for pair, rate in exchange_rates.items():
                src, dst = pair[:3], pair[4:] # "EUR_GBP"
                if src == current_currency and dst not in visited:
                    new_rate = current_rate * rate
                    new_path = current_path + [dst]
                    if len(new_path) == 4 and dst == start_currency:
                        return (new_path, new_rate)
                    queue.append((start_currency, dst, new_rate, new_path))
    return ([], None)
            




class TestTriangularArbitrage(unittest.TestCase):

    def test_there_is_triangular_arbitrage(self):
        exchange_rates = {"USD_EUR": 0.83,"EUR_GBP": 0.75,"GBP_USD": 1.2}
        result = triangular_arbitrage(exchange_rates)
        self.assertEqual((["USD", "EUR", "GBP", "USD"], 0.83 * 0.75 * 1.2), result)

    def test_there_isnt_triangular_arbitrage(self):
        exchange_rates = {"USD_EUR": 0.83,"EUR_GBP": 0.75,"GBP_RBL": 1.2}
        result = triangular_arbitrage(exchange_rates)
        self.assertEqual(([], None), result)

if __name__ == "__main__":
    unittest.main()