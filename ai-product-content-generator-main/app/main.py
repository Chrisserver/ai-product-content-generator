from fetch_data import fetch_product_data
from generate_description import generate_description
from save_output import save_to_file
from db import save_to_mysql

"""
    Main pipeline to fetch product data, generate SEO description, and save results.
"""

def run_pipeline(product_name):
    print("Fetching product data...")
    product_data = fetch_product_data(product_name)

    if not product_data:
        print("Product not found.")
        return

    print("Generating SEO description...")
    description = generate_description(product_data[0])

    print("Saving results...")
    save_to_file(product_name, description)
    save_to_mysql(product_name, description)

    print("\n✅ Done!")
    print(description)


if __name__ == "__main__":
    product_name = input("Enter product name: ")
    run_pipeline(product_name)
