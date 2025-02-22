# Title of the app
print("Currency Converter (PKR to USD, GBP, CNY, RUB, INR)")

# Predefined conversion rates (You can replace with live API in real-world scenarios)
exchange_rates = {
    "USA (USD)": 279.50,  # Example conversion rate from PKR to USD
    "UK (GBP)": 353.16,   # Example conversion rate from PKR to GBP
    "China (CNY)": 38.56,  # Example conversion rate from PKR to CNY
    "Russia (RUB)": 3.16,  # Example conversion rate from PKR to RUB
    "India (INR)": 3.23   # Example conversion rate from PKR to INR
}

# Input field for Pakistani Rupees (PKR)
pkr_amount = float(input("Enter amount in Pakistani Rupees (PKR): "))

# Dropdown to select target currency
currency_to = input("Select the target currency (USD, GBP, CNY, RUB, INR): ").strip().upper()

# Ensure the selected currency is valid
valid_currencies = ["USD", "GBP", "CNY", "RUB", "INR"]
if currency_to not in valid_currencies:
    print("Invalid currency selection. Please select one of: USD, GBP, CNY, RUB, INR.")
else:
    # Perform conversion if amount is valid
    if pkr_amount > 0:
        # Get the corresponding conversion rate
        currency_key = f"{currency_to} ({currency_to.upper()})"
        converted_amount = pkr_amount * exchange_rates[currency_key]
        
        # Display the result
        print(f"{pkr_amount} PKR is equal to {converted_amount:.2f} {currency_key}")
    else:
        print("Please enter a valid amount greater than 0 PKR.")
