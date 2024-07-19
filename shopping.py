import unittest

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

class TestShopping(unittest.TestCase):
    
    def setUp(self):
        self.products = [
            ["Cheese", "Dairy"], ["Carrots", "Produce"], ["Potatoes", "Produce"],
            ["Canned Tuna", "Pantry"], ["Romaine Lettuce", "Produce"], ["Chocolate Milk", "Dairy"],
            ["Flour", "Pantry"], ["Iceberg Lettuce", "Produce"], ["Coffee", "Pantry"],
            ["Pasta", "Pantry"], ["Milk", "Dairy"], ["Blueberries", "Produce"],
            ["Pasta Sauce", "Pantry"]
        ]
    
    def test_list1(self):
        shopping_list = ["Blueberries", "Milk", "Coffee", "Flour", "Cheese", "Carrots"]
        result = shopping(self.products, shopping_list)
        self.assertEqual(result, 2)
    
    def test_list2(self):
        shopping_list = ["Blueberries", "Carrots", "Coffee", "Milk", "Flour", "Cheese"]
        result = shopping(self.products, shopping_list)
        self.assertEqual(result, 2)
    
    def test_list3(self):
        shopping_list = ["Blueberries", "Carrots", "Romaine Lettuce", "Iceberg Lettuce"]
        result = shopping(self.products, shopping_list)
        self.assertEqual(result, 0)
    
    def test_list4(self):
        shopping_list = ["Milk", "Flour", "Chocolate Milk", "Pasta Sauce"]
        result = shopping(self.products, shopping_list)
        self.assertEqual(result, 2)
    
    def test_list5(self):
        shopping_list = ["Cheese", "Potatoes", "Blueberries", "Canned Tuna"]
        result = shopping(self.products, shopping_list)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
