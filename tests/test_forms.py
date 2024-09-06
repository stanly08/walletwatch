import unittest
from app import create_app
from app.forms import RegistrationForm, ExpenseForm

class FormsTestCase(unittest.TestCase):
    def setUp(self):
        # Create an app instance
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_invalid_expense_form(self):
        form = ExpenseForm(amount='abc', category='', description='', date=None)
        self.assertFalse(form.validate())

    def test_invalid_registration_form(self):
        form = RegistrationForm(username='t', email='invalidemail', password='short', confirm_password='mismatch')
        self.assertFalse(form.validate())

    def test_valid_expense_form(self):
        form = ExpenseForm(amount=1500.00, category='Network', description='Wifi payment', date=datetime.utcnow())
        self.assertTrue(form.validate())

    def test_valid_registration_form(self):
        form = RegistrationForm(username='testuser', email='test@example.com', password='Password1!', confirm_password='Password1!')
        self.assertTrue(form.validate())

if __name__ == '__main__':
    unittest.main()

