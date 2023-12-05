from pydantic import ValidationError
from dto.author import Author
from dto.bookItem import  BookItem
from dto.bookStore import BookStore
from typing import Dict, List
from fastapi import FastAPI, HTTPException


my_book_items_dict: Dict[str, BookItem]={}
app=FastAPI()

def creating_items():
    print()
#correct start
    try: 
        my_author1= Author(
            author_name="J.R.R. Tolkien",
            author_id="SIAK-1144"
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')

    else:
        print(f'POSITIVE : Author 1:  {my_author1}')

    try: 
        my_author2= Author(
            author_name="Dan Brown",
            author_id="DBUS-7028"
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')
    else:
        print(f'POSITIVE : Author 2:  {my_author2}')

    try:
        my_book1= BookItem(
            book_name= "The Lord of The Rings",
            book_author=    my_author1,
            year_published="1954"
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')
    else:
        print(f'POSITIVE : book 1:  {my_book1}')

    try:
        my_book2= BookItem(
            book_name= "DaVinci Code",
            book_author=    my_author2,
            year_published="2003"
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')
    else:
        print(f'POSITIVE : book 2:  {my_book2}')

    try:
        my_book_store1=BookStore(
            name_of_bookstore="Puro Verso",
            book_shelve=[my_book1, my_book2]
        )
    except ValidationError as ve:
        print(f'something went wrong with validation')        
    else:
        print(f'POSITIVE : BookStore 1 :  {my_book_store1}'), print()#giving spacing
# end of correct entries

#incorrect values as variable for print referencing 
    wrong_author_name1="J.R.R. 4olkien"
    wrong_author_name2="j.j.r. tolkien"
    wrong_author_id="SI3K-1?44"
    wrong_publishing_year ="2025"
    wrong_book_shelve=[my_book1, my_author1]
#end of incorrect values as variable for print referencing

#start of TRYing wrong entries
    try: #wrong name
        my_wrong_author1= Author(
            author_name=wrong_author_name1,
            author_id=wrong_author_id
        )
    except ValidationError as ve:
        print(f'Inserting WRONG autor name ({wrong_author_name1})')

    try: #wrong name
        my_wrong_author2= Author(
            author_name=wrong_author_name2,
            author_id=wrong_author_id
        )
    except ValidationError as ve:
        print(f'Inserting WRONG autor name ({wrong_author_name2})')    

    try: #wrong id
        my_wrong_author3= Author(
            author_name="J.R.R. Tolkien",
            author_id=wrong_author_id
        )
    except ValidationError as ve:
        print(f'Inserting WRONG autor id ({wrong_author_id})')

    try: #wrong publishing year
        
        my_wrong_book1= BookItem(
            book_name= "The Lord of The Rings",
            book_author= my_author1,
            year_published=wrong_publishing_year
        )
    except ValidationError as ve:
        print(f'Inserting WRONG publishing year ({wrong_publishing_year})')

    try: #wrong item added instead of BOOK class item
        my_wrong_book_store1=BookStore(
            name_of_bookstore="Puro Verso",
            book_shelve=wrong_book_shelve
        )
    except ValidationError as ve:
        print(f'Inserting WRONG bookshelve ({wrong_book_shelve})')


def main():

    creating_items()

#  2 my_book_items_dict[str,BookItem]    V
#  3 Put /boobks/{name}                           V
#  4 get /books/{name}                             V
#  5 Create delete Api                              V
#  6 Create GET APIs (all items saved)      V

#API TIMES
@app.put("/books/{name}") 
def createBook(book:BookItem, name:str)-> None:
    my_book_items_dict[name]=book
    print("Added : ", book.book_name)

@app.get("/books/{name}")
def readBook(name:str)-> BookItem:
    if name in my_book_items_dict.keys():        
        print("Book Found: ", my_book_items_dict[name])
        return my_book_items_dict[name]
    else:
        my_message= "Book ", name ," has not been found"
        # raise HTTPException(status_code=404, detail=("Book has not been found"))
        raise HTTPException(status_code=404, detail=my_message)
    
@app.get("/books/")
def getBooks()-> List[BookItem]:
    print("Success, like hot chocolate in winter")
    return  my_book_items_dict.values()
    
@app.delete("/books/{name}")
def deleteBook(name:str)-> Dict:
    if name in my_book_items_dict.keys():
        deleted_item=my_book_items_dict[name]
        my_book_items_dict.pop(name)
        print("Deleting :", deleted_item) 
        return {"message": "Deleted the following: " + str(deleted_item.book_name)}
    else:
        raise HTTPException(status_code=404, detail="Book not found")

if __name__=="__main__":
    main()