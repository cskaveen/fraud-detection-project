'''def check_fraud(transaction):
    reasons = []

    # Rule 1: High amount
    if transaction["amount"] > 10000:
        reasons.append("High transaction amount")

    # Rule 2: Too many recent transactions
    if transaction["transactions_last_min"] > 3:
        reasons.append("Too many transactions in 1 minute")

    return reasons
    '''
def check_fraud(transaction):
    reasons = []

    # Rule 1: High amount
    if transaction["amount"] > 10000:
        reasons.append("High transaction amount")

    # Rule 2: Too many transactions
    if transaction["transactions_last_min"] > 3:
        reasons.append("Too many transactions in 1 minute")

    # Rule 3: Night-time transaction
    hour = int(transaction["timestamp"][11:13])
    if hour >= 23 or hour <= 5:
        reasons.append("Unusual transaction time")

    return reasons

