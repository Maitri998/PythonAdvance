from pydantic import BaseModel, Field
from typing import Optional

class BookCreate(BaseModel):
    title: str = Field(..., min_length=1, example="The Hobbit")
    author: str = Field(..., min_length=1, example="J.R.R. Tolkien")
    year: int = Field(..., ge=0, example=1937)
    available: Optional[bool] = True

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, example="Updated Title")
    author: Optional[str] = Field(None, example="Updated Author")
    year: Optional[int] = Field(None, ge=0, example=2000)
    available: Optional[bool] = None
