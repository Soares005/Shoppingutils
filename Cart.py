def calculate_total_price(cart):
  total_price = 0
  for item in cart:
    total_price += item['preço']
  return total_price
