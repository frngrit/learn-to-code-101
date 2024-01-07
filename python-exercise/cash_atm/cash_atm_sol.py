def atm(amount):
    result = {}
    banks = [1000, 500, 100]
    for bank in banks:
        bank_count = amount // bank
        amount -= bank_count * bank
        result[bank] = bank_count
    
    return result