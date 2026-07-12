def test_practice():
    products = [
    {"name":"aplle","price":17},
    {"name":"banana","price":25},
    {"name":"phone","price":20}
    ]
    assert len(products) > 0

    for product in products:
        assert "name" in product
        assert isinstance(product["name"],str)

        assert "price" in product
        assert isinstance(product["price"],int)
        assert product["price"] > 0

def test_books_list():
    books = [
    {"title":"love test","author":{
        "name":"Anna",
        "age":30
        }
    },
    {"title":"dont love test","pages":25},
    {"title":"good book test","pages":20}
    ]

    assert len(books) > 0
    for book in books:
        assert "title" in book
        assert isinstance(book["title"],str)
        assert len(book["title"]) > 0 #на длину норм если для строк

        assert "pages" in book
        assert isinstance(book["pages"],int)
        assert book["pages"] > 0


def test_books_with_author():
    books = [
{
    "title": "Love testic",
    "author": {
        "name": "Artem",
        "age": 30
    }
},
{
    "title": "good test",
    "author": {
        "name": "inna",
        "age": 20
    }
},
{
    "title": "dont Love test",
    "author": {
        "name": "Anna",
        "age": 22
    }
}
]
    for book in books:
        assert "title" in book
        assert isinstance(book["title"], str)
        assert len(book["title"]) > 0

        assert "author" in book
        assert isinstance(book["author"], dict)
       

        assert "name" in book["author"]
        assert isinstance(book["author"]["name"], str)
        assert len(book["author"]["name"]) > 0

        assert "age" in book["author"]
        assert isinstance(book["author"]["age"], int)
        assert book["author"]["age"] > 0

def test_books_wich_genres():
    books = [
{
     "title": "Love testic",
     "genres":["romance","drama"]
},
{
     "title": "good test",
     "genres":["thriller","phih"]
    
},
{
     "title": "dont Love test",
     "genres":["fonk","disco"]
    
 }
]
    for book in books:
        assert "title" in book
        assert isinstance(book["title"], str)
        assert len(book["title"]) > 0

        assert "genres" in book
        assert isinstance(book["genres"], list)
        assert len(book["genres"]) > 0
        
        for genre in book["genres"]:
            assert isinstance(genre, str)
            assert len(genre) > 0

            if genre == "romance":
                assert book["title"] == "Love testic"
            if genre == "thriller":
                assert book["title"] == "good test"

                #books       # список всех книг
#book        # одна книга
#book["author"]              # словарь автора
#book["author"]["name"]      # имя автора
#book["genres"]              # список жанров
#genre                       # один жанр
#[]   # список — list
#{}   # словарь — dict
#""   # строка — str
#17   # целое число — int
#books = []          # список
#book = {}           # словарь
#"title"             # строка
#30                  # число
