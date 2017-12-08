LIBRARY_DATA = """
TITLE: Hitchhiker's Guide to the Galaxy
AUTHOR: Douglas Adams
DESCRIPTION: Seconds before the Earth is demolished to make way for a galactic freeway,
Arthur Dent is plucked off the planet by his friend Ford Prefect, a researcher for the
revised edition of The Hitchhiker's Guide to the Galaxy who, for the last fifteen years,
has been posing as an out-of-work actor.

TITLE: Dune
AUTHOR: Frank Herbert
DESCRIPTION: The troubles begin when stewardship of Arrakis is transferred by the
Emperor from the Harkonnen Noble House to House Atreides. The Harkonnens don't want to
give up their privilege, though, and through sabotage and treachery they cast young
Duke Paul Atreides out into the planet's harsh environment to die. There he falls in
with the Fremen, a tribe of desert dwellers who become the basis of the army with which
he will reclaim what's rightfully his. Paul Atreides, though, is far more than just a
usurped duke. He might be the end product of a very long-term genetic experiment
designed to breed a super human; he might be a messiah. His struggle is at the center
of a nexus of powerful people and events, and the repercussions will be felt throughout
the Imperium.

TITLE: A Song Of Ice And Fire Series
AUTHOR: George R.R. Martin
DESCRIPTION: As the Seven Kingdoms face a generation-long winter, the noble Stark family
confronts the poisonous plots of the rival Lannisters, the emergence of the
White Walkers, the arrival of barbarian hordes, and other threats.

"""
class Book(object):
    def __init__(self):
        self.book_id = None
        self.title = None
        self.author = None
        self.words = set()

class Library(object):
    def __init__(self, data):
        self.book_id = 0
        self.books = []
        for line in LIBRARY_DATA.split('\n'):

            if len(line) == 0:
                continue

            if line.startswith('TITLE'):
                book = Book()
                book.book_id = self.book_id
                self.books.append(book)
                self.book_id +=1

                book_name = line.split(':')[1].strip()
                words_in_book_name = book_name.split()
                book.title = book_name
                book.words.update(words_in_book_name)
                continue

            if line.startswith('AUTHOR'):
                author_name = line.split(':')[1].strip()
                words_in_author_name = author_name.split()
                book.author = author_name
                book.words.update(words_in_author_name)
                continue

            elif line.startswith('DESCRIPTION'):

                words_in_description = line.split(':')[1]
                words_in_description = words_in_description.replace(',', '')
                words_in_description = words_in_description.replace('.', '')
                words_in_description = words_in_description.split()

                book.words.update(words_in_description)
                continue

            else:
                words_in_description = line.split()
                book.words.update(words_in_description)

        for book in self.books:
            print book.title
            print book.author

    def search(self, word):
        output_dict = []
        for book in self.books:
            if word in book.words:
                output_dict.append(book)
        return output_dict

library = Library(LIBRARY_DATA)

first_results = library.search("Arrakis")
assert first_results[0].title == "Dune"
second_results = library.search("winter")
assert second_results[0].title == "A Song Of Ice And Fire Series"
third_results = library.search("demolished")
assert third_results[0].title == "Hitchhiker's Guide to the Galaxy"
fourth_results = library.search("the")
assert len(fourth_results) == 3
assert fourth_results[0].title == "Hitchhiker's Guide to the Galaxy"
assert fourth_results[1].title == "Dune"
assert fourth_results[2].title == "A Song Of Ice And Fire Series"
