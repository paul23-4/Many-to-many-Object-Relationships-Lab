from list import Author, Book, Contract

def test_author_initialization():
    author = Author("John Doe")
    assert author.name == "John Doe"

def test_book_initialization():
    book = Book("Python Programming")
    assert book.title == "Python Programming"

def test_contract_initialization():
    author = Author("Jane Smith")
    book = Book("Data Science Essentials")
    contract = Contract(author, book, "2024-03-14", 10)
    assert contract.author == author
    assert contract.book == book
    assert contract.date == "2024-03-14"
    assert contract.royalties == 10

def test_author_contracts():
    author = Author("Alice Brown")
    book1 = Book("Book 1")
    book2 = Book("Book 2")
    contract1 = author.sign_contract(book1, "2024-01-01", 15)
    contract2 = author.sign_contract(book2, "2024-02-01", 20)
    assert author.contracts() == [contract1, contract2]

def test_author_books():
    author = Author("Bob Green")
    book1 = Book("Book 1")
    book2 = Book("Book 2")
    author.sign_contract(book1, "2024-01-01", 15)
    author.sign_contract(book2, "2024-02-01", 20)
    assert author.books() == [book1, book2]

def test_total_royalties():
    author = Author("Charlie Blue")
    book1 = Book("Book 1")
    book2 = Book("Book 2")
    author.sign_contract(book1, "2024-01-01", 15)
    author.sign_contract(book2, "2024-02-01", 20)
    assert author.total_royalties() == 35

def test_contracts_by_date():
    author = Author("David Gray")
    book1 = Book("Book 1")
    book2 = Book("Book 2")
    contract1 = author.sign_contract(book1, "2024-01-01", 15)
    contract2 = author.sign_contract(book2, "2024-01-01", 20)

    # Assuming contracts_by_date returns a list of contracts for the given date
    contracts = Contract.contracts_by_date("2024-01-01")

    # Compare the length of the contracts list to the expected number of contracts
    assert len(contracts) == 5