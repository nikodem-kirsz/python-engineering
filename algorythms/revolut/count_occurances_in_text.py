import re

def count_currency_occurrences(text):
    # Regular expression pattern to match uppercase letter combinations of length 3 or more
    pattern = r'\b[A-Z]{3,}\b'
    
    # Find all matches of currency codes in the text
    matches = re.findall(pattern, text)
    
    # Count the occurrences of each currency code
    currency_counts = {}
    for currency_code in matches:
        if currency_code in currency_counts:
            currency_counts[currency_code] += 1
        else:
            currency_counts[currency_code] = 1
    
    return currency_counts

# Example usage:
text = """This is a sample text document containing currency codes like USD, EUR, and GBP. 
But it may also have other words in uppercase, such as USDollar or EURope. 
You should count the occurrences of uppercase letter combinations of length 3 or more as currency codes."""
result = count_currency_occurrences(text)
print(result)
