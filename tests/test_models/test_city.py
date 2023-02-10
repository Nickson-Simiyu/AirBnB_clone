#!/usr/bin/python3
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def tearDown(self):
        pass

    def test_City_inherits_from_BaseModel(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_City_has_state_id_attribute(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertIsInstance(self.city.state_id, str)

    def test_City_has_name_attribute(self):
        self.assertTrue(hasattr(self.city, "name"))
        self.assertIsInstance(self.city.name, str)

if __name__ == "__main__":
    unittest.main()

