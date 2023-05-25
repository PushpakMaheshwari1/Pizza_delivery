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