# Leetcode -121

##### Brut Force #####

lst = list(map(int, input().split()))
max = 0

for i in range(len(lst)):
    for j in range(i,len(lst)):
        if lst[j]-lst[i] > max:
            max = lst[j]-lst[i]

print(max)


##### Updated #####

class Solution(object):
    def maxProfit(self, prices):

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit