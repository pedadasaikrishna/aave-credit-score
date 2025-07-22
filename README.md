# Aave V2 Wallet Credit Scorer

This project uses raw transaction data from Aave V2 to assign credit scores to user wallets based on behavior such as deposits, borrows, and liquidations.

## Scoring Range
- **0–1000 scale** — higher scores = more trustworthy DeFi users.

## Architecture
1. **JSON Parsing** from raw input
2. **Feature Engineering**: deposits, borrows, liquidation count, asset diversity
3. **Modeling**: RandomForestRegressor trained on synthetic weights
4. **Output**: Wallet + Credit Score CSV

## Run It

```bash
bash run.sh
