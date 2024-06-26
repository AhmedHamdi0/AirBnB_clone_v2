#!/usr/bin/python3

"""Defines the FileStorage class."""

import json
import os
from datetime import datetime


class FileStorage:
    """
    Serialize instances to a JSON file and
    deserialize JSON file to instances.
    """

    __file_path: str = 'file.json'
    __objects: dict = {}

    def all(self, cls=None):
        """Return the list of objects of one type of class."""
        if cls is None:
            return FileStorage.__objects
        else:
            return {key: value for key, value in self.__objects.items() if type(value) is cls}

    def new(self, obj):
        """Add a new object to the storage."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to JSON file (__file_path)."""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            data = {key: value.to_dict()
                    for key, value in FileStorage.__objects.items()}
            json.dump(data, file, indent=4)

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside."""
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in FileStorage.__objects:
            del FileStorage.__objects[key]

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "BaseModel":
                {"id": str,
                 "created_at": datetime,
                 "updated_at": datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attributes
