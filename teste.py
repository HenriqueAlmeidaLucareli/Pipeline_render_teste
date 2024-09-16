import unittest
from app import app

#testando
class BasicTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

#verificando
if __name__ == '__main__':
    unittest.main()