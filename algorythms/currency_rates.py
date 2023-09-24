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

"""
Python patterns.
How does garbage collector is working?
How are implemented dicts?
Postgresql isolations
"""


def find_exchange_rate(src, dst, rates): # "USD", "RUB", [GBPRUB: 100, USDGBP: 0.7, GBPEUR: 0.83, EURRUB: 86.3]
    def dfs(currency, visited):
        if currency == dst: # base condition => USD == USD
            return 1.0, [currency]
        visited.add(currency)
        min_rate = float('inf')
        min_path = []

        for pair, rate in rates.items():
            src_currency, dst_currency = pair[:3], pair[3:]
            if currency == src_currency and dst_currency not in visited:
                rate_to_dst, path_to_dst = dfs(dst_currency, visited) # Recursion ends sets 1.0, []
                # Recursion returns, it gets to the last node where currency equals dst end returns
                if rate * rate_to_dst < min_rate:
                    min_rate = rate * rate_to_dst
                    min_path = [currency] + path_to_dst

        visited.remove(currency)
        return min_rate, min_path        

    rate, path = dfs(src, set()) # recursively start looking from currency = src
    return rate, path    

# Example usage:
rates = {"GBPRUB": 100, "USDGBP": 0.7, "GBPEUR": 0.83, "EURRUB": 86.3}
src = "USD"
dst = "PLN"
exchange_rate, path = find_exchange_rate(src, dst, rates)

if exchange_rate is not None:
    print(f"The exchange rate from {src} to {dst} is {exchange_rate}")
    print(f"Exchange path: {' -> '.join(path)}")
else:
    print(f"No exchange rate found from {src} to {dst}")


"""
Input:
A directed graph represented as an adjacency list, where each node is associated with a list of its outgoing edges, and each edge includes the destination node and its weight.
The source node and the destination node.

Output:
The shortest path from the source node to the destination node.
The total weight (distance) of the shortest path.
"""

def shortest_path(src, dst, graph):
    def dfs(current, visited):
        if current == dst:
            return [current], 1
        visited.add(current)
        min_path = []
        total_weight = float('inf')

        for pair in graph[current]:
            current_node, current_weight = pair[0], pair[1]
            if (current_node not in visited):
                path_to_node, weight_to_node = dfs(pair[0], visited)
                if weight_to_node * current_weight < total_weight:
                    min_path = [current] + path_to_node
                    total_weight = current_weight * weight_to_node
        visited.remove(current)

        return min_path, total_weight    

    if src not in graph or dst not in graph:
        return [], 0
    
    path, weight = dfs(src, set())

    return path, weight


graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('D', 3)],
    'D': []
}

path, weight = shortest_path('A', 'D', graph)
print(f'Path: {path}')
print(f'Weight: {weight}')