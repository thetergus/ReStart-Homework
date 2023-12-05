from pydantic import BaseModel, field_validator
from .author import Author

class BookItem(BaseModel):
    book_name:str
    book_author:Author
    year_published:int
    
    @field_validator("year_published")
    @classmethod
    def check_valid_year(cls,year_published: int):
        # assert (year_published => -3000) and year_published!=<2023, "Wrong value for year of publishing, -3000 to 2023 only"
        assert -3000 <= year_published <= 2023, "Wrong value for year of publishing, -3000 to 2023 only"
        return year_published
    
