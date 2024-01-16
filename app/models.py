from pydantic import BaseModel, Field, EmailStr, validator
from typing import List

# Post Schema
class Ads(BaseModel):
    id : int = Field(default=None, gt=0)
    title : str = Field(default=None, max_length=200,
                        json_schema_extra={
                                'title': 'Title',
                                'description': 'Ad title',
                                'examples': ['JSON Web Token 🔐'],
                            }
                        )
    content: str = Field(default=None, max_length=5000,
                        json_schema_extra={
                                'title': 'Content',
                                'description': 'Ad content',
                                'examples': [
                                    "is a JSON-based open standard proposed by the IETF for the creation of access tokens that enable the propagation of identity and privileges or 'claims'"
                                ],
                            }
                        )

    class Config:
        example_schema = {
            "Ad": {
                "title": "Batman the Dark Knight",
                "content": """Batman has to maintain the balance between heroism and
                            vigilantism to fight against a vile criminal known as the Joker, who intends to submerge
                            Gotham City in anarchy."""
            }
        }

        @validator('title')
        def validate_title(cls, value:str):
            if not value.isalnum():
                raise ValueError("Title must only contain alphanumeric characters.")
            return value

        @validator('content')
        def validate_content(cls, value:str):
            if not value.isprintable():
                raise ValueError("Content must only contain printable characters.")
            return value

class User(BaseModel):
    full_name: str = Field(default=None, 
                            json_schema_extra={
                                'title': 'Full Name',
                                'description': 'First and Last Name of the user',
                                'examples': ['Bruce Wayne'],
                            }
                        )
    email: EmailStr = Field(default=None,
                            json_schema_extra={
                                'title': 'Email',
                                'description': 'User email',
                                'examples': ['thetruedarknight007@batmail.com'],
                            }
                        )
    password : str = Field(default=None, 
                            json_schema_extra={
                                'title': 'Password',
                                'description': 'User password',
                                'examples': ['I_am_revenge'],
                            }
                        )

    class Cofig():
        example_schema = {
            "user": {
                "name": "Bruce Wayne",
                "email": "thetruedarknight007@batmail.com",
                "password": "I_am_revenge"
            }
        }

class UserLogin(BaseModel):
    email: EmailStr = Field(default=None,
                            json_schema_extra={
                                'title': 'Email',
                                'description': 'User email',
                                'examples': ['thetruedarknight007@batmail.com'],
                            }
                        )
    password : str = Field(default=None, 
                            json_schema_extra={
                                'title': 'Password',
                                'description': 'User password',
                                'examples': ['I_am_revenge'],
                            }
                        )

    class Cofig():
        example_eschema = {
            "login": {
                "email": "thetruedarknight007@batmail.com",
                "password": "I_am_revenge"
            }
        }