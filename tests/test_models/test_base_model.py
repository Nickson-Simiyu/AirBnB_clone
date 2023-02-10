#!/usr/bin/python3
import unittest
import models
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test BaseModel class."""

    def setUp(self):
        """Set up method that runs before each test."""
        self.base = BaseModel()

    def tearDown(self):
        """Tear down method that runs after each test."""
        del self.base

    def test_init_args(self):
        """Test the __init__ method with arguments."""
        b = BaseModel(id="1", name="Test")
        self.assertEqual(b.id, "1")
        self.assertEqual(b.name, "Test")

    def test_init_kwargs(self):
        """Test the __init__ method with keyword arguments."""
        b = BaseModel(**{'id': '1', 'name': 'Test'})
        self.assertEqual(b.id, "1")
        self.assertEqual(b.name, "Test")

    def test_init_no_args(self):
        """Test the __init__ method without arguments."""
        self.assertIsInstance(self.base, BaseModel)
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))

    def test_save(self):
        """Test the save method."""
        before = self.base.updated_at
        self.base.save()
        after = self.base.updated_at
        self.assertNotEqual(before, after)

    def test_to_dict(self):
        """Test the to_dict method."""
        bdict = self.base.to_dict()
        self.assertIsInstance(bdict, dict)
        self.assertTrue(hasattr(bdict, "__class__"))
        self.assertEqual(bdict["__class__"], "BaseModel")
        self.assertTrue(hasattr(bdict, "created_at"))
        self.assertTrue(hasattr(bdict, "updated_at"))
        self.assertTrue(hasattr(bdict, "id"))

    def test_str(self):
        """Test the __str__ method."""
        bstr = str(self.base)
        self.assertIsInstance(bstr, str)
        self.assertIn("[BaseModel]", bstr)
        self.assertIn("'id':", bstr)
        self.assertIn("'created_at':", bstr)
        self.assertIn("'updated_at':", bstr)

if __name__ == "__main__":
    unittest.main()

