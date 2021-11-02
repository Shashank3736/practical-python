# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename: str):
  cost = 0
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    next(rows)
    for row in rows:
      share_price = int(row[1])*(float(row[2]))
      cost = cost + share_price

  return cost

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = './Work/Data/portfolio.csv'
try:
  cost = portfolio_cost(filename)
  print('Total cost',cost)
except FileNotFoundError:
  print("Error: File not available at",filename)