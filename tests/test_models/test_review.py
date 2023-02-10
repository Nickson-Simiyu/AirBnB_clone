#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "This is a great place!"

    def test_attributes(self):
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "This is a great place!")

    def test_to_dict(self):
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["place_id"], "123")
        self.assertEqual(review_dict["user_id"], "456")
        self.assertEqual(review_dict["text"], "This is a great place!")
        self.assertEqual(review_dict["__class__"], "Review")

if __name__ == "__main__":
    unittest.main()

