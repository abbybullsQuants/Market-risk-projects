# Simple Parametric Value at Risk (VaR) Calculation
def calculate_var(portfolio_value, volatility, confidence_level=0.95):
    # Z-scores for common confidence levels
    if confidence_level == 0.99:
        z_score = 2.33
    else:
        z_score = 1.645  # Default to 95%
        
    return portfolio_value * volatility * z_score

# Example position
portfolio = 1000000  # 1 Million
daily_vol = 0.02     # 2% daily volatility

var_95 = calculate_var(portfolio, daily_vol, 0.95)
print(f"95% Daily Value at Risk: {var_95:,.2f}")
