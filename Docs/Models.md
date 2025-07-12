# 📦 Models Documentation

This document provides a detailed explanation of the models used in the inventory and order management system.

---
## 🧩 Entities Overview

| Entity                  | Description |
|-------------------------|-------------|
| **User**                | Represents the warehouse manager or system user who creates and manages products,    categories, inventory transactions, and orders. |
| **Product**             | Represents items stored in the warehouse, including details like weight, brand, expiration date, and manufacturing country. |
| **Category**            | Groups similar products together to organize the inventory more effectively. |
| **InventoryTransaction**| Records every change in product stock, including inbound (adding new stock), outbound (removing stock), and internal transfers within the warehouse. |
| **Order**               | Represents a transaction that is either a purchase from suppliers or a sale to customers, including metadata like status and related party name. |
| **OrderItem**           | Represents the individual products and their quantities included in each order, along with their price. |

---
