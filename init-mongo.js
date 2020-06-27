db.createUser(
    {
        user: "winnin",
        pwd: "winnin",
        roles:
            [
                {
                    role: "readWrite",
                    db: "reddit_posts"
                },
                {
                    role: "readWrite",
                    db: "reddit_posts_test"
                }
            ]
    }
)