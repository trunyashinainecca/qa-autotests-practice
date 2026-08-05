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
    {"title":"dont love test","pages":25},
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

def test_if_practic():
    user = {
    "name":"Inessa",
    "age":19
    }
    assert "name" in user
    assert isinstance(user["name"],str)
    assert "age" in user
    assert isinstance(user["age"],int)
    if user["age"] >= 18:
        assert len(user["name"]) > 0
    else:
        assert user["age"] > 0

        
def test_if_practic_two():
    products = [
    {"name": "phone", "price": 700},
    {"name": "book", "price": 300},
    {"name": "pen", "price": 50}
]
    for product in products:
        assert "name" in product
        assert isinstance(product["name"],str)
        assert "price" in product
        assert isinstance(product["price"],int)
        if  product["price"] > 500:
            assert len(product["name"]) > 0
        else:
            assert product["price"] > 0

def test_ifelse_practic_two():
    products = [
    {"name": "phone", "price": 700},
    {"name": "book", "price": 300},
    {"name": "pen", "price": 50}
]
    for product in products:
        assert "name" in product
        assert isinstance(product["name"],str)
        assert "price" in product
        assert isinstance(product["price"],int)
        if  product["price"] > 500:
            assert len(product["name"]) > 0
        elif product["price"] > 100:
            assert  product["price"] < 500
        else:
            assert product["price"] > 0


def test_ifelse2_practic_two():
    products = [
    {"name": "phone", "price": 700},
    {"name": "book", "price": 300},
    {"name": "pen", "price": 50}
]
    for product in products:
        assert "name" in product
        assert isinstance(product["name"],str)
        assert "price" in product
        assert isinstance(product["price"],int)
        if  product["price"] > 500:
            assert len(product["name"]) > 0
        elif product["price"] > 200:
            assert  product["price"] < 900
        else:
            assert product["price"] > 0

def test_user_age():
    user={
          "name":"inessa",
          "age":20
          }
    assert "name" in user
    assert isinstance(user["name"],str)
    assert len(user["name"]) > 0
    
    assert "age" in user
    assert isinstance(user["age"], int)
    assert user["age"] > 0

def check_name(name):
    assert isinstance(name, str)
    assert len(name) > 0


def check_product(name, price):
    assert isinstance(name, str)
    assert len(name) > 0

    assert isinstance(price, int)
    assert price > 0

products = [
    {"name": "phone", "price": 700},
    {"name": "book", "price": 300},
    {"name": "pen", "price": 50}
]
for product in products:
 check_product(product["name"], product["price"])
    
check_product("phone", 700)
check_product("book", 300)


def check_name(name):
    assert isinstance(name, str)
    assert len(name) > 0
users = [
    {"name": "Inessa"},
    {"name": "Ivan"},
    {"name": "Masha"}
]
for user in users:
    assert "name" in user
    check_name(user["name"])

def is_even(number):
 if  number% 2 == 0:
    return True
 else:
    return False
 
print(is_even(4))
print(is_even(7))

def is_adult(age):
 if age >= 18 :
    return True
 else:
    return False
 
def check_temperature(temperature):
    if temperature <= 10:
        print("cold")
    elif  temperature <= 24:
        print("warm")
    else:
        print("hot")

def check_score(score):
    if score < 50:
        return "bad"
    elif score <= 79:
        return "good"
    else:
        return"excellent" 
        
def is_password_length(password):
 if len(password) < 8 :
    return "short"
 else:
    return "ok"

def is_password_length(password):
 if len(password) < 8 :
    return "short"
 elif not any(char.isdigit() for char in password): #если в пароле нет ни одной цифры
    return "weak"
 else:
    return "ok"
 
 def check_balance(balance):
     if balance < 0:
         return "negative"
     elif balance == 0:
         return "zero"
     else:
         return "positive"
    
def check_age(age):
     if age < 14:
         return "child"
     elif age <= 17:
         return "teen"
     else:
         return "adult"
     
    
def check_price(price):
     if price < 100:
         return "cheap"
     elif price <= 500:
         return "normal"
     else:
         return "expensive"
     
def check_login(login):
     if len(login) == 0:
         return "empty"
     elif len(login) < 5:
         return "short"
     else:
         return "ok"
     
def check_age(age):
    if age < 18:
        return "child"
    else:
        return "adult"
result = check_age(20)
print(result)
result = check_age(15)
print(result)

def check_price(price):
    if price < 100:
        return "cheap"
    elif price <= 500:
        return "normal"
    else:
        return "expensive"
result = check_price(650)
print(result)
result = check_price(300)
print(result)
result = check_price(50)
print(result)
result = check_price(100)
print(result)
result = check_price(500)
print(result)

def check_name(name):
    print(name[-1])
check_name("Python")

def check_scare(score):
    if score < 50: 
        return "fail" 
    elif score <= 80: 
        return "good" 
    else: 
        return"excellent" 

def test_check_score():
    assert check_scare(49) == "fail"
    assert check_scare(50) == "good"
    assert check_scare(80) == "good"
    assert check_scare(81) == "excellent"

scores = [49,50,80,81] 
for score in scores:
    print(check_scare(score))

def check_price(price):
    assert isinstance(price,int)
    assert price > 0
    return "valid"