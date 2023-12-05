from fastapi.testclient import TestClient
from main import app
import pytest

@pytest.fixture
def client():   #refreshing, creating a new client every time.
    yield TestClient(app)

@pytest.fixture
def good_payload():
    return    {
        "book_name": "DaVinci Code",
        "book_author": {
            "author_name": "Dan Brown",
            "author_id": "DDAA-5948"
        },
        "year_published": 2003
    }

@pytest.fixture
def bad_payload():    
    return{
        "book_name": "DaVinci Code", 
        "book_author": {
            "author_name": "dan Brown", 
            "author_id": "DDA-5948"     
        },
        "year_published": 2029
    }



def testing_incorrect_put_api______(client, bad_payload):
    response = client.put(f"/books/{bad_payload['book_name']}", json= bad_payload)        
    assert response.status_code==422    

def testing_put_api________________(client, good_payload):
    response = client.put(f"/books/{good_payload['book_name']}", json= good_payload)  
    assert response.status_code==200    

def test_get_item__________________(client):
    response = client.get("/books/")
    assert response.status_code==200

def test_delete_good_______________(client,good_payload): 
    response = client.delete(f"/books/{good_payload['book_name']}/")
    assert response.status_code==200       
    
def test_put_then_get_api__________(client, good_payload):
        response = client.put(f"/books/{good_payload['book_name']}", json=good_payload)
        assert response.status_code==200 
        
        response = client.get(f"/books/{good_payload['book_name']}")
        assert response.status_code == 200 
        assert response.json() == good_payload
        

@pytest.mark.parametrize("payload, http_code",
                         [({
                            "book_name": "A Thousand Faces",
                            "book_author": {
                                "author_name": "J. Campbell",
                                "author_id": "CAMP-1496"
                            },
                            "year_published": 2000
                            }
                             ,200),
                          ({
                            "book_name": "Monster Manual", 
                            "book_author": {
                                "author_name": "lizards of da koast", 
                                "author_id": "MTG-A948"     
                            },
                            "year_published": 2029
                             },422)],
)
def test_many_put_api(client,payload,http_code):
    assert client.put(f"/books/{payload['book_name']}", json=payload).status_code==http_code

    
