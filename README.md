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

- [Models](Models.md)
- [Serializers](Serializers.md)
- [Views](Views.md)


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
