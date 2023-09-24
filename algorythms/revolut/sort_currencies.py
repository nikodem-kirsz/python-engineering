import unittest
"""
You are given a list of transaction currencies.
The goal is to write a function that sorts these currencies from
the most to the least used one.

If two or more currencies appear the same number of times sort the alphabetically

Examples:
    ~ USD, EUR, USD, USD=>USD, EUR
    ~ USD, GBP, EUR=>EUR, GBP, USD
"""

def sort_currencies(currencies):
    occurances = {}
    if not currencies:
        return [] 
    for item in currencies:
        if len(item) > 3:
            currencies = item.split("=>")
            for currency in currencies:
                occurances[currency] = occurances.get(currency, 0) + 1
            print(occurances)
        else:
            occurances[item] = occurances.get(item, 0) + 1 
    
    currencies = [(currency, freq) for currency, freq in occurances.items()]
    print(currencies)
    currencies.sort(key=lambda currency: (-currency[1], currency[0]))
    currencies = [currency for (currency, _) in currencies]
    return currencies


class TestSortCurrencies(unittest.TestCase):
    def test_currencies(self):
        currencies = ["USD", "EUR", "USD", "USD=>USD", "EUR", "PLN", "GBP"]
        sorted_currencies = sort_currencies(currencies)
        self.assertEqual(sorted_currencies, ["USD", "EUR", "GBP", "PLN"])
    def test_empty_currencies(self):
        currencies = []
        sorted_currencies = sort_currencies(currencies)
        self.assertEqual(sorted_currencies, [])    

if __name__ == "__main__":
    unittest.main()