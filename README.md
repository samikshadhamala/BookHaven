# 📚 BookHaven - Online Bookstore

A modern, full-stack online bookstore web application built with Flask, SQLAlchemy, and Bootstrap 5.

![BookHaven](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)

## 🎯 Project Overview

**Course**: Web Technology (BIT233)  
**Institution**: Texas College of Management & IT  
**Instructor**: Mr. Ashish Gautam (PhD Scholars)  
**Academic Year**: Second Year / Third Semester

This project is a comprehensive Online Bookstore that demonstrates full-stack web development skills including frontend design, backend programming, database management, and deployment.

## ✨ Features

### User Features
- 📖 Browse books by category, search, and filter
- 🛒 Shopping cart functionality
- 👤 User registration and authentication
- 📦 Order placement and tracking
- 👨‍💼 User dashboard with order history
- 🔐 Secure password hashing
- 📱 Fully responsive design

### Admin Features
- 📚 Book management (CRUD operations)
- 📊 Admin dashboard with statistics
- 📋 Order management and status updates
- 👥 User management
- 📈 Inventory tracking

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask 2.3.0
- **Database**: SQLAlchemy (SQLite)
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Password Security**: Werkzeug

### Frontend
- **Framework**: Bootstrap 5.3.0
- **Icons**: Font Awesome 6.x
- **Fonts**: Google Fonts (Playfair Display, Poppins)
- **JavaScript**: jQuery 3.6.0
- **Styling**: Custom CSS with modern design

## 📁 Project Structure

```
bookstore/
├── app.py                  # Main Flask application
├── models.py              # Database models
├── forms.py               # WTForms validation
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
├── README.md             # Project documentation
├── static/
│   ├── css/
│   │   └── style.css     # Custom styles
│   ├── js/
│   │   └── script.js     # JavaScript functionality
│   └── images/
│       └── book_covers/  # Book cover images
├── templates/
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── books.html        # Book catalog
│   ├── book_detail.html  # Book details
│   ├── cart.html         # Shopping cart
│   ├── checkout.html     # Checkout page
│   ├── dashboard.html    # User dashboard
│   ├── profile.html      # User profile
│   ├── login.html        # Login page
│   ├── register.html     # Registration
│   ├── order_confirmation.html  # Order confirmation
│   ├── admin.html        # Admin dashboard
│   ├── admin_books.html  # Manage books
│   ├── admin_orders.html # Manage orders
│   ├── add_book.html     # Add book form
│   ├── edit_book.html    # Edit book form
│   ├── 404.html          # Error 404
│   └── 500.html          # Error 500
└── instance/
    └── bookstore.db      # SQLite database
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd bookstore
```

### Step 2: Create Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize Database
```bash
# Initialize database tables
flask --app app init-db

# Seed database with sample data (optional)
flask --app app seed-db
```

### Step 5: Run the Application
```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`

## 👥 Default Users

After seeding the database, you can log in with:

### Admin Account
- **Username**: admin
- **Password**: admin123
- **Role**: Administrator

### Regular User
- **Username**: john
- **Password**: password123
- **Role**: Customer

## 📋 Database Schema

### Users Table
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- role (user/admin)
- full_name
- phone
- address
- created_at

### Books Table
- id (Primary Key)
- title
- author
- isbn (Unique)
- price
- stock_quantity
- category
- description
- publisher
- publication_year
- pages
- language
- cover_image
- rating
- created_at

### Orders Table
- id (Primary Key)
- user_id (Foreign Key → Users)
- order_date
- total_amount
- status
- shipping_address
- shipping_city
- shipping_postal_code
- shipping_phone
- payment_method

### OrderItems Table
- id (Primary Key)
- order_id (Foreign Key → Orders)
- book_id (Foreign Key → Books)
- quantity
- price

## 🎨 Design Features

- **Modern UI/UX**: Clean, professional design with smooth animations
- **Color Scheme**: Rich brown (#8B4513) and gold (#DAA520) palette
- **Typography**: Playfair Display for headings, Poppins for body text
- **Responsive**: Mobile-first design that works on all devices
- **Animations**: Smooth transitions and hover effects
- **Accessibility**: Semantic HTML and ARIA labels

## 🔒 Security Features

- Password hashing using Werkzeug
- CSRF protection with Flask-WTF
- Session management with Flask-Login
- SQL injection prevention with SQLAlchemy ORM
- Secure file upload validation

## 📝 API Routes

### Public Routes
- `GET /` - Homepage
- `GET /books` - Browse books
- `GET /book/<id>` - Book details
- `GET /register` - Registration form
- `GET /login` - Login form
- `POST /login` - Login submission

### Protected Routes (Login Required)
- `GET /cart` - Shopping cart
- `POST /add_to_cart/<id>` - Add to cart
- `GET /checkout` - Checkout
- `POST /checkout` - Place order
- `GET /dashboard` - User dashboard
- `GET /profile` - User profile
- `GET /logout` - Logout

### Admin Routes (Admin Only)
- `GET /admin` - Admin dashboard
- `GET /admin/books` - Manage books
- `GET /admin/orders` - Manage orders
- `GET /admin/book/add` - Add book
- `POST /admin/book/add` - Save new book
- `GET /admin/book/edit/<id>` - Edit book
- `POST /admin/book/edit/<id>` - Update book
- `POST /admin/book/delete/<id>` - Delete book
- `POST /admin/order/update/<id>` - Update order status

## 🧪 Testing

To test the application:

1. **Registration**: Create a new user account
2. **Login**: Log in with credentials
3. **Browse**: View books and categories
4. **Search**: Search for books by title/author
5. **Cart**: Add books to cart, update quantities
6. **Checkout**: Place an order
7. **Dashboard**: View order history
8. **Admin**: Log in as admin to manage books/orders

## 📦 Deployment

### Local Deployment
Already running locally after setup.

### PythonAnywhere
1. Create account on PythonAnywhere
2. Upload files via dashboard
3. Configure web app with Flask
4. Set environment variables
5. Reload web app

### Heroku
```bash
# Install Heroku CLI
heroku login
heroku create bookstore-app
git push heroku main
heroku run flask --app app init-db
```

## 🤝 Contributing

This is an academic project. For suggestions or improvements:
1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is created for educational purposes as part of Web Technology (BIT233) course assignment.

## 👨‍💻 Author

**[Your Name]**  
Student ID: [Your LCID]  
Texas College of Management & IT  
Bachelor of Information Technology (BIT)

## 📧 Contact

For questions or feedback:
- Email: [your-email@example.com]
- GitHub: [your-github-username]

## 🙏 Acknowledgments

- **Instructor**: Mr. Ashish Gautam for guidance and support
- **Texas College of Management & IT** for providing learning opportunities
- **Flask Documentation** for excellent framework documentation
- **Bootstrap Team** for the amazing CSS framework
- **Font Awesome** for beautiful icons

---

**Note**: This project demonstrates full-stack web development skills including Python Flask, SQLAlchemy ORM, HTML5, CSS3, JavaScript, Bootstrap 5, responsive design, database management, authentication, and deployment.

Made with ❤️ for Web Technology (BIT233) Assignment
