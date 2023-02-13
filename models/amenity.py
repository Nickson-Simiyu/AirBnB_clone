#!/usr/bin/python3
"""
Class Amenity, inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents the Amenity class and inherits from BaseModel.
    Public class attribute:
        name: empty string
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity class with the BaseModel's init method."""
        super().__init__(*args, **kwargs)
