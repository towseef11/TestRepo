prices = [7,1,5,3,6,4]

minPrice = prices[0]
maxProfit = 0

for price in prices :
    if price < minPrice:
        minPrice = price
    
    profit = price - minPrice 
    
    if(profit > maxProfit):
        maxProfit = profit   
print(maxProfit)        