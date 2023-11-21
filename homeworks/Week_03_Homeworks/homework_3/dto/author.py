from pydantic import BaseModel, field_validator
import re

class Author(BaseModel):
    author_name:str
    author_id:str

    @field_validator("author_name")
    @classmethod
    def check_author_name(cls,author_name: str):
        assert author_name.istitle(), "Author name has NOT  been  capitalized properly "
        return author_name

    @field_validator("author_id")
    @classmethod
    def check_author_id(cls,author_id: str):
        id_format=re.compile(r'^[A-Z]{4}-\d{4}$')
        assert id_format.match(author_id), "Yo! That's not a valid Author ID, we need 4 CAPITAL  letters, a dash, and 4 numbers, no spaces."
        return author_id
