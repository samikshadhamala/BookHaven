"""
Main Flask Application for Online Bookstore
Created for Web Technology (BIT233) Assignment
"""
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
import os
from datetime import datetime

# Import configuration and models
from config import Config
from models import db, User, Book, Order, OrderItem
from forms import RegistrationForm, LoginForm, BookForm, ProfileForm, CheckoutForm, SearchForm

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login"""
    return User.query.get(int(user_id))

# Helper function to check allowed file extensions
def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# ==================== ROUTES ====================

# HOME PAGE
@app.route('/')
@app.route('/index')
def index():
    """Homepage with featured books and categories"""
    # Get featured books (highest rated)
    featured_books = Book.query.filter(Book.stock_quantity > 0).order_by(Book.rating.desc()).limit(8).all()
    
    # Get latest books
    latest_books = Book.query.filter(Book.stock_quantity > 0).order_by(Book.created_at.desc()).limit(8).all()
    
    # Get all categories
    categories = db.session.query(Book.category).distinct().all()
    
    return render_template('index.html', 
                         featured_books=featured_books,
                         latest_books=latest_books,
                         categories=categories)

# USER REGISTRATION
@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page"""
    # Redirect if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data,
            full_name=form.full_name.data,
            phone=form.phone.data
        )
        user.set_password(form.password.data)
        
        # Save to database
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

# USER LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login page"""
    # Redirect if already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        # Find user by username
        user = User.query.filter_by(username=form.username.data).first()
        
        # Check if user exists and password is correct
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            
            # Redirect to next page or home
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    
    return render_template('login.html', form=form)

# USER LOGOUT
@app.route('/logout')
@login_required
def logout():
    """Log out current user"""
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('index'))

# BOOKS CATALOG
@app.route('/books')
def books():
    """Display all books with filtering and search"""
    # Get search parameters
    search_query = request.args.get('query', '')
    category_filter = request.args.get('category', '')
    sort_by = request.args.get('sort', 'title')
    
    # Start with base query
    query = Book.query.filter(Book.stock_quantity > 0)
    
    # Apply search filter
    if search_query:
        query = query.filter(
            db.or_(
                Book.title.ilike(f'%{search_query}%'),
                Book.author.ilike(f'%{search_query}%'),
                Book.isbn.ilike(f'%{search_query}%')
            )
        )
    
    # Apply category filter
    if category_filter:
        query = query.filter(Book.category == category_filter)
    
    # Apply sorting
    if sort_by == 'price_asc':
        query = query.order_by(Book.price.asc())
    elif sort_by == 'price_desc':
        query = query.order_by(Book.price.desc())
    elif sort_by == 'rating':
        query = query.order_by(Book.rating.desc())
    else:
        query = query.order_by(Book.title.asc())
    
    # Paginate results
    page = request.args.get('page', 1, type=int)
    books_pagination = query.paginate(page=page, per_page=app.config['BOOKS_PER_PAGE'], error_out=False)
    
    # Get all categories for filter
    categories = db.session.query(Book.category).distinct().all()
    
    return render_template('books.html', 
                         books=books_pagination.items,
                         pagination=books_pagination,
                         categories=categories,
                         search_query=search_query,
                         category_filter=category_filter,
                         sort_by=sort_by)

# BOOK DETAILS
@app.route('/book/<int:book_id>')
def book_detail(book_id):
    """Display single book details"""
    book = Book.query.get_or_404(book_id)
    
    # Get related books from same category
    related_books = Book.query.filter(
        Book.category == book.category,
        Book.id != book.id,
        Book.stock_quantity > 0
    ).limit(4).all()
    
    return render_template('book_detail.html', book=book, related_books=related_books)

