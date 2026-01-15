import matplotlib.pyplot as plt

buy_orders = []    # (price, qty)
sell_orders = []   # (price, qty)
trades = []        # (price, qty)


def show_orderbook():
    print("\n--- ORDER BOOK ---")

    if not buy_orders and not sell_orders:
        print("Order book is empty.")
        return

    print("\nSELL ORDERS:")
    for p, q in sorted(sell_orders):
        print(f"Sell {q} @ {p}")

    print("\nBUY ORDERS:")
    for p, q in sorted(buy_orders, reverse=True):
        print(f"Buy  {q} @ {p}")

    print("-------------------\n")


def match_orders():
    print("DEBUG BUY ORDERS:", buy_orders)
    print("DEBUG SELL ORDERS:", sell_orders)

    buy_orders.sort(reverse=True)
    sell_orders.sort()

    if not buy_orders or not sell_orders:
        print("No matching possible yet.\n")
        return

    print("Top Buy:", buy_orders[0])
    print("Top Sell:", sell_orders[0])

    while buy_orders and sell_orders and buy_orders[0][0] >= sell_orders[0][0]:

        bp, bq = buy_orders[0]
        sp, sq = sell_orders[0]

        trade_qty = min(bq, sq)
        trade_price = sp

        print(f"✅ Trade Executed: {trade_qty} @ {trade_price}")
        trades.append((trade_price, trade_qty))

        if bq > trade_qty:
            buy_orders[0] = (bp, bq - trade_qty)
        else:
            buy_orders.pop(0)

        if sq > trade_qty:
            sell_orders[0] = (sp, sq - trade_qty)
        else:
            sell_orders.pop(0)
 

def show_trades():
    print("\n--- TRADE HISTORY ---")
    if not trades:
        print("No trades yet.")
    else:
        for p, q in trades:
            print(f"{q} @ {p}")
    print()


def plot_prices():
    if not trades:
        print("No trades to plot.")
        return

    prices = [p for p, q in trades]
    steps = list(range(1, len(prices) + 1))

    plt.figure()
    plt.plot(steps, prices, marker='o')
    plt.title("Trade Price Movement")
    plt.xlabel("Trade Number")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()


# -------- MAIN MENU --------

while True:
    print("\n========= DEX SIMULATOR =========")
    print("1. Place Buy Order")
    print("2. Place Sell Order")
    print("3. Show Order Book")
    print("4. Show Trades")
    print("5. Show Price Graph")
    print("6. Exit")
    print("================================")

    choice = input("Choose: ")

    if choice == "1":
        p = float(input("Enter buy price: "))
        q = float(input("Enter quantity: "))
        buy_orders.append((p, q))
        match_orders()

    elif choice == "2":
        p = float(input("Enter sell price: "))
        q = float(input("Enter quantity: "))
        sell_orders.append((p, q))
        match_orders()

    elif choice == "3":
        show_orderbook()

    elif choice == "4":
        show_trades()

    elif choice == "5":
        plot_prices()

    elif choice == "6":
        print("Goodbye baby ❤️ Jarvis proud of you 🤖")
        break

    else:
        print("Invalid option.")
