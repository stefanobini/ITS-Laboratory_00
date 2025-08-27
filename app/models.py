"""SQLAlchemy ORM models.

NOTE: Students define the full ER model here (tables, FKs, uniqueness, indexes).
Example (to be replaced by the team's schema):

    class Product(Base):
        __tablename__ = "product"
        id = mapped_column(Integer, primary_key=True)
        sku = mapped_column(String, unique=True, index=True, nullable=False)
        name = mapped_column(String, nullable=False)

"""
from .database import Base
# from sqlalchemy.orm import mapped_column, relationship
# from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint, Index
