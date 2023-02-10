#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_instance(self):
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        self.assertEqual(self.amenity.name, "")

if __name__ == "__main__":
    unittest.main()

