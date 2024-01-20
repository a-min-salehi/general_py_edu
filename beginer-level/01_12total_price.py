sell_price = 24.75

buy_price = 0.59 * sell_price

send_one_price = 5

send_others_price = 0.62

total_buy = (80 * buy_price + send_one_price) + (send_others_price * 79)

total_sell = 80 * 24.75

print("total buy price is : $",total_buy)

print("total buy sell is : $",total_sell)

print("profit =", total_sell - total_buy)
