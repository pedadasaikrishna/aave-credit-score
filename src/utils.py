import datetime

def unix_to_datetime(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp)

def normalize_amount(amount_str):
    return float(amount_str) / (10 ** 6)  # Assuming 6 decimals like USDC

def calculate_usd_value(amount_str, price_str):
    return float(amount_str) * float(price_str) / (10 ** 6)
