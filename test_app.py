import unittest
from unittest.mock import patch
from app import run_training

class TestApp(unittest.TestCase):
    
    @patch('app.subprocess.run')
    def test_run_training(self, mock_run):
        mock_run.return_value = None
        with app.test_request_context(method='POST'):
            response = run_training()
            self.assertEqual(response.status_code, 200)