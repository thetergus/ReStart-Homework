#pytest // python -m pytest // python3 -m pytest
#python -m pytest -vvl
#pytests looks for files named with test_*.py(?), with it, it's one way to do unit tests.

# Setup testing structure = V
# Test PUT api to 200       = V
# Test PUT api to 400       = V , got 422 couldn't custom, Discord said it was ok to be 422
# Test GET api body resp. = V
# Test DELETE Api             = V
# Test GET ALL api            = V


from fastapi.testclient import TestClient
from main import app
from dto.author import Author
from dto.bookItem import  BookItem
from typing import Dict, List


client = TestClient(app)

my_book1=BookItem(
    book_name= "DaVinci Code",
    book_author= Author(
        author_name= "Dan Brown",
        author_id= "DDAA-5948"
    ),
    year_published= 2003
)

my_book2=BookItem(
    book_name= "The Lord of the Rings",
    book_author= Author(
        author_name= "J.R.R. Tolkien",
        author_id= "SIAK-1144"
    ),
    year_published= 1954
)

def test_DELETE_all_books_____________():
    response = client.delete("/books/") 
    assert response.status_code==200

def test_PUT_good_1___________________():
    response = client.put("/books/DaVinci%20Code/", json=
        {
            "book_name": "DaVinci Code",
            "book_author": {
                "author_name": "Dan Brown",
                "author_id": "DDAA-5948"
            },
            "year_published": 2003
        }
        )
    assert response.status_code==200

def test_PUT_good_2___________________():
    response = client.put("/books/The%20Lord%20of%20the%20Rigns/", json=
        {
            "book_name": "The Lord of the Rings",
            "book_author": {
                "author_name": "J.R.R. Tolkien",
                "author_id": "SIAK-1144"
            },
            "year_published": 1954
        }
        )
    assert response.status_code==200

def test_PUT_bad_author_name__________():
    response = client.put("/books/1222/", json=
        {
            "book_name": "Lettuce Attempt",
            "book_author": {
                "author_name": "brown Rice",
                "author_id": "FTHA-5351"
            },
            "year_published": 2003
        }
        )
    assert response.status_code==422

def test_PUT_bad_author_code__________():
    response = client.put("/books/1222/", json=
        {
            "book_name": "Lettuce Attempt",
            "book_author": {
                "author_name": "brown Rice",
                "author_id": "ftHA-5351"
            },
            "year_published": 2003
        }
        )
    assert response.status_code==422

def test_PUT_bad_publishing_year______(): #
    response = client.put("/books/1222/", json=
        {
            "book_name": "Lettuce",
            "book_author": {
                "author_name": "Brown Rice",
                "author_id": "FTHA-5351"
            },
            "year_published": 2028
        }
        )
    print("publishing year code", response.status_code)
    assert response.status_code==422

def test_GET_single_good______________():
    response = client.get("/books/DaVinci%20Code/")
    assert response.status_code==200   
    assert BookItem(**response.json()) ==my_book1 #unpacking the response.json into python keyword args
    # assert response.json()==my_book1

def test_GET_single_bad_______________():
    response = client.get("/books/Ranting/")
    assert response.status_code==404


def test_GET_all_good_exists__________(): #there is no validation scripted  for this
    response = client.get("/books/")
    assert response.status_code==200
    # books=[]
    # for book in response.json():
    #         books.append(book)
    # assert books ==List[my_book1,my_book2]


def test_DELETE_bad___________________():    #Doing Bad one first since we currently have a book
    response = client.delete("/books/Vuvuzelas/")
    assert response.status_code==404   


def test_DELETE_good__________________(): 
    response = client.delete("/books/DaVinci%20Code/")
    assert response.status_code==200   


def test_DELETE_good_confirm__________(): 
    response = client.delete("/books/DaVinci%20Code/")
    assert response.status_code==404   


def test_DELETE_good_2________________(): 
    response = client.delete("/books/The%20Lord%20of%20the%20Rigns/")
    assert response.status_code==200   


def test_DELETE_good_confirm_2________(): 
    response = client.delete("/books/The%20Lord%20of%20the%20Rigns/")
    assert response.status_code==404       
    
    
def test_DELETE_good_confirm_2________(): 
    response = client.delete("/books/The%20Lord%20of%20the%20Rigns/")
    assert response.status_code==404       
    
    
def test_GET_all_good_no_data_________():
    response = client.get("/books/")  # Make sure to use the correct path with a trailing slash
    assert response.status_code == 404
    

