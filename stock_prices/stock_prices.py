#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit_so_far = -10000000000
  current_min_price_so_far = prices[0]
  for i in range(len(prices)):

    if i == 0: 
      current_min_price_so_far = prices[0]
      continue

    profit = prices[i] - current_min_price_so_far
    
    if profit > max_profit_so_far:
      max_profit_so_far = profit

    if prices[i] < current_min_price_so_far:
      current_min_price_so_far = prices[i]

  
  return max_profit_so_far

print(find_max_profit([100, 90, 80, 50, 20, 10]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))