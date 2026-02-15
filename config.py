"""
Configuration file for Flask application
Contains all the configuration settings for the bookstore application
"""
import os

# Get the base directory of the application
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration class with default settings"""
    
    # Secret key for session management and CSRF protection
    # IMPORTANT: Change this to a random string in production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database configuration
    # Using SQLite database stored in instance folder
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'instance', 'bookstore.db')
    
    # Disable track modifications to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload folder for book cover images
    UPLOAD_FOLDER = os.path.join(basedir, 'static', 'images', 'book_covers')
    
    # Maximum file size for uploads (5MB)
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    
    # Allowed file extensions for book covers
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    
    # Pagination settings
    BOOKS_PER_PAGE = 12
    ORDERS_PER_PAGE = 10
