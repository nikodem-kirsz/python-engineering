import unittest
from collections import deque


def maximize_conversion(exchange_rates, source):
    max_amounts = {}

    queue = deque([(source, 1.0)])
    visited = set()

    while queue:
        current_currency, current_rate = queue.popleft() # "USD, 1.0"
        if current_currency in visited:
            continue
        visited.add(current_currency)

        for pair, rate in exchange_rates.items(): # "USD_EUR"
            src, dst = pair[:3], pair[4:]
            if src == current_currency and dst not in visited:
                new_amount = rate * current_rate
                if dst not in max_amounts.keys():
                    max_amounts[dst] = new_amount
                elif max_amounts[dst] < new_amount:
                        max_amounts[dst] = new_amount
                queue.append((dst, new_amount))
        
    desination = max(max_amounts)
    amount = max_amounts[desination]
    return desination, amount

class TestMaximizeConversion(unittest.TestCase):

    def test_maximize_conversion(self):
        exchange_rates = {"USD_GBP": 0.7, "GBP_EUR": 0.83, "EUR_RUB": 86.3}
        result = maximize_conversion(exchange_rates, "USD")
        self.assertEqual(("RUB", 0.7 * 0.83 * 86.3), result)

if __name__ == "__main__":
    unittest.main()