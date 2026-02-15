# 📘 BookHaven - Complete Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Installation Guide](#installation-guide)
3. [User Manual](#user-manual)
4. [Admin Manual](#admin-manual)
5. [Technical Documentation](#technical-documentation)
6. [Troubleshooting](#troubleshooting)

---

## Project Overview

### Assignment Details
- **Course**: Web Technology (BIT233)
- **Project**: Build the Web - A Full-Stack Website Development Project
- **Type**: Online Bookstore
- **Technology Stack**: Flask, SQLAlchemy, Bootstrap 5, jQuery

### Features Implemented
✅ User registration and authentication  
✅ Book browsing with search and filters  
✅ Shopping cart functionality  
✅ Order placement and tracking  
✅ Admin panel for book/order management  
✅ Responsive design  
✅ Form validation (client & server-side)  
✅ Password hashing  
✅ Session management  
✅ CRUD operations  
✅ Database relationships  

---

## Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Web browser (Chrome, Firefox, Safari, Edge)

### Step-by-Step Installation

#### 1. Download the Project
```bash
git clone <repository-url>
cd bookstore
```

#### 2. Create Virtual Environment
**Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Initialize Database
```bash
flask --app app init-db
flask --app app seed-db
```

#### 5. Run Application
```bash
python app.py
```

#### 6. Access Application
Open browser and navigate to: `http://127.0.0.1:5000/`

---

## User Manual

### For Customers

#### 1. Registration
1. Click "Register" in navigation
2. Fill in the form:
   - Username (minimum 3 characters)
   - Email (valid email format)
   - Full Name
   - Phone Number (optional)
   - Password (minimum 8 characters)
   - Confirm Password
3. Click "Register" button
4. You'll be redirected to login page

#### 2. Login
1. Click "Login" in navigation
2. Enter username and password
3. Click "Login" button

#### 3. Browse Books
1. Click "Browse Books" in navigation
2. Use filters:
   - Search by title/author/ISBN
   - Filter by category
   - Sort by price/rating
3. Click on book to view details

#### 4. Add to Cart
1. View book details
2. Select quantity
3. Click "Add to Cart"
4. View cart by clicking cart icon

#### 5. Checkout
1. Go to cart
2. Review items
3. Click "Proceed to Checkout"
4. Fill shipping information
5. Select payment method
6. Click "Place Order"

#### 6. View Orders
1. Go to Dashboard
2. See order history
3. Click order to view details

---

## Admin Manual

### Admin Access
- Username: `admin`
- Password: `admin123`

### 1. Admin Dashboard
- View total books, users, orders
- See recent orders
- Quick access to management features

### 2. Manage Books

#### Add New Book
1. Go to Admin Dashboard
2. Click "Add New Book"
3. Fill in book details:
   - Title, Author, ISBN
   - Price, Stock Quantity
   - Category, Description
   - Publisher, Year, Pages
   - Language, Rating
   - Upload cover image
4. Click "Save Book"

#### Edit Book
1. Go to "Manage Books"
2. Click edit icon (pencil)
3. Update details
4. Click "Save Book"

#### Delete Book
1. Go to "Manage Books"
2. Click delete icon (trash)
3. Confirm deletion

### 3. Manage Orders
1. Go to "Manage Orders"
2. View all orders
3. Update status:
   - Pending
   - Processing
   - Shipped
   - Delivered
   - Cancelled

---

## Technical Documentation

### Database Models

#### User Model
```python
- id: Integer (Primary Key)
- username: String(80) Unique
- email: String(120) Unique
- password_hash: String(200)
- role: String(20) [user/admin]
- full_name: String(100)
- phone: String(20)
- address: Text
- created_at: DateTime
```

#### Book Model
```python
- id: Integer (Primary Key)
- title: String(200)
- author: String(100)
- isbn: String(13) Unique
- price: Float
- stock_quantity: Integer
- category: String(50)
- description: Text
- publisher: String(100)
- publication_year: Integer
- pages: Integer
- language: String(20)
- cover_image: String(200)
- rating: Float
- created_at: DateTime
```

#### Order Model
```python
- id: Integer (Primary Key)
- user_id: Integer (Foreign Key)
- order_date: DateTime
- total_amount: Float
- status: String(20)
- shipping_address: Text
- shipping_city: String(100)
- shipping_postal_code: String(20)
- shipping_phone: String(20)
- payment_method: String(50)
```

#### OrderItem Model
```python
- id: Integer (Primary Key)
- order_id: Integer (Foreign Key)
- book_id: Integer (Foreign Key)
- quantity: Integer
- price: Float
```

### Relationships
- User → Orders (One-to-Many)
- Order → OrderItems (One-to-Many)
- Book → OrderItems (One-to-Many)
- Orders ↔ Books (Many-to-Many through OrderItems)

### Form Validation

#### Server-Side (Flask-WTF)
- DataRequired
- Email
- Length
- NumberRange
- EqualTo
- Custom validators

#### Client-Side (JavaScript)
- Email format
- Password length
- Password match
- Stock availability
- Number ranges

### Security Features
1. **Password Hashing**: Werkzeug PBKDF2
2. **CSRF Protection**: Flask-WTF tokens
3. **SQL Injection Prevention**: SQLAlchemy ORM
4. **Session Security**: Flask-Login
5. **File Upload Validation**: Extension checking

---

## Troubleshooting

### Common Issues

#### 1. Database Not Found
**Error**: `sqlite3.OperationalError: no such table`

**Solution**:
```bash
flask --app app init-db
flask --app app seed-db
```

#### 2. Module Not Found
**Error**: `ModuleNotFoundError: No module named 'flask'`

**Solution**:
```bash
pip install -r requirements.txt
```

#### 3. Port Already in Use
**Error**: `Address already in use`

**Solution**:
```python
# In app.py, change:
app.run(debug=True, port=5001)
```

#### 4. Image Upload Not Working
**Error**: Images not displaying

**Solution**:
- Check `static/images/book_covers/` exists
- Verify file permissions
- Check file extensions (jpg, png, gif, webp)
- Maximum file size: 5MB

#### 5. Login Not Working
**Issue**: Cannot log in

**Check**:
- Username/password correct
- Database seeded
- Session secret key set

#### 6. Admin Access Denied
**Issue**: Cannot access admin panel

**Check**:
- Logged in as admin user
- User role is 'admin' in database

### Getting Help

If you encounter issues:
1. Check error messages in terminal
2. Review browser console (F12)
3. Verify all dependencies installed
4. Check database exists and is seeded
5. Restart application

---

## Performance Optimization

### For Production

1. **Debug Mode**
```python
app.run(debug=False)
```

2. **Database**
- Use PostgreSQL instead of SQLite
- Add database indexes
- Implement caching

3. **Static Files**
- Use CDN for libraries
- Minify CSS/JS
- Optimize images

4. **Security**
- Change SECRET_KEY
- Use environment variables
- Enable HTTPS
- Add rate limiting

---

## Future Enhancements

Potential improvements:
- Email notifications
- Payment gateway integration
- Book reviews and ratings
- Wishlist functionality
- Advanced search (filters)
- Recommendation system
- Export orders to PDF
- Multi-language support
- Social media login
- RESTful API

---

## Appendix

### Technologies Used
- **Backend**: Flask 2.3.0
- **Database**: SQLAlchemy + SQLite
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Frontend**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.x
- **JavaScript**: jQuery 3.6.0
- **Fonts**: Google Fonts

### Resources
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)

---

**Project Created**: February 2025  
**Course**: Web Technology (BIT233)  
**Institution**: Texas College of Management & IT
