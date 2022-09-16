from internal.models.models import Author, PostAuthor, Response
from internal.driver.driver import connect_DB
"""
    book_id: int
    book_title: str
    publication: str
    author_id: int
    author_first_name: str
    author_last_name: str
"""


def create_resp(b_id, b_title, b_pub, a_id, a_fname, a_lname):
    resp = Response()

    resp.book_id = b_id
    resp.author_id = a_id
    resp.author_first_name = a_fname
    resp.author_last_name = a_lname
    resp.book_title = b_title
    resp.publication = b_pub

    return resp


def create_author_resp(id, fname, lname, created_at):
    a = Author()

    a.id = id
    a.first_name = fname
    a.last_name = lname
    a.created_at = created_at

    return a


class Database:

    db = connect_DB()

    @classmethod
    def get_all_books(cls):
        cursor = cls.db.cursor()

        cursor.execute("""
        select b.id, b.title, b.author_id, b.publication, a.first_name, a.last_name
        from books b
        left join authors a on b.author_id = a.id
        """)

        rows = cursor.fetchall()

        responses = []

        for r in rows:
            resp = create_resp(r[0], r[1], r[3], r[2], r[4], r[5])
            responses.append(resp)

        cursor.close()

        return responses

    @classmethod
    def get_book(cls, id):
        cursor = cls.db.cursor()

        query = f"""
        select b.id, b.title, b.author_id, b.publication, a.first_name, a.last_name
        from books b
        left join authors a on b.author_id = a.id
        where b.id={id}
        """

        cursor.execute(query)

        row = cursor.fetchone()

        resp = create_resp(row[0], row[1], row[3], row[2], row[4], row[5])

        cursor.close()

        return resp

    @classmethod
    def get_author(cls, id):
        cursor = cls.db.cursor()

        query = f"""
        select id, first_name, last_name, created_at
        from authors
        where id={id}
        """

        cursor.execute(query)

        row = cursor.fetchone()

        author = create_author_resp(row[0], row[1], row[2], row[3])

        cursor.close()

        return author

    @classmethod
    def list_authors(cls):
        cursor = cls.db.cursor()

        query = """
        select id, first_name, last_name, created_at
        from authors
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        authors = []

        for r in rows:
            author = create_author_resp(r[0], r[1], r[2], r[3])
            authors.append(author)

        cursor.close()

        return authors

    @classmethod
    def new_author(cls, author: PostAuthor):
        cursor = cls.db.cursor()

        query = f"""
        insert into authors(first_name, last_name) 
        values('{author.first_name}', '{author.last_name}')
        """

        cursor.execute(query)

        cursor.close()

        return
