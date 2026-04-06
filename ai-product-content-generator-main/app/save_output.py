import json
from datetime import datetime
import os

"""
    This module saves the generated SEO descriptions to a JSON file.
"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(BASE_DIR, "data", "outputs.json")

def save_to_file(product_name, description):
    data = {
        "product": product_name,
        "description": description,
        "timestamp": str(datetime.now())
    }

    try :
       with open(DIR, "r") as f:
            lines = json.load(f)
    except FileNotFoundError:
        lines = []

    lines.append(data)
    with open(DIR, "w") as f:
        json.dump(lines, f, indent=4)
