from menu import products


def calculate_tab(consumption: list):
    sum = 0
    for item in consumption:
        price_of_items = 0

        for product in products:
            if product['_id'] == item['_id']:
                price_of_items = product['price'] * item['amount']

        sum = sum + price_of_items
    bill = {'subtotal': f'${round(sum, 2)}'}

    return bill
