def stockmax(prices):
    profit = 0
    sharesBought = 0
    moneySpent = 0

    maxStockPrices = sorted(prices)
    maxStockPrice = maxStockPrices.pop()
    
    print('maxStockPrice: ', maxStockPrice)
    for i in range(len(prices)):
        print(f'Profit: {profit}, shareBought: {sharesBought}, moneySpent: {moneySpent}')
        if prices[i] == maxStockPrice:
            print('inside selling for: ', maxStockPrice)
            profit += (sharesBought * maxStockPrice) - moneySpent
            sharesBought = 0
            moneySpent = 0

            maxStockPrice = maxStockPrices.pop()
            print("max: ", maxStockPrice)
        else:
            print('inside buying for: ', prices[i])
            sharesBought += 1
            moneySpent += prices[i]    
    return profit
        
print(stockmax([1,2, 100]))