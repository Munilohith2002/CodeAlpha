
# Online Python - IDE, Editor, Compiler, Interpreter

class Stock:
    def __init__(self, symbol, shares, price):
        self.symbol = symbol
        self.shares = shares
        self.price = price

class Portfolio:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        self.stocks.append(stock)

    def remove_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
                print(f"{symbol} removed from portfolio.")
                return
        print(f"{symbol} not found in portfolio.")

    def view_portfolio(self):
        if not self.stocks:
            print("Portfolio is empty.")
            return

        print("Portfolio:")
        for stock in self.stocks:
            print(f"Symbol: {stock.symbol}, Shares: {stock.shares}, Price: ${stock.price:.2f}")

def main():
    portfolio = Portfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ")
            shares = int(input("Enter number of shares: "))
            price = float(input("Enter price per share: "))
            stock = Stock(symbol, shares, price)
            portfolio.add_stock(stock)

        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ")
            portfolio.remove_stock(symbol)

        elif choice == "3":
            portfolio.view_portfolio()

        elif choice == "4":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
    