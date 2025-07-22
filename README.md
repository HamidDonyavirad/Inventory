# 📦 Inventory Management API

The goal of this project is to design and implement a powerful and flexible API for the comprehensive management of warehouse operations and order processing. This system can serve as a central core within logistics management software, online stores, distribution companies, and other businesses that deal with inventory and order registration. The designed API will be capable of connecting to other systems (such as websites, sales applications, or accounting systems).

## 🚀 Features

- Real-time stock tracking
- Record product entries and exits
- Define detailed product info (SKU, weight, color, etc.)
- Categorize products 
- Inventory reports and valuation
- Order  management


## 📄 Documentations

- [Models](Docs/Models.md)
- [Serializers](Docs/Serializers.md)
- [Views](Docs/Views.md)



## 🧪 Tests

For this inventory management project, I used the built-in `unittest` framework in Python to write and run unit tests. This helps ensure the reliability and correctness of the application's core functionality.

- [Models](inventory/tests/test_models.py)
- [Views](inventory/tests/test_views.py)
- [Serializers](inventory/tests/test_Serializers.py)


## 🧰 Tech Stack

- Python, Django, DRF
- PostgreSQL
- JWT Authentication


## 🔧 Setup

```bash
git clone https://github.com/HamidDonyavirad/Inventory.git
cd Inventory
python -m venv env
or env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
