import requests

"""
    This module fetches product data from a dummy API based on the product name provided by the user.
"""

def fetch_product_data(product_name):
    url = "https://dummyjson.com/products"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()["products"]
    except Exception as e:
        return e.printstacktrace()

    return [product for product in products 
            if product_name.lower() in product["title"].lower()
        ]
