sample_input = [3, 2, 1, 3]


def birthdayCakeCandles(ar):
    "Function to determine the number of candles to be blown."
    max_height = max(ar)
    n_of_max_height_candles = 0
    for i in ar:
        if i == max_height:
            n_of_max_height_candles += 1
        else:
            continue
    return n_of_max_height_candles


print(birthdayCakeCandles(sample_input))
