# Data Dictionary (to be completed by the team)

## Tables
- **product**
  - id (PK, int)
  - sku (string, unique)
  - name (string)
  - ...
- **partner**
  - id (PK, int)
  - type (enum: supplier|customer)
  - name, email, phone, address (personal data — minimize)
  - ...
- **location**
  - id (PK, int)
  - code (string, unique)
  - description (string)
  - ...
- **movement**
  - id (PK, int)
  - ts (datetime)
  - type (IN|OUT|TRANSFER)
  - product_id (FK)
  - qty (numeric)
  - from_location_id (FK, nullable)
  - to_location_id (FK, nullable)
  - reason (enum), note (text)
  - ...

## Views
- **v_stock** — current stock by product/location (IN−OUT), indexes suggested.

## Constraints, Indexes & Notes
- FKs defined; uniqueness on natural keys; indexes on hot queries
- Nullability rules aligned to business logic
