#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self):
"""Generate a unique id"""
        self.id = str(uuid.uuid4())
"""Set the creation and update times"""
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
"""Update the updated_at time"""
        self.updated_at = datetime.now()

    def to_dict(self):
"""Create a dictionary representation of the instance"""
        data = {
            "__class__": self.__class__.__name__,
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
        data.update(self.__dict__)
        return data

