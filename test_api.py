import unittest
import json


# Import the Flask application instance
from app import app
from app.database import init_db

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()  # Create a test client for the Flask application
        self.app.testing = True
        init_db()

    def test_get_funds(self):
        response = self.app.get('/funds')
        self.assertEqual(response.status_code, 200)

    def test_create_fund(self):
        response = self.app.post('/funds', data=json.dumps({
            'name': 'Beta Fund',
            'manager_name': 'Jane Doe',
            'description': 'A stable fund.',
            'nav': 500000,
            'date_of_creation': '2024-06-27',
            'performance': 3.0
        }), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_fund(self):
        self.app.post('/funds', data=json.dumps({
            'name': 'Beta Fund',
            'manager_name': 'Jane Doe',
            'description': 'A stable fund.',
            'nav': 500000,
            'date_of_creation': '2024-06-27',
            'performance': 3.0
        }), content_type='application/json')
        response = self.app.get('/funds/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Beta Fund', str(response.data))

    def test_update_fund(self):
        self.app.post('/funds', data=json.dumps({
            'name': 'Beta Fund',
            'manager_name': 'Jane Doe',
            'description': 'A stable fund.',
            'nav': 500000,
            'date_of_creation': '2024-06-27',
            'performance': 3.0
        }), content_type='application/json')
        response = self.app.put('/funds/1', data=json.dumps({'performance': 4.0}),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('4.0', str(response.data))

    def test_delete_fund(self):
        self.app.post('/funds', data=json.dumps({
            'name': 'Beta Fund',
            'manager_name': 'Jane Doe',
            'description': 'A stable fund.',
            'nav': 500000,
            'date_of_creation': '2024-06-27',
            'performance': 3.0
        }), content_type='application/json')
        response = self.app.delete('/funds/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('True', str(response.data))

if __name__ == '__main__':
    unittest.main()
