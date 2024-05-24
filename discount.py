


def apply_discount(cart, discount):

  discounted_cart = []
  for item in cart:
    discounted_price = item['preço'] * (1 - discount)
    discounted_cart.append({'produto': item['produto'], 'preço': discounted_price})
  return discounted_cart
