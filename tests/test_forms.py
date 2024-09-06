import unittest
from app import create_app
from app.forms import RegistrationForm, ExpenseForm

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
            self.assertIn('Field must be equal to confirm_password.', form.confirm_password.errors)


    def test_invalid_expense_form(self):
        form = ExpenseForm(amount='abc', category='', description='', date=None)
        self.assertFalse(form.validate())


    def test_valid_expense_form(self):
        form = ExpenseForm(amount=1500.00, category='Network', description='Wifi payment', date=datetime.utcnow())
        self.assertTrue(form.validate())

    def test_valid_registration_form(self):
        form = RegistrationForm(username='testuser', email='test@example.com', password='Password1!', confirm_password='Password1!')
        self.assertTrue(form.validate())

if __name__ == '__main__':
    unittest.main()

