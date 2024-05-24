
def check_availability(cart, inventory):
  for item in cart:
    if item['produto'] not in inventory or item['quantidade'] > inventory[item['produto']]:
      return False
  return True
