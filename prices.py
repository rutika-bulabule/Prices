import sys

if len(sys.argv) < 2:
    print("Usage: python prices.py price1 price2 price3 ...")
    sys.exit(1)
else:
    prices = [float(p) for p in sys.argv[1:]]

    maximum = max(prices)
    minimum = min(prices)
    average_price = sum(prices) / len(prices)

    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Average price:", average_price)