def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices

# Example usage:
product_list = ["Apple", "Banana", "Orange", "Apple", "Grapes", "Apple"]
target_product = "Apple"
result = linear_search_product(product_list, target_product)

if result:
    print(f"{target_product} found at indices: {result}")
else:
    print(f"{target_product} not found in the list.")
