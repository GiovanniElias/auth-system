import unittest
from utils.validator import LoginValidator
from models.requestinfo import RequestInfo
from exceptions.exceptions import UserNotFoundException

class TestLoginValidator(unittest.TestCase):

    def test_user_exists(self):
        request_info = RequestInfo(dict(email="banana",password="12789123"))
        validator = LoginValidator(request_info)

        with self.assertRaises(UserNotFoundException):
            validator._validate_email()

if __name__ == '__main__': 
    unittest.main()