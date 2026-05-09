import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from categories.models import Category, SubCategory
from products.models import Product

# Categories
electronics, _ = Category.objects.get_or_create(
    name="Electronics",
    defaults={
        "description": "Electronic gadgets"
    }
)

fashion, _ = Category.objects.get_or_create(
    name="Fashion",
    defaults={
        "description": "Fashion products"
    }
)

# Sub Categories
mobiles, _ = SubCategory.objects.get_or_create(
    category=electronics,
    name="Mobiles",
    defaults={
        "description": "Mobile phones"
    }
)

laptops, _ = SubCategory.objects.get_or_create(
    category=electronics,
    name="Laptops",
    defaults={
        "description": "Laptop products"
    }
)

# Products
Product.objects.get_or_create(
    category=mobiles,
    name="iPhone 15",
    defaults={
        "price": 79999,
        "quantity": 10,
        "description": "Latest Apple smartphone"
    }
)

Product.objects.get_or_create(
    category=laptops,
    name="Dell XPS 15",
    defaults={
        "price": 125000,
        "quantity": 5,
        "description": "Premium laptop"
    }
)

print("Demo data inserted successfully!")