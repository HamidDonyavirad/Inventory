# 📦 Serializers Documentation

This document describes the serializers used in the project, their purpose, and related fields.

---

## 👤 RegisterSerializer
| Item | Details |
|-----|--------|
| **Type** | ModelSerializer |
| **Model** | User |
| **Purpose** | Handles user registration by accepting username, email, and password. |
| **Fields** | username, email, password |
| **Notes** | - Password is write-only for security. <br> - Uses a custom `create` method to hash the password correctly with `create_user`. |

---

## 🛒 ProductSerializer
| Item | Details |
|-----|--------|
| **Type** | ModelSerializer |
| **Model** | Product |
| **Purpose** | Serializes product data including optional fields and related category. |
| **Fields** | id, product_name, product_code, weight, color, dimensions, country_of_manufacture, brand, expiration_date, user, category |
| **Notes** | - Fields `color`, `dimensions`, and `brand` are optional and can be left blank. <br> - `user` is read-only and represented by username using `SlugRelatedField`. |

---

## 🗂 CategorySerializer
| Item | Details |
|-----|--------|
| **Type** | ModelSerializer |
| **Model** | Category |
| **Purpose** | Serializes category data. |
| **Fields** | id, category_name, user |

---

## 📦 InventorySerializer
| Item | Details |
|-----|--------|
| **Type** | ModelSerializer |
| **Model** | Inventory |
| **Purpose** | Serializes inventory transactions (inbound, outbound, transfer). |
| **Fields** | id, transaction_type, quantity, date, user, product |

---

## 🧾 OrderSerializer
| Item | Details |
|-----|--------|
| **Type** | ModelSerializer |
| **Model** | Order |
| **Purpose** | Serializes purchase and sale orders. |
| **Fields** | id, order_number, transaction_type, costomer_or_supplier_choices, date, status |
| **Notes** | *Consider reviewing the field name `costomer_or_supplier_choices` for clarity or renaming.* |

---

## 📦 OrderItemSerializer
| Item | Details |
|-----|--------|
| **Type** | ModelSerializer |
| **Model** | OrderItem |
| **Purpose** | Serializes individual items included in an order. |
| **Fields** | id, price, quantity, order, product |

---

## 🧩 Design Notes
- All serializers are based on DRF’s `ModelSerializer` for simplicity and direct mapping to models.
- Optional fields (like `color`, `dimensions`, `brand` in `ProductSerializer`) allow flexibility in API.
- `RegisterSerializer` uses a custom `create` method to securely create a new user.
- `SlugRelatedField` in `ProductSerializer` makes the API more readable by showing the username instead of the raw user ID.

---

🌱 This documentation is meant to help developers understand how data is transformed between models and API responses/requests.
