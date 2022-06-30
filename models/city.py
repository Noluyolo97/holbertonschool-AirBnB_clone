#!/usr/bin/python3
"""
City class that inherits from BaseModel
"""


from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class that defines public class atribute
    with two  empty strings
    """

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
