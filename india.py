# def converter():
#     a = int(input("Enter amount in Indian currency: "))
#     d = 80  
#     def calculate():
#         print("Converted amount:", a * d)
    
#     calculate()

# converter()




# class Converter:
#     def __init__(self, rupee_to_usd):
#         rupee_to_usd = int(input("rupee"))

#         self.rupee_to_usd = rupee_to_usd
    
#     def convert(self, amount, currency):
#         if currency.lower() == "usd":
#             print("Converted amount in USD: ", amount * self.rupee_to_usd)
#         else:
#             print("Unsupported currency")

# converter = Converter("usd")  
# converter.convert(80, "usd")


exchange_rates = {
    'USD': 1.0,    
    'EUR': 0.85,   # Euro
    'GBP': 0.72,   # British Pound
    'INR': 74.5,   # Indian Rupee
    'JPY': 110.0,  # Japanese Yen
    'AUD': 1.35,   # Australian Dollar
    'CAD': 1.25,   # Canadian Dollar
    'SGD': 1.34,   # Singapore Dollar
    'CHF': 0.92,   # Swiss Franc
    'CNY': 6.45,   # Chinese Yuan
    'MYR': 4.17    # Malaysian Ringgit
}


def print_currencies():

    print("Supported currencies:")
    for currency in exchange_rates:
        print(f"- {currency}")

def convert_currency(amount, from_currency, to_currency):
    
    amount_in_usd = amount / exchange_rates[from_currency]

    converted_amount = amount_in_usd * exchange_rates[to_currency]
    return converted_amount





def main():
    
    print("Welcome to the Currency Converter!")
    print_currencies()

    while True:


        amount = input("\nEnter the amount (or 'q' to quit): ").strip()
        if amount.lower() == 'q':
            print("Thank you for using the Currency Converter. Goodbye!")
            break

        try:
            amount = float(amount)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue




        from_currency = input("Enter the source currency (e.g., USD): ").upper()
        to_currency = input("Enter the target currency (e.g., EUR): ").upper()



        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            print("Unsupported currency. Please check your input.")
            continue



        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()