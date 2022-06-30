#!/usr/bin/python3

"""
The  User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that defines  public attributes
    with string empty
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
