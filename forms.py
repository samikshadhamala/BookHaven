"""
Forms for Online Bookstore using Flask-WTF
Includes validation for user input
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, TextAreaField, FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, NumberRange
from models import User, Book

class RegistrationForm(FlaskForm):
    """Form for new user registration"""
    username = StringField('Username', 
                          validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', 
                       validators=[DataRequired(), Email()])
    full_name = StringField('Full Name', 
                           validators=[DataRequired(), Length(min=2, max=100)])
    phone = StringField('Phone Number', 
                       validators=[Length(max=20)])
    password = PasswordField('Password', 
                            validators=[DataRequired(), Length(min=8, message='Password must be at least 8 characters')])
    confirm_password = PasswordField('Confirm Password', 
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        """Check if username already exists"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')
    
    def validate_email(self, email):
        """Check if email already exists"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different one.')


class LoginForm(FlaskForm):
    """Form for user login"""
    username = StringField('Username', 
                          validators=[DataRequired()])
    password = PasswordField('Password', 
                            validators=[DataRequired()])
    submit = SubmitField('Login')


class BookForm(FlaskForm):
    """Form for adding/editing books (Admin)"""
    title = StringField('Book Title', 
                       validators=[DataRequired(), Length(max=200)])
    author = StringField('Author', 
                        validators=[DataRequired(), Length(max=100)])
    isbn = StringField('ISBN', 
                      validators=[DataRequired(), Length(min=10, max=13)])
    price = FloatField('Price (NPR)', 
                      validators=[DataRequired(), NumberRange(min=0, message='Price must be positive')])
    stock_quantity = IntegerField('Stock Quantity', 
                                 validators=[DataRequired(), NumberRange(min=0, message='Stock cannot be negative')])
    category = SelectField('Category', 
                          choices=[
                              ('Fiction', 'Fiction'),
                              ('Non-Fiction', 'Non-Fiction'),
                              ('Science', 'Science'),
                              ('Technology', 'Technology'),
                              ('History', 'History'),
                              ('Biography', 'Biography'),
                              ('Self-Help', 'Self-Help'),
                              ('Business', 'Business'),
                              ('Children', 'Children'),
                              ('Romance', 'Romance'),
                              ('Mystery', 'Mystery'),
                              ('Fantasy', 'Fantasy')
                          ],
                          validators=[DataRequired()])
    description = TextAreaField('Description', 
                               validators=[Length(max=1000)])
    publisher = StringField('Publisher', 
                           validators=[Length(max=100)])
    publication_year = IntegerField('Publication Year', 
                                   validators=[NumberRange(min=1900, max=2025)])
    pages = IntegerField('Number of Pages', 
                        validators=[NumberRange(min=1)])
    language = StringField('Language', 
                          validators=[Length(max=20)])
    rating = FloatField('Rating (0-5)', 
                       validators=[NumberRange(min=0, max=5)])
    cover_image = FileField('Book Cover', 
                           validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webp'], 'Images only!')])
    submit = SubmitField('Save Book')


class ProfileForm(FlaskForm):
    """Form for updating user profile"""
    full_name = StringField('Full Name', 
                           validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', 
                       validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', 
                       validators=[Length(max=20)])
    address = TextAreaField('Address', 
                           validators=[Length(max=500)])
    submit = SubmitField('Update Profile')


class CheckoutForm(FlaskForm):
    """Form for checkout and order placement"""
    shipping_address = TextAreaField('Shipping Address', 
                                    validators=[DataRequired(), Length(min=10, max=500)])
    shipping_city = StringField('City', 
                               validators=[DataRequired(), Length(max=100)])
    shipping_postal_code = StringField('Postal Code', 
                                      validators=[DataRequired(), Length(max=20)])
    shipping_phone = StringField('Contact Phone', 
                                validators=[DataRequired(), Length(min=10, max=20)])
    payment_method = SelectField('Payment Method', 
                                choices=[
                                    ('Cash on Delivery', 'Cash on Delivery'),
                                    ('Online Payment', 'Online Payment (Coming Soon)')
                                ],
                                validators=[DataRequired()])
    submit = SubmitField('Place Order')


class SearchForm(FlaskForm):
    """Form for searching books"""
    query = StringField('Search', validators=[Length(max=100)])
    category = SelectField('Category', 
                          choices=[
                              ('', 'All Categories'),
                              ('Fiction', 'Fiction'),
                              ('Non-Fiction', 'Non-Fiction'),
                              ('Science', 'Science'),
                              ('Technology', 'Technology'),
                              ('History', 'History'),
                              ('Biography', 'Biography'),
                              ('Self-Help', 'Self-Help'),
                              ('Business', 'Business'),
                              ('Children', 'Children'),
                              ('Romance', 'Romance'),
                              ('Mystery', 'Mystery'),
                              ('Fantasy', 'Fantasy')
                          ])
    submit = SubmitField('Search')
