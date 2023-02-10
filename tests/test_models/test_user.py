#!/usr/bin/python3
"""
Test User Classes
"""
import unittest
from models.user import User
from models.base_model import BaseModel
import pep8

class Test_UserModel(unittest.TestCase):
    """
    Test the user model class
    """

    def setUp(self):
        self.model = User()
        self.model.save()

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_attributes_User(self):
        """check User attributes"""
        self.assertTrue('id' in self.model.__dict__)
        self.assertTrue('created_at' in self.model.__dict__)
        self.assertTrue('updated_at' in self.model.__dict__)
        self.assertFalse('email' in self.model.__dict__)
        self.assertFalse('password' in self.model.__dict__)
        self.assertFalse('first_name' in self.model.__dict__)
        self.assertFalse('last_name' in self.model.__dict__)

    def test_is_subclass_User(self):
        """test if User is subclass of BaseModel"""
        self.assertTrue(issubclass(self.model.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()

