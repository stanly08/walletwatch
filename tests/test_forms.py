import unittest
from app import create_app, db
from app.forms import RegistrationForm, ExpenseForm
from datetime import date


class FormsTestCase(unittest.TestCase):
    def setUp(self):
        # Initialize your Flask application and testing setup
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing purposes
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        # Clean up after each test
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_invalid_registration_form(self):
        # Create a test request context
        with self.app.test_request_context():
            form = RegistrationForm(username='t', email='invalidemail', password='short', confirm_password='mismatch')
            self.assertFalse(form.validate())  # Ensure that form validation fails
            self.assertIn('Invalid email address.', form.email.errors)
            self.assertIn('Field must be at least 8 characters long.', form.password.errors)
            self.assertIn('Field must be equal to password.', form.confirm_password.errors)

    # Test for valid ExpenseForm
    def test_valid_expense_form(self):
        # Create a test request context
        with self.app.test_request_context():
            form = ExpenseForm(amount=100, category='Groceries', description='Weekly groceries', date=date.today())
            self.assertTrue(form.validate())  # Ensure that form validation passes

    def test_invalid_expense_form(self):
        # Create a test request context
        with self.app.test_request_context():
            form = ExpenseForm(amount=-10, category='', description='miscellaneous', date=date.today())
            self.assertFalse(form.validate())  # Ensure that form validation fails
            self.assertIn('The expense amount must be greater than zero.', form.amount.errors)
            self.assertIn('This field is required.', form.category.errors)
            self.assertIn('Please provide a more specific description.', form.description.errors)

    # Test for valid RegistrationForm
    def test_valid_registration_form(self):
        # Create a test request context
        with self.app.test_request_context():
            form = RegistrationForm(username='testuser', email='test@example.com', password='password123', confirm_password='password123')
            if not form.validate():
                print("Form Errors:", form.errors)  # Print errors for debugging
            self.assertTrue(form.validate())  # Ensure that form validation passes


if __name__ == '__main__':
    unittest.main()


