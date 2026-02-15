"""
Database Models for Online Bookstore
Defines all database tables and their relationships using Flask-SQLAlchemy
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

class User(UserMixin, db.Model):
    """
    User model for storing user account information
    Includes both regular users and admin users
    """
    __tablename__ = 'users'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # User credentials and information
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(200), nullable=False)
    
    # User role: 'user' or 'admin'
    role = db.Column(db.String(20), default='user', nullable=False)
    
    # Profile information
    full_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship: One user can have many orders
    orders = db.relationship('Order', backref='customer', lazy='dynamic', cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Hash and set the user's password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify if the provided password matches the hash"""
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        """Check if user has admin privileges"""
        return self.role == 'admin'
    
    def __repr__(self):
        return f'<User {self.username}>'


class Book(db.Model):
    """
    Book model for storing book information in the catalog
    """
    __tablename__ = 'books'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Book information
    title = db.Column(db.String(200), nullable=False, index=True)
    author = db.Column(db.String(100), nullable=False, index=True)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    
    # Pricing and inventory
    price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0, nullable=False)
    
    # Book details
    category = db.Column(db.String(50), nullable=False, index=True)
    description = db.Column(db.Text)
    publisher = db.Column(db.String(100))
    publication_year = db.Column(db.Integer)
    pages = db.Column(db.Integer)
    language = db.Column(db.String(20), default='English')
    
    # Image and rating
    cover_image = db.Column(db.String(200), default='default_cover.jpg')
    rating = db.Column(db.Float, default=0.0)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship: One book can appear in many order items
    order_items = db.relationship('OrderItem', backref='book', lazy='dynamic')
    
    def is_in_stock(self):
        """Check if book is available in stock"""
        return self.stock_quantity > 0
    
    def __repr__(self):
        return f'<Book {self.title}>'


class Order(db.Model):
    """
    Order model for storing customer orders
    """
    __tablename__ = 'orders'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign key to User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Order information
    order_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    
    # Order status: 'Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled'
    status = db.Column(db.String(20), default='Pending', nullable=False)
    
    # Shipping information
    shipping_address = db.Column(db.Text, nullable=False)
    shipping_city = db.Column(db.String(100))
    shipping_postal_code = db.Column(db.String(20))
    shipping_phone = db.Column(db.String(20))
    
    # Payment information
    payment_method = db.Column(db.String(50), default='Cash on Delivery')
    
    # Relationship: One order can have many order items
    order_items = db.relationship('OrderItem', backref='order', lazy='dynamic', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Order {self.id}>'


class OrderItem(db.Model):
    """
    OrderItem model for many-to-many relationship between Orders and Books
    Stores individual items in each order
    """
    __tablename__ = 'order_items'
    
    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign keys
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    
    # Item details
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Float, nullable=False)  # Price at time of order
    
    def subtotal(self):
        """Calculate subtotal for this item"""
        return self.quantity * self.price
    
    def __repr__(self):
        return f'<OrderItem {self.id}>'
