from yahoo_fin.stock_info import get_data, get_day_gainers, get_day_losers

amazon_weekly = get_data("tsla", start_date="12/04/2009", end_date="1/04/2021", index_as_date = False, interval="1wk")
print(amazon_weekly)

# gainers = get_day_losers()
# print(type(gainers))
