class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # This is absolutely a 2-ptr problem

        buy_day = 0        # Pointer for the day we might buy NeetCoin
        sell_day = 1       # Pointer for the day we might sell NeetCoin (must be after buy_day)
        max_profit = 0     # Tracks the maximum profit found so far

        # Loop through the price list while the sell_day is within bounds
        while sell_day < len(prices):
            
            # If the sell price is higher than the buy price, it's a valid transaction
            if prices[buy_day] < prices[sell_day]:
                
                # Calculate the profit
                current_profit = prices[sell_day] - prices[buy_day]  
                
                # Update max_profit if current is better
                max_profit = max(max_profit, current_profit)         
            else:
                # If the current sell price is lower or equal to the buy price, move the buy_day to sell_day
                # We're always looking for the lowest buy price before a higher sell price
                buy_day = sell_day

            # Move the sell_day pointer forward to the next day
            sell_day += 1

        # Return the best profit found, or 0 if no profit was possible
        return max_profit

# NOTES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 2ptr approach: linear TC, constant SC
# Alt approaches --    
# Brute force w nested loops: O(n^2) TC | O(1) SC
# For an interview, I would brute force first then talk through 2ptr