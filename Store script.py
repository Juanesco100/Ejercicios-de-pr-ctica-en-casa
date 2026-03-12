def register_sales(sales, product_sales):

    buyer = input("Ingrese su nombre: ")

    number_sales = int(input("Cuantos productos desea comprar: "))

    for i in range(number_sales):

        print("\nVenta", i + 1)

        product = input("Nombre del producto: ")
        price = int(input("Precio unitario: "))
        quantity = int(input("Cantidad vendida: "))

        total_sale = price * quantity

        product_sales.append(product)
        sales.append(total_sale)

        continue_buying = input("Desea agregar otro producto (si/no): ")

        if continue_buying == "no":
            break

    return [product_sales, sales, buyer]


def calculate_total(sales):

    total = sum(sales)

    return total


def show_summary(product_sales, sales, buyer, total):

    print("\n------------- RESUMEN DE LA COMPRA -------------")

    print("Comprador:", buyer)

    print("\nProductos comprados:")

    for i in range(len(product_sales)):
        print(product_sales[i], "- total vendido:", sales[i])

    print("\nTotal pagado:", total)
