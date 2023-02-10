#!/usr/bin/python3
import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from hbnb import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()

    def test_do_create(self):
        self.hbnb.onecmd("create BaseModel")
        bm_obj = storage.all()
        bm_key = list(bm_obj.keys())[0]
        self.assertEqual(bm_obj[bm_key].__class__.__name__, "BaseModel")
        self.hbnb.onecmd("create User")
        user_obj = storage.all()
        user_key = list(user_obj.keys())[1]
        self.assertEqual(user_obj[user_key].__class__.__name__, "User")

    def test_do_show(self):
        bm = BaseModel()
        bm.save()
        bm_key = bm.__class__.__name__ + "." + bm.id
        self.hbnb.onecmd("show BaseModel {}".format(bm.id))
        output = self.hbnb.stdout.getvalue().strip()
        self.assertEqual(output, str(bm_obj[bm_key]))

    def test_do_destroy(self):
        bm = BaseModel()
        bm.save()
        bm_key = bm.__class__.__name__ + "." + bm.id
        self.hbnb.onecmd("destroy BaseModel {}".format(bm.id))
        self.assertFalse(bm_key in storage.all().keys())

    def test_do_all(self):
        bm = BaseModel()
        bm.save()
        self.hbnb.onecmd("all")
        output = self.hbnb.stdout.getvalue().strip()
        bm_key = bm.__class__.__name__ + "." + bm.id
        self.assertIn(str(bm_obj[bm_key]), output)

    def test_do_count(self):
        bm = BaseModel()
        bm.save()
        self.hbnb.onecmd("count BaseModel")
        output = self.hbnb.stdout.getvalue().strip()
        self.assertEqual(output, "1")

    def test_do_update(self):
        bm = BaseModel()
        bm.save()
        bm_key = bm.__class__.__name__ + "." + bm.id
        self.hbnb.onecmd("update BaseModel {} name \"Test\"".format(bm.id))
        bm_obj = storage.all()
        self.assertEqual(bm_obj[bm_key].name, "Test")

   
i
