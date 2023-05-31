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

class OrderModel(BaseModel):
    id : Optional[int]
    quantity : int
    order_status : Optional[str] = "PENDING" 
    pizza_size : Optional[str] = "SMALL"
    user_id : Optional[int]

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "quantity" : 2,
                "pizza_size":"LARGE" 
            }
        }