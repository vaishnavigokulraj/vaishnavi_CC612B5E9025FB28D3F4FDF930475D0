def linear_search_product(products, target_product):
    indices = []
    for index, product in enumerate(products):
        if product == target_product:
            indices.append(index)
    return indices

# Example usage:
product_list = ["Apple", "Banana", "Orange", "Apple", "Mango", "Apple"]
target = "Apple"
result = linear_search_product(product_list, target)

if result:
    print(f"The product '{target}' was found at indices: {result}")
else:
    print(f"The product '{target}' was not found in the list.")