# SHOPPING CART
@app.route('/cart')
def cart():
    """Display shopping cart"""
    # Get cart from session
    cart = session.get('cart', {})
    cart_items = []
    total = 0
    
    # Get book details for each item in cart
    for book_id, quantity in cart.items():
        book = Book.query.get(int(book_id))
        if book:
            subtotal = book.price * quantity
            cart_items.append({
                'book': book,
                'quantity': quantity,
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('cart.html', cart_items=cart_items, total=total)

# ADD TO CART
@app.route('/add_to_cart/<int:book_id>', methods=['POST'])
def add_to_cart(book_id):
    """Add book to shopping cart"""
    book = Book.query.get_or_404(book_id)
    quantity = int(request.form.get('quantity', 1))
    
    # Check stock availability
    if quantity > book.stock_quantity:
        flash(f'Only {book.stock_quantity} copies available in stock.', 'warning')
        return redirect(url_for('book_detail', book_id=book_id))
    
    # Get or create cart in session
    cart = session.get('cart', {})
    
    # Add or update quantity
    if str(book_id) in cart:
        cart[str(book_id)] += quantity
    else:
        cart[str(book_id)] = quantity
    
    # Save cart to session
    session['cart'] = cart
    session.modified = True
    
    flash(f'{book.title} added to cart!', 'success')
    return redirect(url_for('books'))

# UPDATE CART
@app.route('/update_cart/<int:book_id>', methods=['POST'])
def update_cart(book_id):
    """Update quantity in cart"""
    quantity = int(request.form.get('quantity', 1))
    
    cart = session.get('cart', {})
    
    if quantity > 0:
        cart[str(book_id)] = quantity
    else:
        cart.pop(str(book_id), None)
    
    session['cart'] = cart
    session.modified = True
    
    flash('Cart updated successfully!', 'success')
    return redirect(url_for('cart'))

# REMOVE FROM CART
@app.route('/remove_from_cart/<int:book_id>')
def remove_from_cart(book_id):
    """Remove item from cart"""
    cart = session.get('cart', {})
    cart.pop(str(book_id), None)
    
    session['cart'] = cart
    session.modified = True
    
    flash('Item removed from cart.', 'info')
    return redirect(url_for('cart'))

# CHECKOUT
@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    """Checkout and place order"""
    # Get cart from session
    cart = session.get('cart', {})
    
    if not cart:
        flash('Your cart is empty!', 'warning')
        return redirect(url_for('books'))
    
    form = CheckoutForm()
    
    # Pre-fill form with user data
    if request.method == 'GET':
        form.shipping_address.data = current_user.address
        form.shipping_phone.data = current_user.phone
    
    if form.validate_on_submit():
        # Calculate total
        total = 0
        order_items_data = []
        
        for book_id, quantity in cart.items():
            book = Book.query.get(int(book_id))
            if book and book.stock_quantity >= quantity:
                subtotal = book.price * quantity
                total += subtotal
                order_items_data.append({
                    'book': book,
                    'quantity': quantity,
                    'price': book.price
                })
            else:
                flash(f'Insufficient stock for {book.title}', 'danger')
                return redirect(url_for('cart'))
        
        # Create order
        order = Order(
            user_id=current_user.id,
            total_amount=total,
            shipping_address=form.shipping_address.data,
            shipping_city=form.shipping_city.data,
            shipping_postal_code=form.shipping_postal_code.data,
            shipping_phone=form.shipping_phone.data,
            payment_method=form.payment_method.data
        )
        db.session.add(order)
        db.session.flush()  # Get order ID
        
        # Create order items and update stock
        for item_data in order_items_data:
            order_item = OrderItem(
                order_id=order.id,
                book_id=item_data['book'].id,
                quantity=item_data['quantity'],
                price=item_data['price']
            )
            db.session.add(order_item)
            
            # Update book stock
            item_data['book'].stock_quantity -= item_data['quantity']
        
        db.session.commit()
        
        # Clear cart
        session['cart'] = {}
        session.modified = True
        
        flash(f'Order #{order.id} placed successfully!', 'success')
        return redirect(url_for('order_confirmation', order_id=order.id))
    
    # Calculate cart total for display
    cart_items = []
    total = 0
    for book_id, quantity in cart.items():
        book = Book.query.get(int(book_id))
        if book:
            subtotal = book.price * quantity
            cart_items.append({
                'book': book,
                'quantity': quantity,
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('checkout.html', form=form, cart_items=cart_items, total=total)

# ORDER CONFIRMATION
@app.route('/order_confirmation/<int:order_id>')
@login_required
def order_confirmation(order_id):
    """Display order confirmation"""
    order = Order.query.get_or_404(order_id)
    
    # Check if order belongs to current user
    if order.user_id != current_user.id and not current_user.is_admin():
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    return render_template('order_confirmation.html', order=order)

# USER DASHBOARD
@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard with profile and order history"""
    # Get user's orders
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_date.desc()).all()
    
    return render_template('dashboard.html', orders=orders)

# UPDATE PROFILE
@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """Update user profile"""
    form = ProfileForm()
    
    if form.validate_on_submit():
        current_user.full_name = form.full_name.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    # Pre-fill form
    elif request.method == 'GET':
        form.full_name.data = current_user.full_name
        form.email.data = current_user.email
        form.phone.data = current_user.phone
        form.address.data = current_user.address
    
    return render_template('profile.html', form=form)

# ==================== ADMIN ROUTES ====================

# ADMIN DASHBOARD
@app.route('/admin')
@login_required
def admin_dashboard():
    """Admin dashboard"""
    if not current_user.is_admin():
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('index'))
    
    # Get statistics
    total_books = Book.query.count()
    total_users = User.query.filter_by(role='user').count()
    total_orders = Order.query.count()
    pending_orders = Order.query.filter_by(status='Pending').count()
    
    # Get recent orders
    recent_orders = Order.query.order_by(Order.order_date.desc()).limit(10).all()
    
    return render_template('admin.html', 
                         total_books=total_books,
                         total_users=total_users,
                         total_orders=total_orders,
                         pending_orders=pending_orders,
                         recent_orders=recent_orders)

# MANAGE BOOKS (Admin)
@app.route('/admin/books')
@login_required
def admin_books():
    """View all books (Admin)"""
    if not current_user.is_admin():
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    page = request.args.get('page', 1, type=int)
    books = Book.query.order_by(Book.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )
    
    return render_template('admin_books.html', books=books)

# ADD BOOK (Admin)
@app.route('/admin/book/add', methods=['GET', 'POST'])
@login_required
def add_book():
    """Add new book (Admin)"""
    if not current_user.is_admin():
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    form = BookForm()
    
    if form.validate_on_submit():
        # Handle file upload
        cover_image = 'default_cover.jpg'
        if form.cover_image.data:
            file = form.cover_image.data
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Add timestamp to filename to make it unique
                filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cover_image = filename
        
        # Create new book
        book = Book(
            title=form.title.data,
            author=form.author.data,
            isbn=form.isbn.data,
            price=form.price.data,
            stock_quantity=form.stock_quantity.data,
            category=form.category.data,
            description=form.description.data,
            publisher=form.publisher.data,
            publication_year=form.publication_year.data,
            pages=form.pages.data,
            language=form.language.data or 'English',
            rating=form.rating.data or 0.0,
            cover_image=cover_image
        )
        
        db.session.add(book)
        db.session.commit()
        
        flash(f'Book "{book.title}" added successfully!', 'success')
        return redirect(url_for('admin_books'))
    
    return render_template('add_book.html', form=form)

# EDIT BOOK (Admin)
@app.route('/admin/book/edit/<int:book_id>', methods=['GET', 'POST'])
@login_required
def edit_book(book_id):
    """Edit existing book (Admin)"""
    if not current_user.is_admin():
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    book = Book.query.get_or_404(book_id)
    form = BookForm()
    
    if form.validate_on_submit():
        # Handle file upload
        if form.cover_image.data:
            file = form.cover_image.data
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                book.cover_image = filename
        
        # Update book details
        book.title = form.title.data
        book.author = form.author.data
        book.isbn = form.isbn.data
        book.price = form.price.data
        book.stock_quantity = form.stock_quantity.data
        book.category = form.category.data
        book.description = form.description.data
        book.publisher = form.publisher.data
        book.publication_year = form.publication_year.data
        book.pages = form.pages.data
        book.language = form.language.data
        book.rating = form.rating.data
        
        db.session.commit()
        
        flash(f'Book "{book.title}" updated successfully!', 'success')
        return redirect(url_for('admin_books'))
    
    # Pre-fill form
    elif request.method == 'GET':
        form.title.data = book.title
        form.author.data = book.author
        form.isbn.data = book.isbn
        form.price.data = book.price
        form.stock_quantity.data = book.stock_quantity
        form.category.data = book.category
        form.description.data = book.description
        form.publisher.data = book.publisher
        form.publication_year.data = book.publication_year
        form.pages.data = book.pages
        form.language.data = book.language
        form.rating.data = book.rating
    
    return render_template('edit_book.html', form=form, book=book)

# DELETE BOOK (Admin)
@app.route('/admin/book/delete/<int:book_id>', methods=['POST'])
@login_required
def delete_book(book_id):
    """Delete book (Admin)"""
    if not current_user.is_admin():
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    book = Book.query.get_or_404(book_id)
    
    db.session.delete(book)
    db.session.commit()
    
    flash(f'Book "{book.title}" deleted successfully.', 'info')
    return redirect(url_for('admin_books'))

# MANAGE ORDERS (Admin)
@app.route('/admin/orders')
@login_required
def admin_orders():
    """View all orders (Admin)"""
    if not current_user.is_admin():
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    page = request.args.get('page', 1, type=int)
    orders = Order.query.order_by(Order.order_date.desc()).paginate(
        page=page, per_page=app.config['ORDERS_PER_PAGE'], error_out=False
    )
    
    return render_template('admin_orders.html', orders=orders)

# UPDATE ORDER STATUS (Admin)
@app.route('/admin/order/update/<int:order_id>', methods=['POST'])
@login_required
def update_order_status(order_id):
    """Update order status (Admin)"""
    if not current_user.is_admin():
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    order = Order.query.get_or_404(order_id)
    new_status = request.form.get('status')
    
    if new_status in ['Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled']:
        order.status = new_status
        db.session.commit()
        flash(f'Order #{order.id} status updated to {new_status}.', 'success')
    
    return redirect(url_for('admin_orders'))

# ==================== ERROR HANDLERS ====================

@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    db.session.rollback()
    return render_template('500.html'), 500

# ==================== DATABASE INITIALIZATION ====================

@app.cli.command()
def init_db():
    """Initialize the database with tables"""
    db.create_all()
    print('Database initialized!')

@app.cli.command()
def seed_db():
    """Seed database with sample data"""
    # Create admin user
    admin = User(username='admin', email='admin@bookstore.com', full_name='Admin User', role='admin')
    admin.set_password('admin123')
    db.session.add(admin)
    
    # Create sample user
    user = User(username='john', email='john@example.com', full_name='John Doe', phone='9841234567')
    user.set_password('password123')
    db.session.add(user)
    
    # Sample books data
    sample_books = [
        {
            'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '9780743273565',
            'price': 650.00, 'stock_quantity': 25, 'category': 'Fiction',
            'description': 'A classic American novel set in the Jazz Age.',
            'publisher': 'Scribner', 'publication_year': 1925, 'pages': 180, 'rating': 4.5
        },
        {
            'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'isbn': '9780061120084',
            'price': 700.00, 'stock_quantity': 30, 'category': 'Fiction',
            'description': 'A powerful story of racial injustice and childhood innocence.',
            'publisher': 'Harper Perennial', 'publication_year': 1960, 'pages': 324, 'rating': 4.8
        },
        {
            'title': '1984', 'author': 'George Orwell', 'isbn': '9780451524935',
            'price': 550.00, 'stock_quantity': 20, 'category': 'Fiction',
            'description': 'A dystopian social science fiction novel.',
            'publisher': 'Signet Classic', 'publication_year': 1949, 'pages': 328, 'rating': 4.7
        },
        {
            'title': 'Python Crash Course', 'author': 'Eric Matthes', 'isbn': '9781593279288',
            'price': 1200.00, 'stock_quantity': 15, 'category': 'Technology',
            'description': 'A hands-on, project-based introduction to programming.',
            'publisher': 'No Starch Press', 'publication_year': 2019, 'pages': 544, 'rating': 4.6
        },
        {
            'title': 'Clean Code', 'author': 'Robert C. Martin', 'isbn': '9780132350884',
            'price': 1500.00, 'stock_quantity': 12, 'category': 'Technology',
            'description': 'A handbook of agile software craftsmanship.',
            'publisher': 'Prentice Hall', 'publication_year': 2008, 'pages': 464, 'rating': 4.7
        },
        {
            'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'isbn': '9780062316097',
            'price': 900.00, 'stock_quantity': 18, 'category': 'History',
            'description': 'A brief history of humankind.',
            'publisher': 'Harper', 'publication_year': 2015, 'pages': 443, 'rating': 4.5
        },
        {
            'title': 'Atomic Habits', 'author': 'James Clear', 'isbn': '9780735211292',
            'price': 800.00, 'stock_quantity': 22, 'category': 'Self-Help',
            'description': 'An easy and proven way to build good habits.',
            'publisher': 'Avery', 'publication_year': 2018, 'pages': 320, 'rating': 4.8
        },
        {
            'title': 'The Alchemist', 'author': 'Paulo Coelho', 'isbn': '9780062315007',
            'price': 600.00, 'stock_quantity': 28, 'category': 'Fiction',
            'description': 'A magical story about following your dreams.',
            'publisher': 'HarperOne', 'publication_year': 1988, 'pages': 208, 'rating': 4.6
        }
    ]
    
    for book_data in sample_books:
        book = Book(**book_data)
        db.session.add(book)
    
    db.session.commit()
    print('Database seeded with sample data!')

# ==================== RUN APPLICATION ====================

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
        # Create upload folder if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    app.run(debug=True)
