print(2 ** 3) # ^ does not work for exponent but ** works as an exponent

def raise_to_power(base_num, pow_num):
    result = 1
    print(base_num ** pow_num)
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))