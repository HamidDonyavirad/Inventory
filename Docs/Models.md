# 📦 Models Documentation

This document provides a detailed explanation of the models used in the inventory and order management system.

---
## 🧩 Entities Overview

| Entity                  | Description |
|-------------------------|-------------|
| **User**                | Represents the warehouse manager or system user who creates and manages products,    categories, inventory transactions, and orders. |
| **Product**             | Represents items stored in the warehouse, including details like weight, brand, expiration date, and manufacturing country. |
| **Category**            | Groups similar products together to organize the inventory more effectively. |
| **Inventory**| Records every change in product stock, including inbound (adding new stock), outbound (removing stock), and internal transfers within the warehouse. |
| **Order**               | Represents a transaction that is either a purchase from suppliers or a sale to customers, including metadata like status and related party name. |
| **OrderItem**           | Represents the individual products and their quantities included in each order, along with their price. |

---

## 🛒 Product
Stores information about the products in the system.

| Field | Type | Description |
|------|------|-------------|
| product_name | CharField(max_length=200) | Name of the product |
| product_code | IntegerField(unique=True) | Unique product code |
| weight | FloatField | Weight of the product (in kilograms) |
| color | CharField(max_length=100, null=True, blank=True) | Color (optional) |
| dimensions | CharField(max_length=200, null=True, blank=True) | Dimensions (optional) |
| country_of_manufacture | CharField(max_length=200) | Country of manufacture |
| brand | CharField(max_length=100, null=True, blank=True) | Brand (optional) |
| expiration_date | DateField | Expiration date |
| user | ForeignKey(User, on_delete=CASCADE) | User who created this product |
| category | ForeignKey(Category, on_delete=CASCADE) | Category of the product |

**Methods:**
- `__str__`: Returns a string in the format `product_name - product_code`

---

## 🗂 Category
Represents product categories.

| Field | Type | Description |
|------|------|-------------|
| category_name | CharField(max_length=100) | Category name |
| user | ForeignKey(User, on_delete=CASCADE) | User who created this category |

**Methods:**
- `__str__`: Returns the category name

---

## 📦 Inventory
Tracks inventory movements: inbound, outbound, and internal transfers.

| Field | Type | Description |
|------|------|-------------|
| transaction_type | CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES, default=INBOUND) | Type of transaction |
| unit_type | CharField(max_length=20, choices=UNIT_TYPE_CHOICES, default=WEIGHT) | Unit type (weight or count) |
| quantity | FloatField | Quantity of items moved |
| date | DateTimeField | Date and time of the transaction |
| user | ForeignKey(User, on_delete=CASCADE) | User who created the transaction |
| product | ForeignKey(Product, on_delete=CASCADE) | Related product |

**Methods:**
- `__str__`: Returns the transaction type

---

## 🧾 Order
Represents purchase or sale orders.

| Field | Type | Description |
|------|------|-------------|
| order_number | IntegerField(unique=True) | Unique order number |
| transaction_type | CharField(max_length=10, choices=PURCHASE/SALE, default=PURCHASE) | Type of order |
| role | CharField(max_length=10, choices=CUSTOMER/SUPPLIER, default=CUSTOMER) | Role of the other party |
| role_name | CharField(max_length=100) | Name of the customer or supplier |
| date | DateTimeField | Date and time of the order |
| status | CharField(max_length=20, choices=STATUS_CHOICES, default=In Progress) | Order status (In Progress, Completed, Cancelled) |

**Methods:**
- `__str__`: *(Needs fixing in current code: currently references a non-existing attribute)*

---

## 📦 OrderItem
Represents individual items within an order.

| Field | Type | Description |
|------|------|-------------|
| price | DecimalField(max_digits=10, decimal_places=2) | Price per unit |
| quantity | IntegerField | Quantity of the product |
| order | ForeignKey(Order, on_delete=CASCADE) | Related order |
| product | ForeignKey(Product, on_delete=CASCADE) | Related product |

**Methods:**
- `__str__`: Displays order number and product name

---

## 🧩 Design Notes
- Each model is linked to a user to establish ownership of data.
- Choice fields are used to standardize certain fields (e.g., transaction type, order status).
- Optional fields (like color and brand) allow flexibility.
- The inventory system handles different transaction types separately (inbound, outbound, transfer).

---

🌱 This documentation serves as a quick reference for understanding the models and their relationships. It can be extended with ERD diagrams, business logic explanations, and sample data examples in the future.
