# Product Requirements Document (PRD)

# Python + Django Ecommerce Store

## 1. Project Overview

### Project Name
Django Ecommerce Store

### Tech Stack
- Backend: Python + Django
- Frontend: HTML5, CSS3, Bootstrap/Tailwind CSS, JavaScript
- Database: SQLite (Development), PostgreSQL/MySQL (Production)
- Template Engine: Django Templates
- Authentication: Django Authentication System
- Architecture Pattern: Function-Based Views (FBV)

### Project Goal
Build a role-based ecommerce website inspired by Amazon-style UI/UX where:
- Admin users can perform full CRUD operations.
- Normal users can browse categories, subcategories, and products.
- Users can add products to cart and manage cart items.
- The platform provides a clean, responsive, user-friendly shopping experience.

---

# 2. User Roles

## 2.1 Admin Role
Admin users will be able to:
- Login/Register
- Manage Categories (Create, Read, Update, Delete)
- Manage Sub Categories (Create, Read, Update, Delete)
- Manage Products (Create, Read, Update, Delete)
- Search categories, subcategories, and products
- View all products
- Manage inventory quantity

## 2.2 User Role
Users will be able to:
- Register/Login
- Browse Categories
- Browse Sub Categories
- Browse Products
- Search Categories/Sub Categories/Products
- Add products to cart
- View cart
- Remove products from cart
- Update product quantity in cart

---

# 3. Functional Requirements

# 3.1 Authentication Module

## Features
- User Registration
- User Login
- Logout
- Role-based access control

## User Flow
1. User enters website.
2. User chooses:
   - Register
   - Login
3. User selects role:
   - Admin
   - User
4. After successful login:
   - Redirect to Category Page

## Validation Rules
- Email must be unique.
- Password must be encrypted.
- Required field validation.
- Session management.

---

# 3.2 Category Module

## Category Fields
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| name | String | Category Name |
| image | ImageField | Category Image |
| description | TextField | Category Description |
| created_at | DateTime | Auto Timestamp |
| updated_at | DateTime | Auto Timestamp |

## Admin Features
- Add category
- Edit category
- Delete category
- View category list
- Search category by name

## User Features
- View categories
- Search categories
- Open related subcategories

## UI Requirements
- Grid-based category cards
- Category image thumbnail
- Hover effect
- Responsive layout
- Search bar on top

---

# 3.3 Sub Category Module

## Sub Category Fields
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| category | ForeignKey(Category) | Parent Category |
| name | String | Sub Category Name |
| image | ImageField | Sub Category Image |
| description | TextField | Description |
| created_at | DateTime | Auto Timestamp |
| updated_at | DateTime | Auto Timestamp |

## Admin Features
- Add sub category
- Edit sub category
- Delete sub category
- View sub category list
- Search sub category by name

## User Features
- View sub categories
- Search sub categories
- Open products page

## UI Requirements
- Amazon-style product card layout
- Responsive grid
- Sidebar filters
- Search functionality

---

# 3.4 Product Module

## Product Fields
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| category | ForeignKey(SubCategory) | Product Category |
| name | String | Product Name |
| image | ImageField | Product Image |
| price | DecimalField | Product Price |
| quantity | IntegerField | Stock Quantity |
| description | TextField | Product Description |
| created_at | DateTime | Auto Timestamp |
| updated_at | DateTime | Auto Timestamp |

## Admin Features
- Add product
- Edit product
- Delete product
- View product list
- Search products by name
- Update stock quantity

## User Features
- View products
- Search products
- Add products to cart
- View product details

## UI Requirements
- Amazon-like product cards
- Product image preview
- Product title
- Product price
- Add to Cart button
- Hover animation
- Responsive mobile design
- Search bar

---

# 3.5 Cart Module

## Cart Features
- Add product to cart
- Remove product from cart
- Update cart quantity
- View cart items
- Calculate total amount

## Cart Fields
| Field | Type | Description |
|---|---|---|
| id | Integer | Primary Key |
| user | ForeignKey(User) | Cart Owner |
| product | ForeignKey(Product) | Product |
| quantity | IntegerField | Product Quantity |
| subtotal | DecimalField | Product Total |

## User Flow
1. User opens products page.
2. Clicks "Add to Cart".
3. Product added to cart.
4. User can view cart.
5. User can update quantity/remove item.

## UI Requirements
- Cart icon in navbar
- Quantity badge
- Cart table layout
- Total price section
- Responsive cart page

---

# 4. Website Navigation Flow

## Main Flow

### Step 1: Landing Page
- Welcome page
- Login/Register buttons

### Step 2: Authentication
- Login/Register form
- Role selection

### Step 3: Category Page
- Display all categories
- Search categories
- Admin CRUD access

### Step 4: Sub Category Page
- Display related sub categories
- Search sub categories
- Admin CRUD access

### Step 5: Products Page
- Display products
- Search products
- Add to cart functionality
- Admin CRUD access

### Step 6: Cart Page
- View added products
- Update/remove products
- View total amount

---

