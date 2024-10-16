from datetime import datetime
from typing import Optional

from pydantic import Field, BaseModel


class UsersBase(BaseModel):
    username: str = Field(
        min_length=1,
        max_length=50,
        description="Username of the user",
        examples=["john_doe"],
    )
    email: str = Field(
        min_length=1,
        max_length=50,
        description="Email of the user",
        examples=["doe@mail.com"],
    )
    password: str = Field(
        min_length=1,
        max_length=50,
        description="Password of the user",
        examples=["password"],
    )
    created_at: datetime = Field(
        default_factory=datetime.now, description="Created at datetime"
    )
    updated_at: Optional[datetime] = Field(
        default=None, description="Updated at datetime"
    )


class UsersUpdate(BaseModel):
    username: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Username of the user",
        examples=["john_doe"],
    )
    email: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Email of the user",
        examples=["doe@mail.com"],
    )
    password: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Password of the user",
        examples=["password"],
    )
    updated_at: Optional[datetime] = Field(
        default=datetime.now, description="Updated at datetime"
    )
