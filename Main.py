from script import register_sales, calculate_total, show_summary

sales = []
product_sales = []

data = register_sales(sales, product_sales)

product_sales = data[0]
sales = data[1]
buyer = data[2]

total = calculate_total(sales)

show_summary(product_sales, sales, buyer, total)
