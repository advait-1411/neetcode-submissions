class Solution:
    def maxProfit(self,prices):
        if len(prices)<=1:
            return 0

        buy_index = 0
        sell_index = 1
        max_profit= 0

        while buy_index<sell_index and sell_index<len(prices):
            # lower buying price possible
            if prices[sell_index]<prices[buy_index]:
                buy_index = sell_index
                sell_index += 1

            # Profit
            elif prices[sell_index]>prices[buy_index]:
                max_profit = max(prices[sell_index]-prices[buy_index], max_profit)
                sell_index += 1

            # loss
            else:
                sell_index += 1

        return max_profit
