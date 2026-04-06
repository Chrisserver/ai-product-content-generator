import os
from openai import OpenAI
from dotenv import load_dotenv

"""
    This module generates high-quality SEO product descriptions using OpenAI's GPT model
    It takes product data as input and returns an optimized description that is clear and made for business
"""

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_description(product_data):
    prompt = f"""
    Write a high-quality SEO product description.

    Product Title: {product_data["title"]}
    Category: {product_data["category"]}
    Price: {product_data["price"]}
    Existing Description: {product_data["description"]}

    Requirements:
    - Optimized for SEO
    - Clear and engaging
    - Include keywords naturally
    """

    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
