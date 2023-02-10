#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up method for the tests"""
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down method for the tests"""
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method"""
        obj = User()
        obj.id = "12345"
        obj.email = "hbtn@holbertonschool.com"
        self.storage.new(obj)
        self.assertEqual(self.storage.all(), {'User.12345': obj})

    def test_new(self):
        """Test the new method"""
        obj = User()
        obj.id = "12345"
        obj.email = "hbtn@holbertonschool.com"
        self.storage.new(obj)
        key = 'User.12345'
        self.assertEqual(self.storage.all()[key].email, "hbtn@holbertonschool.com")

    def test_save(self):
        """Test the save method"""
        obj = User()
        obj.id = "12345"
        obj.email = "hbtn@holbertonschool.com"
        self.storage.new(obj)
        self.storage.save()
        with open("test.json", "r") as file:
            self.assertEqual(json.loads(file.read()), {'User.12345': obj.to_dict()})

    def test_reload(self):
        """Test the reload method"""
        obj = User()
        obj.id = "12345"
        obj.email = "hbtn@holbertonschool.com"
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = 'User.12345'
        self.assertEqual(self.storage.all()[key].email, "hbtn@holbertonschool.com")

if __name__ == '__main__':
    unittest.main()

