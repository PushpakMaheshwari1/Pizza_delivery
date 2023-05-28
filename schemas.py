from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id        : Optional[int]
    username  : str
    email     : str
    password  : str
    is_staff  : Optional[bool]
    is_active : Optional[bool]

    class Config:
        orm_mode = True
        schemas_example = {
            'example' : {
                "username"  : "Pushpak",
                "email"     : "Pushpakmaheshwari140@gmail.com",
                "password"  : "pushpak",
                "is_staff"  : False,
                "is_active" : False
            }
        }


class Settings(BaseModel):
    authjwt_secret_key:str='d2629c262616373df381db932322d5555c71ae6dfece36644da3ddf0cdb20913'

class LoginModel(BaseModel):
    username:str
    password:str