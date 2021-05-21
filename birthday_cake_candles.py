# You are in charge of the cake for a child's birthday.
# You have decided the cake will have one candle for each year
# of their total age. They will only be able to blow out the
# tallest of the candles. Count how many candles are tallest.

# Example
# candles = [4,4,1,3]
# The maximum height candles are 4 units high.
# There are 2 of them. So return 2.

def birthdayCakeCandles(candles):
    # Sort candle in descending order
    sortedCandles = sorted(candles, reverse=True)

    # It starts with 1 because 
    # There is always 1 candle to be the tallest one.
    count = 1

    # Start the loop from index 1
    for candle in sortedCandles[1:]:
        if sortedCandles[0] == candle:
            count += 1
    
    return count