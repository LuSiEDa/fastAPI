from enum import Enum
from typing import Annotated

from pydantic import BaseModel, conint


class GenderEnum(str, Enum):
    male = "male"
    female = "female"


class UserCreateRequest(BaseModel):
    username: str
    age: int
    gender: GenderEnum
    # app/schemas/users.py


class UserUpdateRequest(BaseModel):
    username: str | None = None
    age: int | None = None


class UserSearchRequest(BaseModel):
    model_config = {"extra": "forbid"}
    username: str | None = None
    age: Annotated[int | None, conint(gt=0)] = None
    gender: GenderEnum | None = None
