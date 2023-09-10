"""
You are given a list of transaction currencies.
The goal is to write a function that sorts these currencies from
the most to the least used one.

If two or more currencies appear the same number of times sort the alphabetically

Examples:
    ~ USD, EUR, USD, USD=>USD, EUR
    ~ USD, GBP, EUR=>EUR, GBP, USD
"""

def sort_currencies(transactions_list):
    currency_occurrences = {}
    for transaction in transactions_list: # O(n)
        currencies = transaction.split("=>")
        for currency in currencies: # O(1)
            currency_occurrences[currency] = currency_occurrences.get(currency, 0) + 1
    # O(n)
    currencies = [(currency, occurances) for currency, occurances in currency_occurrences.items()] 
    currencies.sort(key=lambda currency: (currency[1], currency[0]))   
            
    return currencies

# def sort_currencies_sophisticated(transactions_list):
#     currency_occurrences = {currency: sum(1 for trans in transactions_list if currency in trans.split("=>"))
#                             for currency in set(currency for trans in transactions_list for currency in trans.split("=>"))}

#     return currency_occurrences

print(sort_currencies(["USD", "EUR", "USD=>USD", "EUR=>EUR"]))