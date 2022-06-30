#!/usr/bin/python3
"""
Review class inherits from BaseModel
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that defines public class
    atributes with tree  empty strings
    """

    place_id = ""
    user_id = ""
    text = ""
