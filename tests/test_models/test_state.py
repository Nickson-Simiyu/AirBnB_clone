 #!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_attributes(self):
        s = State()
        self.assertEqual(s.name, "")

    def test_save(self):
        s = State()
        s.name = "California"
        s.save()
        self.assertNotEqual(s.created_at, s.updated_at)
        
    def test_to_dict(self):
        s = State()
        s.name = "California"
        s_dict = s.to_dict()
        self.assertIn("name", s_dict)
        self.assertEqual(s_dict["name"], "California")
        self.assertIn("__class__", s_dict)
        self.assertEqual(s_dict["__class__"], "State")
        
    def test_str(self):
        s = State()
        s.name = "California"
        s_str = str(s)
        self.assertIn("'name': 'California'", s_str)
        self.assertIn("'__class__': 'State'", s_str)
        
if __name__ == '__main__':
    unittest.main()

