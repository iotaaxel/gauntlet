# gauntlet

## Scenario 
You are going on a camping trip, but before you leave you need to buy groceries. To optimize your time spent in the store, instead of buying the items from your shopping list in order, you plan to buy everything you need from one department before moving to the next.

Given an unsorted list of products with their departments and a shopping list, return the time saved in terms of the number of department visits eliminated.

Example: 
```Python
products = [
    ["Cheese",          "Dairy"],
    ["Carrots",         "Produce"],
    ["Potatoes",        "Produce"],
    ["Canned Tuna",     "Pantry"],
    ["Romaine Lettuce", "Produce"],
    ["Chocolate Milk",  "Dairy"],
    ["Flour",           "Pantry"],
    ["Iceberg Lettuce", "Produce"],
    ["Coffee",          "Pantry"],
    ["Pasta",           "Pantry"],
    ["Milk",            "Dairy"],
    ["Blueberries",     "Produce"],
    ["Pasta Sauce",     "Pantry"]
]

list1 = ["Blueberries", "Milk", "Coffee", "Flour", "Cheese", "Carrots"]
```

For example, buying the items from `list1` in order would take 5 department visits, whereas your method would lead to only visiting 3 departments, a difference of 2 departments.

```Python
Produce(Blueberries)->Dairy(Milk)->Pantry(Coffee/Flour)->Dairy(Cheese)->Produce(Carrots) = 5 department visits
New: Produce(Blueberries/Carrots)->Pantry(Coffee/Flour)->Dairy(Milk/Cheese) = 3 department visits

list2 = ["Blueberries", "Carrots", "Coffee", "Milk", "Flour", "Cheese"] => 2
list3 = ["Blueberries", "Carrots", "Romaine Lettuce", "Iceberg Lettuce"] => 0
list4 = ["Milk", "Flour", "Chocolate Milk", "Pasta Sauce"] => 2
list5 = ["Cheese", "Potatoes", "Blueberries", "Canned Tuna"] => 0
```

All Test Cases:
```Python
shopping(products, list1) => 2
shopping(products, list2) => 2
shopping(products, list3) => 0
shopping(products, list4) => 2
shopping(products, list5) => 0
```
Complexity Variable:
`n`: number of products

## Performance Analysis of Shopping Optimization Algorithm
### Time Complexity
1. Mapping Products to Departments:
   * The loop that creates the product_to_department dictionary iterates over the products list.
   * This takes `O(n)` time, where `n` is the number of products.
3. Calculating Original Visits:
   * The loop that calculates the number of department visits in the original order iterates over the shopping_list.
   * This takes `O(m)` time, where `m` is the number of items in the shopping list.
5. Calculating Optimized Visits:
   * The set comprehension that collects unique departments from the shopping list also iterates over the shopping_list.
   * This takes `O(m)` time.
    
### Space Complexity 
1. Product to Department Mapping:
   * The product_to_department dictionary stores `n` key-value pairs.
   * This takes `O(n)` space.
3. Departments Set:
   * The set that collects unique departments from the shopping list can store up to `m` unique departments.
   * In the worst case, each item in the shopping list belongs to a different department, so the set requires `O(m)` space.
5. Additional Variables:
   * Other variables such as original_visits, last_department, and time_saved use a constant amount of space, i.e., `O(1)`.

### Summary
* Time Complexity: `O(n+m)`, where `n` is the number of products and `m` is the number of items in the shopping list.
Space Complexity: `O(n+m)`, for storing the product-to-department mapping and the set of unique departments.
