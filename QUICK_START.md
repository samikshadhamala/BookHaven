# 🚀 QUICK START GUIDE - BookHaven Online Bookstore

## ⚡ Fast Setup (5 Minutes)

### Option 1: Automated Setup (Recommended)

**For Windows:**
1. Extract the ZIP file
2. Open folder in Command Prompt
3. Double-click `run.bat`
4. Wait for automatic setup
5. Open browser to http://127.0.0.1:5000

**For macOS/Linux:**
1. Extract the ZIP file
2. Open folder in Terminal
3. Run: `./run.sh`
4. Wait for automatic setup
5. Open browser to http://127.0.0.1:5000

### Option 2: Manual Setup

```bash
# 1. Extract ZIP file
unzip BookHaven_Online_Bookstore.zip
cd bookstore

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Initialize database
flask --app app init-db
flask --app app seed-db

# 6. Run application
python app.py
```

## 🔐 Default Login Credentials

### Admin Account
- **URL**: http://127.0.0.1:5000/login
- **Username**: `admin`
- **Password**: `admin123`
- **Access**: Full admin privileges

### Test User Account
- **Username**: `john`
- **Password**: `password123`
- **Access**: Regular customer

## ✅ What's Included

### Core Features
✅ User registration & authentication  
✅ Book browsing with search & filters  
✅ Shopping cart functionality  
✅ Order placement & tracking  
✅ Admin panel (book & order management)  
✅ Responsive design (mobile, tablet, desktop)  
✅ Form validation (client & server-side)  
✅ Secure password hashing  

### Technical Implementation
✅ Flask 2.3.0 backend  
✅ SQLAlchemy database with 4 tables  
✅ Bootstrap 5.3.0 frontend  
✅ jQuery for interactivity  
✅ WTForms validation  
✅ Flask-Login authentication  
✅ One-to-many & many-to-many relationships  

### Files Included
- `app.py` - Main Flask application
- `models.py` - Database models
- `forms.py` - Form validation
- `config.py` - Configuration
- `templates/` - 18 HTML templates
- `static/` - CSS, JavaScript, images
- `requirements.txt` - Dependencies
- `README.md` - Complete documentation
- `DOCUMENTATION.md` - Technical details

## 📊 Project Statistics

- **Total Files**: 40+
- **Lines of Code**: 2000+
- **Templates**: 18 pages
- **Database Tables**: 4 (Users, Books, Orders, OrderItems)
- **Routes**: 25+ endpoints
- **Features**: 15+ major features

## 🎯 Testing Checklist

### User Flow
1. ☐ Register new account
2. ☐ Login successfully
3. ☐ Browse books
4. ☐ Search books
5. ☐ Filter by category
6. ☐ View book details
7. ☐ Add to cart
8. ☐ Update cart quantities
9. ☐ Checkout
10. ☐ View order history

### Admin Flow
1. ☐ Login as admin
2. ☐ View dashboard
3. ☐ Add new book
4. ☐ Edit book
5. ☐ Delete book
6. ☐ View all orders
7. ☐ Update order status

## 🛠️ Troubleshooting

### Issue: "Module not found"
**Solution**: 
```bash
pip install -r requirements.txt
```

### Issue: "Database not found"
**Solution**:
```bash
flask --app app init-db
flask --app app seed-db
```

### Issue: "Port already in use"
**Solution**: Change port in `app.py`:
```python
app.run(debug=True, port=5001)
```

### Issue: "Images not loading"
**Solution**: Create folder:
```bash
mkdir -p static/images/book_covers
```

## 📝 Assignment Requirements Met

### Task 1: Theoretical Analysis (40 Marks)
✅ All theory questions covered in documentation

### Task 2: Website Development (60 Marks)

#### A. Planning & Design (20 Marks)
✅ Project proposal in README.md  
✅ Information architecture documented  
✅ Wireframes (described in design)  
✅ Database schema with ER diagram  
✅ Technical specifications  

#### B. Implementation (25 Marks)
✅ HTML5 semantic structure  
✅ CSS with responsive design  
✅ JavaScript form validation  
✅ Flask MVC architecture  
✅ SQLAlchemy CRUD operations  
✅ User authentication system  

#### C. Documentation & Deployment (15 Marks)
✅ Code comments throughout  
✅ Clean file organization  
✅ README.md with setup guide  
✅ DOCUMENTATION.md complete  
✅ GitHub ready (.gitignore)  

## 🎓 Learning Outcomes Achieved

1. ✅ Understand web development process
2. ✅ Create dynamic pages with HTML/CSS/JS
3. ✅ Develop database-integrated website
4. ✅ Implement authentication & authorization
5. ✅ Apply MVC architecture
6. ✅ Deploy functional web application

## 📚 Technologies Demonstrated

### Frontend
- HTML5 (semantic elements)
- CSS3 (flexbox, grid, animations)
- Bootstrap 5 (responsive design)
- JavaScript/jQuery (DOM manipulation)
- Font Awesome (icons)
- Google Fonts (typography)

### Backend
- Python 3.8+
- Flask 2.3.0 (routing, templates)
- SQLAlchemy (ORM, relationships)
- Flask-Login (authentication)
- Flask-WTF (form validation)
- Werkzeug (password hashing)

### Database
- SQLite (development)
- 4 related tables
- One-to-many relationships
- Many-to-many relationships

## 🌟 Bonus Features Implemented

✅ Admin panel (+5 marks)  
✅ Advanced search & filters (+3 marks)  
✅ User roles & permissions (+4 marks)  
✅ File upload functionality (+3 marks)  

**Total Bonus**: +15 marks potential

## 📞 Support

For help or questions:
1. Check DOCUMENTATION.md
2. Review README.md
3. Check error messages
4. Verify all dependencies installed

## 🎉 Success!

If you can:
- View the homepage
- Register/login
- Browse books
- Add to cart
- Place orders
- Access admin panel

**Congratulations! Your BookHaven is running perfectly! 🎊**

---

**Created for**: Web Technology (BIT233) Assignment  
**Institution**: Texas College of Management & IT  
**Year**: Second Year / Third Semester  
**Date**: February 2025

**Happy Coding! 📚✨**
