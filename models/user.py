#!/usr/bin/python3
"""User Class Module"""
from models.base_model import BaseModel

class User(BaseModel):
    """Class that represents Users"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
