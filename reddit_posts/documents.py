from .ext.database import db


class Post(db.Document):
    title = db.StringField()
    author = db.StringField()
    author_name = db.StringField()
    ups = db.IntField()
    comments = db.IntField()
    created = db.DateTimeField()

    def to_json(self) -> dict:
        return {'title': self.title,
                'author': self.author,
                'author_name': self.author_name,
                'created': self.created,
                'ups': self.ups,
                'comments': self.comments}


class Response(db.Document):
    code = db.StringField()
