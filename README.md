# fundamental-analysis
Python script for calculation of fair price of the stock based on company financial indicators. The formulae was getting from Artyom Khachatryan lectures.

## Usage
In root folder in Terminal run `python3 investing.py a` (also `python3 investing.py eps`) or `python3 investing.py b` (also `python3 investing.py bv`). 

You will need to type some financial indicators of the company that you've analyzed. 
For type A: net profit margin in the start of analyzed period, net profit margin in the end of analyzed period, the number of periods (for example, for 5-year analyzing period you need to type 4) and average of P/E for last 5 years. 
For type B situation is similar, you need to enter: book value in the start, book value in the end, the number of periods and average of P/BV on 1 stock for last 5 years.

### What is 'fair' price?
This is a price of the stock at which the stock is good for buying but this is NOT a signal for buying in 100% cases. This is only a sign to follow this stock more carefully.
