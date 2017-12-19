def power(power):
    base = 3
    result = 1
    while power > 0:
        if power % 2 == 1:
            result = (result * base) % 2147483647L

        power = power / 2
        base = (base * base) % 2147483647L

    return result
print power(int(raw_input()))
