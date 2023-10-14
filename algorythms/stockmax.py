# def stockmax(prices):
#     profit = 0
#     sharesBought = 0
#     moneySpent = 0

#     maxStockPrices = sorted(prices)
#     maxStockPrice = maxStockPrices.pop()
    
#     print('maxStockPrice: ', maxStockPrice)
#     for i in range(len(prices)):
#         print(f'Profit: {profit}, shareBought: {sharesBought}, moneySpent: {moneySpent}')
#         if prices[i] == maxStockPrice:
#             print('inside selling for: ', maxStockPrice)
#             profit += (sharesBought * maxStockPrice) - moneySpent
#             sharesBought = 0
#             moneySpent = 0

#             maxStockPrice = maxStockPrices.pop()
#             print("max: ", maxStockPrice)
#         else:
#             print('inside buying for: ', prices[i])
#             sharesBought += 1
#             moneySpent += prices[i]    
#     return profit
        
# print(stockmax([1,2, 100]))

def stockmax(prices):
    profit = 0
    shares_bought = 0
    money_spent = 0
    max_stock_prices = sorted(prices)
    max_stock_price = max_stock_prices.pop()

    for i in range(len(prices)):
        if max_stock_price == prices[i]: # Sell
            profit += (shares_bought * max_stock_price) - money_spent
            shares_bought = 0
            money_spent = 0
        else: # Buy
            shares_bought += 1
            money_spent += prices[i]

    return profit


print(stockmax([1,1,3,5,3,2,7]))