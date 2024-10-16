from datetime import datetime

from pydantic import BaseModel, Field
from typing import Optional


class TodoBase(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=50,
        description="Title of the todo",
        examples=["Buy Milk"],
    )
    description: Optional[str] = Field(
        max_length=100, description="Description of the todo", examples=["Buy 2L Milk"]
    )
    priority: int = Field(
        ge=1, le=5, description="Priority of the todo 1-5", examples=[1]
    )
    completed: Optional[bool] = False
    created_at: datetime = Field(
        default_factory=datetime.now, description="Created at datetime"
    )
    updated_at: Optional[datetime] = Field(
        default=None, description="Updated at datetime"
    )


class TodoUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1,
        max_length=50,
        description="Title of the todo",
        examples=["Buy Milk"],
    )
    description: Optional[str] = Field(
        None,
        max_length=100,
        description="Description of the todo",
        examples=["Buy 2L Milk"],
    )
    priority: Optional[int] = Field(
        None, ge=1, le=5, description="Priority of the todo 1-5", examples=[1]
    )
    completed: Optional[bool] = False
    updated_at: Optional[datetime] = Field(
        default=datetime.now, description="Updated at datetime"
    )
