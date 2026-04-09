def max_profit(prices):
    is_profit = 0
    
    if not prices:
        return 0
    
    for i in range(len(prices)):
        for j in range(i+1,len(prices)-1):
            if (prices[j+1] - prices[i]) > is_profit:
                is_profit = prices[j+1] - prices[i]
    return(is_profit)

print(max_profit([7, 6, 4, 3, 1]))