import pandas as pd
from utils import normalize_amount, calculate_usd_value, unix_to_datetime

def engineer_features(df):
    df['datetime'] = df['timestamp'].apply(unix_to_datetime)
    df['usd_value'] = df.apply(lambda row: calculate_usd_value(row['actionData']['amount'], row['actionData']['assetPriceUSD']), axis=1)
    
    grouped = df.groupby('userWallet')

    features = pd.DataFrame({
        'wallet': grouped.size().index,
        'total_txn_count': grouped.size().values,
        'total_usd_deposited': grouped.apply(lambda x: x[x['action'] == 'deposit']['usd_value'].sum()).values,
        'total_usd_borrowed': grouped.apply(lambda x: x[x['action'] == 'borrow']['usd_value'].sum() if 'borrow' in x['action'].values else 0).values,
        'num_liquidations': grouped.apply(lambda x: (x['action'] == 'liquidationcall').sum()).values,
        'unique_assets': grouped.apply(lambda x: x['actionData'].apply(lambda a: a['assetSymbol']).nunique()).values,
        'first_seen': grouped['timestamp'].min().values,
        'last_seen': grouped['timestamp'].max().values,
    })

    features['activity_days'] = (features['last_seen'] - features['first_seen']) / (3600 * 24)
    features = features.fillna(0)
    return features
