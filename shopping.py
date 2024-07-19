def shopping(products, shopping_list):
    # Create a dictionary to map products to departments
    product_to_department = {}
    for product, department in products:
        product_to_department[product] = department
    
    # Determine the number of department visits in the original order
    original_visits = 0
    last_department = None
    for item in shopping_list:
        department = product_to_department[item]
        if department != last_department:
            original_visits += 1
            last_department = department
    
    # Determine the number of department visits in the optimized order
    departments = set(product_to_department[item] for item in shopping_list)
    optimized_visits = len(departments)
    
    # Calculate the time saved in terms of department visits eliminated
    time_saved = original_visits - optimized_visits
    
    return time_saved

# Test cases
products = [
    ["Cheese", "Dairy"], ["Carrots", "Produce"], ["Potatoes", "Produce"],
    ["Canned Tuna", "Pantry"], ["Romaine Lettuce", "Produce"], ["Chocolate Milk", "Dairy"],
    ["Flour", "Pantry"], ["Iceberg Lettuce", "Produce"], ["Coffee", "Pantry"],
    ["Pasta", "Pantry"], ["Milk", "Dairy"], ["Blueberries", "Produce"],
    ["Pasta Sauce", "Pantry"]
]

list1 = ["Blueberries", "Milk", "Coffee", "Flour", "Cheese", "Carrots"]
list2 = ["Blueberries", "Carrots", "Coffee", "Milk", "Flour", "Cheese"]
list3 = ["Blueberries", "Carrots", "Romaine Lettuce", "Iceberg Lettuce"]
list4 = ["Milk", "Flour", "Chocolate Milk", "Pasta Sauce"]
list5 = ["Cheese", "Potatoes", "Blueberries", "Canned Tuna"]

print(shopping(products, list1))  # => 2
print(shopping(products, list2))  # => 2
print(shopping(products, list3))  # => 0
print(shopping(products, list4))  # => 2
print(shopping(products, list5))  # => 0
