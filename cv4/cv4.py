"""
1 (1b) Vytvořte třídu Book. V konstruktoru předejte tři parametry: jméno autora, název knihy a cestu k souboru obsahující text knihy (viz volání v metodě main)
2 (1b) V konstruktoru vytvořte instanční proměnné: tři pro předané parametry a jeden pro rejstřík slov (typ slovník). Zkontrolujte, zda soubor s textem existuje (pokud ne, vyvolejte výjimku FileNotFoundError) - můžete využít funkci exists z os.path
3 (1b) Ve třídě Book vytvořte metodu create_index, která vytvoří a vrátí rejstřík slov z textu knihy.
Rejstřík bude reprezentován jako slovník: klíčem bude slovo, hodnotou bude seznam obsahující čísla řádků, na kterých se dané slovo nachází. Funkci zavolejte v konstruktoru třídy a rejstřík někam uložte.
 Jak na to: můžete použít funkci enumerate pro procházení řádků + jeho čísla. Nahraďte znaky konce vět a čárky (.!?,) prázdným znakem (předpokládejte, že jiné oddělovače v textu nebudou). Pomocí split() oddělte slova, převeďte slova na malá písmena a vraťte slovník.
4 (1b) Přepište funkci __str__, která reprezentuje třídu řetězcem ve formátu "autor - název knihy"
5 (1b) Ve třídě Library doplňte metodu find_books(), která vrátí seznam knih, které obsahují slovo předané v parametru této funkce (využijte vytvořený rejstřík knihy)
Prvkem seznamu bude dvojice (kniha, seznam řádků = prvek rejstříku). Pokud slovo v knize není, do seznamu se nic nepřidá.
"""
import os.path
import errno


class Book:
    def __init__(self, author, book_title, path):
        if not os.path.exists(path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)
        self.author = author
        self.book_title = book_title
        self.path = path
        self.words_index = {}
        self.words_index = self.create_index()

    def __str__(self):
        return f"{self.author} - {self.book_title}"

    def create_index(self):
        characters_to_remove = ".!?,"
        my_index = {}

        f = open(self.path, "r")

        for row, line in enumerate(f, start=1):
            words = line.split()
            tmp = map(lambda x: x.lower(), words)
            words_lower = list(tmp)
            for word in words_lower:
                for char in characters_to_remove:
                    word = word.replace(char, "")
                if word not in my_index:
                    my_index[word] = [row]
                elif row not in my_index[word]:
                    my_index[word].append(row)

        return my_index



class Library:
    def __init__(self):
        self.library = []

    def add_book(self, book):
        self.library.append(book)
   
    def find_books(self, word):
        return [(book, book.words_index[word]) for book in self.library if word in book.words_index]





if __name__ == "__main__":
    lib = Library()
    book1 = Book("Ernest Hemingway", "The Old Man and the Sea", "texts/text1.txt")
    book2 = Book("Amanda M. Douglas", "A Little Girl in Old Chicago", "texts/text2.txt")
    lib.add_book(book1)
    lib.add_book(book2)
    
    for word in ["the", "september", "that"]:
        books = lib.find_books(word)
        print(f"Word '{word}' found in:")
        for b in books:
            print(f"{b[0]} (lines: {b[1]})")

    # test error raise
   # book3 = Book("Amanda M. Douglas", "A Little Girl in Ostrava", "texts/text3.txt")

""" Ocekavany vystup
Word 'python' found in:
Word 'september' found in:
Amanda M. Douglas - A Little Girl in Old Chicago (lines: [4])
Word 'that' found in:
Ernest Hemingway - The Old Man and the Sea (lines: [3, 6])
Amanda M. Douglas - A Little Girl in Old Chicago (lines: [1, 3, 4, 7])
"""
