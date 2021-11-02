# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename: str):
  cost = 0
  with open(filename, 'rt') as f:
    next(f)
    for line in f:
      row = line.split(',')
      if len(row) != 3:
        continue
      share_price = int(row[1])*(float(row[2]))
      cost = cost + share_price

  return cost

cost = portfolio_cost('./Work/Data/portfolio.csv')
print('Total cost',cost)