#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def test_attributes(self):
        self.assertEqual(hasattr(self.place, "city_id"), True)
        self.assertEqual(hasattr(self.place, "user_id"), True)
        self.assertEqual(hasattr(self.place, "name"), True)
        self.assertEqual(hasattr(self.place, "description"), True)
        self.assertEqual(hasattr(self.place, "number_rooms"), True)
        self.assertEqual(hasattr(self.place, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.place, "max_guest"), True)
        self.assertEqual(hasattr(self.place, "price_by_night"), True)
        self.assertEqual(hasattr(self.place, "latitude"), True)
        self.assertEqual(hasattr(self.place, "longitude"), True)
        self.assertEqual(hasattr(self.place, "amenity_ids"), True)

    def test_types(self):
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(type(self.place.amenity_ids), list)

    def test_inheritance(self):
        self.assertEqual(issubclass(Place, BaseModel), True)

    def test_str_method(self):
        self.assertEqual(str(self.place).startswith("[Place]"), True)

if __name__ == "__main__":
    unittest.main()

