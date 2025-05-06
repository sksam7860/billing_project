S25_samsung_cost = 80_999

# GST Percentages (Total 18%: 9% SGST + 9% CGST)
SGST = 9 / 100
CGST = 9 / 100

print("------- We are selling Samsung S25 mobiles --------\n")
print("------- Each mobile costs ₹80,999 ---------------\n")

# Number of items required by the user
required_items = int(input("No. of required items: "))

# Apply discount based on quantity
if 2 <= required_items <= 5:
    discount = 5 / 100
elif 6 <= required_items <= 10:
    discount = 10 / 100
elif 11 <= required_items <= 20:
    discount = 18 / 100
elif 21 <= required_items <= 40:
    discount = 24 / 100
else:
    discount = 2 / 100

# Calculations
S25_total_cost = required_items * S25_samsung_cost
S25_SGST = S25_total_cost * SGST
S25_CGST = S25_total_cost * CGST
S25_discount_amount = S25_total_cost * discount

# Final total cost
total_cost = S25_total_cost + S25_SGST + S25_CGST - S25_discount_amount

# Output
print("\n------------ Billing Summary --------------------")
print("      Total Samsung Cost        : ₹:", S25_total_cost)
print("      SGST (9%)                 : ₹:",S25_SGST)
print("      CGST (9%)                 : ₹:", S25_CGST)
print("      Discount({}%)              : ₹:{}".format (int(discount*100),S25_discount_amount))
print("\n-------------------------------------------------")
print("      Total Payable Amount      : ₹:", total_cost)
print("\n-------------------------------------------------")
print(".<.<.<    THANK YOU AND VISIT AGAIN    >.>.>.")
