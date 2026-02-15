"""
Simple database initialization script
Run this to create the database and add sample data
"""
from app import app, db
from models import User, Book

print("🗄️  Initializing BookHaven Database...")
print("=" * 50)

with app.app_context():
    # Create all tables
    print("Creating database tables...")
    db.create_all()
    print("✅ Tables created!")
    
    # Check if admin already exists
    existing_admin = User.query.filter_by(username='admin').first()
    if existing_admin:
        print("⚠️  Admin user already exists, skipping seed data...")
    else:
        print("\nAdding sample data...")
        
        # Create admin user
        admin = User(
            username='admin',
            email='admin@bookstore.com',
            full_name='Admin User',
            role='admin'
        )
        admin.set_password('admin123')
        db.session.add(admin)
        print("✅ Admin user created")
        
        # Create regular user
        user = User(
            username='john',
            email='john@example.com',
            full_name='John Doe',
            phone='9841234567'
        )
        user.set_password('password123')
        db.session.add(user)
        print("✅ Regular user created")
        
        # Sample books
        books = [
            {
                'title': 'The Great Gatsby',
                'author': 'F. Scott Fitzgerald',
                'isbn': '9780743273565',
                'price': 650.00,
                'stock_quantity': 25,
                'category': 'Fiction',
                'description': 'A classic American novel set in the Jazz Age.',
                'publisher': 'Scribner',
                'publication_year': 1925,
                'pages': 180,
                'rating': 4.5
            },
            {
                'title': 'To Kill a Mockingbird',
                'author': 'Harper Lee',
                'isbn': '9780061120084',
                'price': 700.00,
                'stock_quantity': 30,
                'category': 'Fiction',
                'description': 'A story of racial injustice and childhood innocence.',
                'publisher': 'Harper Perennial',
                'publication_year': 1960,
                'pages': 324,
                'rating': 4.8
            },
            {
                'title': '1984',
                'author': 'George Orwell',
                'isbn': '9780451524935',
                'price': 550.00,
                'stock_quantity': 20,
                'category': 'Fiction',
                'description': 'A dystopian social science fiction novel.',
                'publisher': 'Signet Classic',
                'publication_year': 1949,
                'pages': 328,
                'rating': 4.7
            },
            {
                'title': 'Python Crash Course',
                'author': 'Eric Matthes',
                'isbn': '9781593279288',
                'price': 1200.00,
                'stock_quantity': 15,
                'category': 'Technology',
                'description': 'A hands-on introduction to programming.',
                'publisher': 'No Starch Press',
                'publication_year': 2019,
                'pages': 544,
                'rating': 4.6
            },
            {
                'title': 'Clean Code',
                'author': 'Robert C. Martin',
                'isbn': '9780132350884',
                'price': 1500.00,
                'stock_quantity': 12,
                'category': 'Technology',
                'description': 'A handbook of agile software craftsmanship.',
                'publisher': 'Prentice Hall',
                'publication_year': 2008,
                'pages': 464,
                'rating': 4.7
            },
            {
                'title': 'Sapiens',
                'author': 'Yuval Noah Harari',
                'isbn': '9780062316097',
                'price': 900.00,
                'stock_quantity': 18,
                'category': 'History',
                'description': 'A brief history of humankind.',
                'publisher': 'Harper',
                'publication_year': 2015,
                'pages': 443,
                'rating': 4.5
            },
            {
                'title': 'Atomic Habits',
                'author': 'James Clear',
                'isbn': '9780735211292',
                'price': 800.00,
                'stock_quantity': 22,
                'category': 'Self-Help',
                'description': 'An easy way to build good habits.',
                'publisher': 'Avery',
                'publication_year': 2018,
                'pages': 320,
                'rating': 4.8
            },
            {
                'title': 'The Alchemist',
                'author': 'Paulo Coelho',
                'isbn': '9780062315007',
                'price': 600.00,
                'stock_quantity': 28,
                'category': 'Fiction',
                'description': 'A magical story about following your dreams.',
                'publisher': 'HarperOne',
                'publication_year': 1988,
                'pages': 208,
                'rating': 4.6
            }
        ]
        
        for book_data in books:
            book = Book(**book_data)
            db.session.add(book)
        
        db.session.commit()
        print("✅ Sample books added")
    
    print("\n" + "=" * 50)
    print("✅ Database initialization complete!")
    print("\nYou can now run: python app.py")
    print("\nDefault login credentials:")
    print("  Admin: admin / admin123")
    print("  User:  john / password123")
    print("=" * 50)
