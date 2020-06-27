import datetime


class RedditServiceDto:
    def __init__(self, title: str, author_fullname: str, author: str, created: int, ups: int, num_comments: int,
                 **kwargs):
        self.title = title
        self.author = author_fullname
        self.author_name = author
        self.created = created
        self.ups = ups
        self.num_comments = num_comments

    def to_json(self) -> dict:
        return dict(
            title=self.title,
            author=self.author,
            author_name=self.author_name,
            created=datetime.datetime.fromtimestamp(self.created),
            ups=self.ups,
            comments=self.num_comments
        )
