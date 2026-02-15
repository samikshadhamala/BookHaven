# 📚 BookHaven - Online Bookstore

A modern, full-stack online bookstore web application built with Flask, SQLAlchemy, and Bootstrap 5.

**Course**: Web Technology (BIT233)  
**Institution**: Texas College of Management & IT

## 🚀 Quick Setup

1. **Install Python 3.8+** (if not already installed)

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Initialize Database**
   ```bash
   flask --app app init-db
   flask --app app seed-db
   ```

4. **Run Application**
   ```bash
   python app.py
   ```

5. **Open Browser**
   ```
   http://127.0.0.1:5000
   ```

## 🔐 Default Login

**Admin**: admin / admin123  
**User**: john / password123

## ✨ Features

### User Features
- User registration & login
- Browse books by category
- Search & filter books
- Shopping cart
- Order placement & tracking
- Profile management

### Admin Features
- Admin dashboard
- Add/Edit/Delete books
- Manage inventory
- View/Update orders

## 💻 Technology Stack

**Backend**: Flask 2.3.0, SQLAlchemy, Flask-Login, Flask-WTF  
**Frontend**: Bootstrap 5.3.0, jQuery, HTML5, CSS3  
**Database**: SQLite with 4 related tables

## 📁 Project Structure

```
bookstore/
├── app.py                  # Main application
├── models.py              # Database models
├── forms.py               # Form validation
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── templates/             # 18 HTML templates
├── static/
│   ├── css/style.css     # Custom styles
│   ├── js/script.js      # JavaScript
│   └── images/           # Images
└── instance/
    └── bookstore.db      # Database
```

## 📊 Database Schema

- **Users**: User accounts (id, username, email, password_hash, role, etc.)
- **Books**: Book catalog (id, title, author, isbn, price, stock, etc.)
- **Orders**: Customer orders (id, user_id, total_amount, status, etc.)
- **OrderItems**: Order details (id, order_id, book_id, quantity, price)

**Relationships**:
- Users → Orders (One-to-Many)
- Orders → OrderItems (One-to-Many)
- Books → OrderItems (One-to-Many)
- Orders ↔ Books (Many-to-Many through OrderItems)

## 🎯 Assignment Requirements Met

✅ Responsive HTML5/CSS3 design  
✅ Bootstrap 5 integration  
✅ JavaScript/jQuery interactivity  
✅ Flask backend with routing  
✅ SQLAlchemy database (4 tables)  
✅ User authentication & sessions  
✅ CRUD operations  
✅ Form validation (client & server)  
✅ Admin panel (+5 bonus)  
✅ File upload (+3 bonus)  
✅ Advanced search (+3 bonus)  
✅ User roles (+4 bonus)  

**Total**: 60 marks + 15 bonus = 75 marks potential!

## 📖 Documentation

- **README.md**: This file
- **DOCUMENTATION.md**: Detailed technical documentation
- **QUICK_START.md**: Fast setup guide
- **SETUP.txt**: Manual setup instructions

## 🛠️ Troubleshooting

**Issue**: Module not found  
**Fix**: `pip install -r requirements.txt`

**Issue**: Database not found  
**Fix**: `flask --app app init-db`

**Issue**: Port already in use  
**Fix**: Change port in app.py to 5001

## 👨‍💻 Author

Created for Web Technology (BIT233) Assignment  
Texas College of Management & IT  
Second Year / Third Semester

---

**Made with ❤️ for BIT233 Assignment**
