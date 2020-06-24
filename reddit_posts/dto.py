import datetime


class RedditServiceDto:
    def __init__(self, title, author_fullname, author, created, ups, num_comments, **kwargs):
        self.title = title
        self.author_id = author_fullname
        self.author = author
        self.created = created
        self.ups = ups
        self.num_comments = num_comments

    def __repr__(self):
        return f'({self.author_id}, {self.title}, ups={self.ups}, comments={self.num_comments})'


