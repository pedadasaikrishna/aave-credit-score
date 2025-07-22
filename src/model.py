from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def train_and_score(features_df):
    X = features_df.drop(columns=['wallet'])
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    y_dummy = (X_scaled[:, 1] * 0.6 + X_scaled[:, 2] * 0.3 - X_scaled[:, 3] * 0.1) * 1000  # mock scoring logic
    y_dummy = np.clip(y_dummy, 0, 1000)

    model.fit(X_scaled, y_dummy)
    scores = model.predict(X_scaled)

    result = features_df[['wallet']].copy()
    result['credit_score'] = scores.round(2)
    return result