# 5. Non-Functional Requirements

## Performance
- Fast page loading
- Optimized image loading
- Pagination for products

## Security
- CSRF Protection
- Password Hashing
- Role-based authorization
- Input validation
- Secure sessions

## Scalability
- Modular app structure
- Reusable templates
- Maintainable codebase

## Responsiveness
- Mobile-first design
- Tablet responsive
- Desktop optimized

---

# 6. UI/UX Requirements

## Design Inspiration
- Amazon-like ecommerce UI
- Clean product cards
- Sticky navbar
- Large product images
- Professional typography

## Color Palette
| Element | Suggested Color |
|---|---|
| Primary | #131921 |
| Secondary | #232F3E |
| Accent | #FF9900 |
| Background | #F3F3F3 |
| Text | #111111 |

## UI Components
- Navbar
- Sidebar Filters
- Search Bars
- Product Cards
- Category Cards
- Buttons
- Modal confirmations
- Responsive Footer

## User Experience Goals
- Easy navigation
- Minimal clicks
- Fast product browsing
- Clear visual hierarchy
- Smooth interactions

---

# 7. Django Project Structure

```plaintext
project_root/
│
├── ecommerce_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── categories/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── products/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── templates/
│
├── cart/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── media/
├── static/
├── templates/
└── manage.py
```

---

# 8. Database Design

# User Table
| Field | Type |
|---|---|
| id | Integer |
| username | String |
| email | String |
| password | String |
| role | ChoiceField(Admin/User) |

# Category Table
| Field | Type |
|---|---|
| id | Integer |
| name | String |
| image | Image |
| description | Text |

# Sub Category Table
| Field | Type |
|---|---|
| id | Integer |
| category_id | Foreign Key |
| name | String |
| image | Image |
| description | Text |

# Product Table
| Field | Type |
|---|---|
| id | Integer |
| category_id | Foreign Key |
| name | String |
| image | Image |
| price | Decimal |
| quantity | Integer |
| description | Text |

# Cart Table
| Field | Type |
|---|---|
| id | Integer |
| user_id | Foreign Key |
| product_id | Foreign Key |
| quantity | Integer |

---

# 9. Function-Based Views Requirement

All views must use Function-Based Views (FBV).

## Example Modules
- login_view()
- register_view()
- category_list()
- add_category()
- edit_category()
- delete_category()
- subcategory_list()
- product_list()
- add_to_cart()
- cart_view()

## Access Control
Use decorators:
- @login_required
- Custom admin_required decorator

---

# 10. Search & Filter Requirements

## Search Features
Every page should include search functionality.

### Category Search
- Search categories by name.

### Sub Category Search
- Search sub categories by name.

### Product Search
- Search products by name.

## Filter Behavior
- Real-time filtering optional.
- Query parameter-based filtering.
- Case-insensitive search.

---

# 11. Validation Requirements

## Category Validation
- Name required
- Image required

## Sub Category Validation
- Name required
- Parent category required

## Product Validation
- Name required
- Price > 0
- Quantity >= 0
- Image required

## Cart Validation
- Quantity must not exceed stock

---

# 12. Recommended Django Packages

## Backend Packages
```bash
pip install django
pip install pillow
```

## Optional Packages
```bash
pip install django-crispy-forms
pip install crispy-bootstrap5
```

---

# 13. Static & Media Handling

## Static Files
Used for:
- CSS
- JavaScript
- Icons
- Fonts

## Media Files
Used for:
- Category Images
- Sub Category Images
- Product Images

---

# 14. Responsive Design Requirements

## Mobile Features
- Hamburger menu
- Responsive cards
- Optimized image loading

## Desktop Features
- Sidebar filters
- Multi-column layouts
- Sticky navbar

---

# 15. Future Enhancements

## Optional Features
- Wishlist
- Product Reviews
- Ratings
- Checkout System
- Payment Gateway Integration
- Order Management
- Product Sorting
- Admin Dashboard Analytics
- JWT Authentication API
- REST API using Django REST Framework

---

# 16. Development Phases

## Phase 1
- Project setup
- Authentication system
- Role management

## Phase 2
- Category CRUD
- Sub Category CRUD

## Phase 3
- Product CRUD
- Product listing UI

## Phase 4
- Cart functionality
- Search and filters

## Phase 5
- UI enhancements
- Responsive optimization
- Testing

---

# 17. Acceptance Criteria

## Admin Acceptance
- Admin can manage all categories.
- Admin can manage sub categories.
- Admin can manage products.
- CRUD operations work properly.

## User Acceptance
- User can browse products.
- User can search products.
- User can add items to cart.
- User can manage cart.

## System Acceptance
- Website responsive on all devices.
- Authentication works securely.
- Search functionality works.
- Function-based views used throughout project.

---

# 18. Conclusion

This Django Ecommerce Store project aims to provide a scalable, clean, and user-friendly ecommerce platform using Python and Django with Function-Based Views. The project follows role-based access control where admins manage the store and users browse and purchase products through a modern Amazon-inspired interface.

