# def function(length):
#     otp=""   
#     for i in range(1,length):
#       otp+=Math.floor(Math.random()*10)
#       print(i)

import random

def generate_otp(length):
    otp = ""   
    for i in range(length):
        otp += str(random.randint(0, 9))
    print(otp)
    
generate_otp(6)  




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



    # exchangerates = {
#     'USD': 1.0,       # United States Dollar
#     'EUR': 0.85,      # Euro
#     'GBP': 0.72,      # British Pound
#     'INR': 74.5,      # Indian Rupee
#     'JPY': 110.0,     # Japanese Yen
#     'AUD': 1.35,      # Australian Dollar
#     'CAD': 1.25,      # Canadian Dollar
#     'SGD': 1.34,      # Singapore Dollar
#     'CHF': 0.92,      # Swiss Franc
#     'CNY': 6.45,      # Chinese Yuan
#     'MYR': 4.17,      # Malaysian Ringgit
#     'NZD': 1.42,      # New Zealand Dollar
#     'KRW': 1180.0,    # South Korean Won
#     'RUB': 75.0,      # Russian Ruble
#     'ZAR': 15.0,      # South African Rand
#     'BRL': 5.25,      # Brazilian Real
#     'MXN': 20.0,      # Mexican Peso
#     'HKD': 7.78,      # Hong Kong Dollar
#     'SEK': 8.65,      # Swedish Krona
#     'NOK': 8.85,      # Norwegian Krone
#     'DKK': 6.35,      # Danish Krone
#     'THB': 33.0,      # Thai Baht
#     'IDR': 14500.0,   # Indonesian Rupiah
#     'PHP': 50.0,      # Philippine Peso
#     'TRY': 8.5,       # Turkish Lira
#     'SAR': 3.75,      # Saudi Riyal
#     'AED': 3.67,      # UAE Dirham
#     'PLN': 3.95,      # Polish Zloty
#     'CZK': 22.0,      # Czech Koruna
#     'HUF': 300.0,     # Hungarian Forint
#     'ILS': 3.25,      # Israeli New Shekel
#     'ARS': 95.0,      # Argentine Peso
#     'CLP': 800.0,     # Chilean Peso
#     'COP': 3800.0,    # Colombian Peso
#     'EGP': 15.7,      # Egyptian Pound
#     'NGN': 410.0,     # Nigerian Naira
#     'PKR': 170.0,     # Pakistani Rupee
#     'VND': 23000.0,   # Vietnamese Dong
#     'BDT': 85.0,      # Bangladeshi Taka
#     'KWD': 0.30,      # Kuwaiti Dinar
#     'QAR': 3.64,      # Qatari Riyal
#     'OMR': 0.38,      # Omani Rial
#     'BHD': 0.38,      # Bahraini Dinar
#     'JOD': 0.71,      # Jordanian Dinar
#     'LKR': 200.0,     # Sri Lankan Rupee
#     'NPR': 120.0,     # Nepalese Rupee
#     'MMK': 1800.0,    # Myanmar Kyat
#     'KHR': 4100.0,    # Cambodian Riel
#     'LAK': 9500.0,    # Lao Kip
#     'MNT': 2850.0,    # Mongolian Tugrik
#     'UZS': 10500.0,   # Uzbekistani Som
#     'KZT': 430.0,     # Kazakhstani Tenge
#     'TWD': 28.0,      # New Taiwan Dollar
#     'XCD': 2.7,       # East Caribbean Dollar
#     'BBD': 2.0,       # Barbadian Dollar
#     'BZD': 2.0,       # Belize Dollar
#     'BSD': 1.0,       # Bahamian Dollar
#     'PAB': 1.0,       # Panamanian Balboa
#     'GYD': 210.0,     # Guyanese Dollar
#     'HTG': 100.0,     # Haitian Gourde
#     'JMD': 150.0,     # Jamaican Dollar
#     'TTD': 6.75,      # Trinidad and Tobago Dollar
#     'XPF': 110.0,     # CFP Franc
#     'XAF': 550.0,     # Central African CFA Franc
#     'XOF': 550.0,     # West African CFA Franc
#     'DJF': 180.0,     # Djiboutian Franc
#     'GNF': 10000.0,   # Guinean Franc
#     'KGS': 85.0,      # Kyrgyzstani Som
#     'MVR': 15.4,      # Maldivian Rufiyaa
#     'MUR': 40.0,      # Mauritian Rupee
#     'SCR': 15.0,      # Seychellois Rupee
#     'SLL': 10000.0,   # Sierra Leonean Leone
#     'SOS': 580.0,     # Somali Shilling
#     'TJS': 11.0,      # Tajikistani Somoni
#     'TMT': 3.5,       # Turkmenistani Manat
#     'UAH': 28.0,      # Ukrainian Hryvnia
#     'UGX': 3700.0,    # Ugandan Shilling
#     'ZMW': 20.0,      # Zambian Kwacha
#     'ZWL': 360.0      # Zimbabwean Dollar
# }
# def print_currencies():
#     print("Supported currencies:")
#     for currency in exchangerates:
#         print(f"- {currency}")

# def convert_currency(amount, from_currency, to_currency):
#     if from_currency not in exchangerates or to_currency not in exchangerates:
#         raise ValueError("Unsupported currency.")

#     # Convert the amount to USD first
#     amount_in_usd = amount / exchangerates[from_currency]
    
#     # Convert the USD amount to the target currency
#     converted_amount = amount_in_usd * exchangerates[to_currency]
#     return converted_amount

# def main():
#     print("Welcome to the Siddharth Currenct converter Converter!")
#     print_currencies()

#     while True:
#         amount = input("\nEnter the amount (or 'q' to quit): ").strip()
#         if amount.lower() == 'q':
#             print("Thank you for using the Currency Converter. Goodbye!")
#             break

#         try:
#             amount = float(amount)
#         except ValueError:
#             print("Invalid amount. Please enter a numeric value.")
#             continue

#         from_currency = input("Enter the source currency (e.g., USD): ").upper()
#         to_currency = input("Enter the target currency (e.g., EUR): ").upper()

#         if from_currency not in exchangerates or to_currency not in exchangerates:
#             print("Unsupported currency. Please check your input.")
#             continue

#         converted_amount = convert_currency(amount, from_currency, to_currency)
#         print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

# if __name__ == "__main__":
#     main()

