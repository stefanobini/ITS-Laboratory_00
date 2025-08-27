"""Deterministic synthetic data seeder (placeholder).

Students should implement:
  - clear()  : reset tables
  - seed_all(): create partners, products, locations, and initial stock
"""
from faker import Faker
import random

fake = Faker()
random.seed(42)

def clear():
    # TODO: drop or truncate tables as appropriate
    pass

def seed_all(n_products: int = 20, n_partners: int = 10, n_locations: int = 5):
    # TODO: insert rows in DB using SQLAlchemy session
    pass

if __name__ == "__main__":
    clear()
    seed_all()
    print("Seed placeholder executed (no-op).")
