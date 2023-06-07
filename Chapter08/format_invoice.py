subtotal = 12.32
tax = subtotal * 0.07
total = subtotal + tax

print(f"Sub: ${subtotal} Tax: ${tax} Total: ${total}")

print("Sub: ${0} Tax: ${1} Total:${ali}".format(subtotal, tax, ali=total))

print(f"Sub: ${subtotal:0.3f} Tax: ${tax:0.2f} Total: ${total:0.2f}")

print("Sub: ${0:0.2f} Tax: ${1:0.2f} "
      "Total: ${moh:0.2f}".format(subtotal, tax, moh=total)
      )

orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]

print("PRODUCT    QUANTITY    PRICE    SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
        f"{product:10s}{quantity: ^9d}    "
        f"${price: <8.2f}${subtotal: <7.2f}"
    )

import datetime

print("the_date: {%Y-%m-%d %I:%M%p }".format(
    datetime.datetime.now()))
