# Shipping Cost Calculator
## Input Package Weight and Shipping Rate

weight=float(input("enter the package in kilograms"))
rate=float(input("enter the shipping rate per kilogram"))

shipping_cost = weight * rate 

print(f"Shipping Cost : {shipping_cost} USD")
