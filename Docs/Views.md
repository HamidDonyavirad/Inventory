# 📦 Views Documentation

This document explains the Django REST Framework (DRF) views in the project: what each does, how they work, and how they fit into the system.

---

## ✅ Overview
- Built using **Django REST Framework (DRF)**.
- Uses **JWT authentication** with `rest_framework_simplejwt`.
- Each view extends from `APIView` for detailed method handling.
- Supports CRUD operations for multiple models: Product, Category, Inventory, Order, and OrderItem.
- Includes an extra endpoint to calculate live stock using aggregation.

---

## 🧩 Views and Their Purposes

### 🔹 RegisterView
| Item | Details |
|-----|--------|
| Method | `POST` |
| Purpose | Register a new user (requires username, email, password). |
| Permissions | `AllowAny` (authentication not needed). |
| Notes | Returns success message on valid data; validation errors otherwise. |

---

### 🔹 LogoutView
| Item | Details |
|-----|--------|
| Method | `POST` |
| Purpose | Logs out a user by blacklisting the provided refresh token. |
| Authentication | Requires `JWTAuthentication` and `IsAuthenticated`. |
| Notes | Responds with error if token is missing, invalid, or expired. |

---

### 🔹 ProductView
| Method | Purpose |
|------|--------|
| `GET` | List all products. |
| `POST` | Create a new product. |
| `PUT` | Fully update a product by primary key (`pk`). |
| `PATCH` | Partially update a product by `pk`. |
| `DELETE` | Delete a product by `pk`. |
| Authentication | Requires `JWTAuthentication` and `IsAuthenticated`. |

---

### 🔹 CategoryView
| Method | Purpose |
|------|--------|
| `GET` | List all categories. |
| `POST` | Create a new category. |
| `PUT` | Update a category by `pk`. |
| `DELETE` | Delete a category by `pk`. |
| Authentication | Requires authentication. |

---

### 🔹 InventoryView
| Method | Purpose |
|------|--------|
| `GET` | List all inventory records (both inbound and outbound). |
| `POST` | Add a new inventory record. |
| `DELETE` | Delete an inventory record by `pk`. |
| Authentication | Requires authentication. |

---

### 🔹 OrderView
| Method | Purpose |
|------|--------|
| `GET` | List all orders. |
| `POST` | Create a new order. |
| `DELETE` | Delete an order by `pk`. |
| Authentication | Requires authentication. |

---

### 🔹 OrderLineView
| Method | Purpose |
|------|--------|
| `GET` | List all order items. |
| `POST` | Create a new order item. |
| `DELETE` | Delete an order item by `pk`. |
| Authentication | Requires authentication. |

---

### 🔹 ProductStockView
| Method | Purpose |
|------|--------|
| `GET` | Calculate and return the current stock of a product (by `pk`). |
| Details | Computes total inbound minus total outbound quantities. |
| Response | Includes product name, product ID, and current stock. |
| Authentication | Requires authentication. |

---

## ⚙️ Technical Details
- **JWT authentication:** Required for protected endpoints.
- **Serializers:** Validate incoming data and format outgoing data.
- **Status codes:** Uses correct HTTP responses (e.g., `201 Created`, `204 No Content`, `400 Bad Request`).
- **Aggregation:** Stock is calculated with Django's `aggregate` + `Sum`.

---

## 📌 Summary
These views together create a secure RESTful API for managing users, products, categories, inventory, and orders.  
They follow DRF best practices and add a stock-check endpoint that reflects real-time data.
