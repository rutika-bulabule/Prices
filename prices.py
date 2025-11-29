import sys

print("Usage: python prices.py price 1, price 2, price 3 ")
sys.exit(1)

price=[float(price)for price in sys.argv[1:]] 

print("Maximum:",maximum)
print("Minimum:",minimum)
print("Average price:", average_price)