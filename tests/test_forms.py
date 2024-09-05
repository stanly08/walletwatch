import unittest
from app.forms import RegistrationForm, LoginForm, ExpenseForm
from datetime import datetime

class FormsTestCase(unittest.TestCase):

    def test_valid_registration_form(self):
        form = RegistrationForm(username='testuser', email='test@example.com', password='Password1!', confirm_password='Password1!')
        self.assertTrue(form.validate())

    def test_invalid_registration_form(self):
        form = RegistrationForm(username='t', email='invalidemail', password='short', confirm_password='mismatch')
        self.assertFalse(form.validate())

    def test_valid_expense_form(self):
        form = ExpenseForm(amount=1500.0, category='Network', description='Wifi payment', date=datetime.utcnow())
        self.assertTrue(form.validate())

    def test_invalid_expense_form(self):
        form = ExpenseForm(amount='abc', category='', description='', date=None)
        self.assertFalse(form.validate())

if __name__ == '__main__':
    unittest.main()
