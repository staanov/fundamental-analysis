import sys


def calcutate_rate_of_growth(start, end, periods):
    rate_of_growth = (end / start)**(1/periods)
    return rate_of_growth


def estimate_conservative_rate_of_growth(rate_of_growth):
    rate = (rate_of_growth - 1) * 100
    if rate >= 20:
        return 20
    elif rate >= 15:
        return 15
    elif rate >= 10:
        return 10
    else:
        return 0
    

def calculate_fair_price(start, end, periods, avg):
    rate_of_growth = calcutate_rate_of_growth(start, end, periods)
    future_rate = (estimate_conservative_rate_of_growth(rate_of_growth) / 100) + 1
    future_eps_or_bv = future_rate**periods * end
    future_price = future_eps_or_bv * avg
    fair_price = future_price / (1.3**periods)
    return fair_price

try:
    type_of_calculation = sys.argv[1].lower()
except IndexError:
    type_of_calculation = None

if (type_of_calculation == 'a' or type_of_calculation == 'eps'):
    net_profit_start = float(input('Enter net profit start value: '))
    net_profit_end = float(input('Enter net profit end value: '))
    periods = int(input('Enter number of periods: '))
    avg_pe = float(input('Enter average P/E for last 5 years: '))
    fair_price = calculate_fair_price(net_profit_start, net_profit_end, periods, avg_pe)
    print('Fair price: ' + str(fair_price))
elif (type_of_calculation == 'b' or type_of_calculation == 'bv'):
    book_value_start = float(input('Enter book value start value: '))
    book_value_end = float(input('Enter book value end value: '))
    periods = int(input('Enter number of periods: '))
    avg_pbv = float(input('Enter average P/BV for last 5 years: '))
    fair_price = calculate_fair_price(book_value_start, book_value_end, periods, avg_pbv)
    print('Fair price: ' + str(fair_price))
else:
    print('Choose type as command-line arg: a (through EPS) or b (through BV)')
