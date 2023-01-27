from menu import products


def get_product_by_id(product_id: int):

    if type(product_id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if product['_id'] == product_id:
            return product
    return {}


def get_products_by_type(product_type: str):
    result = []

    if type(product_type) != str:
        raise TypeError("product type must be a str")

    for product in products:
        if product['type'] == product_type:
            result.append(product)
    return result


def add_product(menu: list, **new_product: dict):
    _id = 0

    id_list = []

    if len(menu) > 0:
        for product in menu:
            id_list.append(product['_id'])
        _id = max(id_list, key=int)

    new_product['_id'] = _id + 1

    menu.append(new_product)

    return new_product


def menu_report():
    product_count = len(products)
    sum_price = 0
    types = set()
    list_of_types = []
    type_freq = []

    for product in products:
        sum_price = sum_price + product['price']
        types.add(product['type'])
        list_of_types.append(product['type'])

    for type in types:
        freq = list_of_types.count(type)
        type_freq.append((type, freq))

    bigger = (type_freq[0])

    for type in type_freq:

        if type[1] > bigger[1]:
            bigger = type

    average_price = round(sum_price / product_count, 2)
    most_common_type = bigger[0]

    return f'Products Count: {product_count} - Average Price: \
${average_price} - Most Common Type: {most_common_type}'


def add_product_extra(menu: list, *required_keys: tuple, **new_product: dict):
    _id = 0

    id_list = []

    for required_key in required_keys:
        if new_product.get(required_key) is None:
            raise KeyError(f"field {required_key} is required")

    for key in list(new_product):
        try:
            required_keys.index(key)
        except ValueError:
            new_product.pop(key)

    if len(menu) > 0:
        for product in menu:
            id_list.append(product['_id'])
        _id = max(id_list, key=int)

    new_product['_id'] = _id + 1

    menu.append(new_product)

    return new_product
