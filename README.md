# ShopDjango — Django Ecommerce Store

A role-based ecommerce platform built with Python + Django using Function-Based Views (FBV), inspired by Amazon's UI.

---

# Features

* Role-based authentication (Admin/User)
* Category CRUD operations
* Subcategory CRUD operations
* Product CRUD operations
* Product search and filtering
* Shopping cart system
* Quantity validation
* Responsive Bootstrap UI
* Amazon-inspired design
* Function-Based Views only
* Demo fixtures and seed data
* CI-ready GitHub structure

---

# Tech Stack

* **Backend:** Python 3.11+ · Django 5
* **Frontend:** Bootstrap 5 · Bootstrap Icons · Django Templates
* **Database:** SQLite (development) → PostgreSQL (production)
* **Image Handling:** Pillow
* **Environment Variables:** python-decouple
* **Package Manager:** uv
* **CI/CD:** GitHub Actions

---

# Screenshots

## Login Page

Add screenshot here:

```plaintext
docs/screenshots/login.png
```

## Categories Page

Add screenshot here:

```plaintext
docs/screenshots/categories.png
```

## Products Page

Add screenshot here:

```plaintext
docs/screenshots/products.png
```

## Cart Page

Add screenshot here:

```plaintext
docs/screenshots/cart.png
```

---

# Project Structure

```plaintext
shop/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── accounts/
├── cart/
├── categories/
├── products/
│
├── core/
│
├── docs/
│   ├── PRD.md
│   └── screenshots/
│
├── fixtures/
│   ├── categories.json
│   ├── subcategories.json
│   └── products.json
│
├── media/
│   └── demo/
│
├── scripts/
│   └── seed_data.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│
├── .env.example
├── .gitignore
├── manage.py
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock
```

---

# Quick Start (uv)

## Clone Repository

```bash
git clone <your-repository-url>
cd shop
```

## Install Dependencies

```bash
uv sync
```

## Create `.env`

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
ALLOWED_HOSTS=127.0.0.1,localhost
```

## Run Migrations

```bash
uv run python manage.py migrate
```

## Load Demo Data

```bash
uv run python manage.py loaddata fixtures/categories.json
uv run python manage.py loaddata fixtures/subcategories.json
uv run python manage.py loaddata fixtures/products.json
```

## Run Server

```bash
uv run python manage.py runserver
```

Open:

```plaintext
http://127.0.0.1:8000
```

---

# Demo Accounts

## Admin Account

```plaintext
Email: admin@example.com
Password: StoreMaster@2026
```

## User Account

```plaintext
Email: user1@example.com
Password: ShopEasy#2026
```

---

# Navigation Flow

1. Register/Login
2. Categories
3. Subcategories
4. Products
5. Cart

---

# Key URLs

| URL                   | Description     |
| --------------------- | --------------- |
| `/categories/`        | Categories page |
| `/products/`          | Products page   |
| `/cart/`              | Cart page       |
| `/accounts/login/`    | Login           |
| `/accounts/register/` | Register        |

---

# Admin Features

* Create categories
* Update categories
* Delete categories
* Manage subcategories
* Manage products
* Update stock quantity

---

# User Features

* Browse categories
* Browse products
* Search products
* Add to cart
* Update cart
* Remove cart items

---

# Security Features

* CSRF Protection
* Role-based authorization
* Password hashing
* Quantity validation
* Environment variable support

---

# Future Enhancements

* Payment gateway integration
* Product reviews and ratings
* Wishlist
* Order management
* Admin analytics dashboard
* REST API with DRF
* JWT authentication

---

# Why This Project?

This project was built to practice:

* Django Function-Based Views
* Ecommerce workflows
* Role-based authentication
* CRUD operations
* Cart management
* Responsive UI design
* Project structuring
* GitHub-ready project organization

---

# License

MIT License
