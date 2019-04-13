def round_sum(a, b, c):
    rounded_values = [int(round(num, -1)) for num in (a, b, c)]
    return sum(rounded_values)