#!/usr/bin/python

import sys

trade_days = int(sys.argv[1])
ticker = sys.argv[2]

#print trade_days
#print ticker

stock_file = ticker + '.csv'
#print stock_file

closing_stock_price = []

fh = open(stock_file)
lines = fh.readlines()[1:trade_days]
for row in lines:
   price = row.split(',')[4]
   price_float = float(price)
   #print price_float
   closing_stock_price.append(price_float)

#print closing_stock_price

stock_close_average = sum(closing_stock_price)/trade_days
print "average stock close: " + str(stock_close_average)
