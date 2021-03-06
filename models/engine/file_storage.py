#!/usr/bin/env python3
"""file_storage.py
This module contains a class FileStorage that serializes and deserializes
BaseModel class instances
"""

import json
import os
from models.base_model import BaseModel

class FileStorage():
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Adds an object to the dictionnary __objects"""
        keys= obj.__class__.__name__ + '.' + obj.id
        self.__objects[keys]= obj

    def save(self):
        """Serializes __objects to the file __file_path"""
        new_object = {}
        for k, v in self.__objects.items():
            new_object[k] = v.to_dict()
        with open(self.__file_path, 'w+') as files:
            json.dump(new_object, files)

    def reload(self):
        """Deserializes __file_path to __objects"""
        if os.path.exists(FileStorage.__file_path):
            my_dict = {}
            with open(FileStorage.__file_path) as my_file:
                my_dict = json.load(my_file)
            for k, v in my_dict.items():
                FileStorage.__objects[k] = BaseModel(**v)
