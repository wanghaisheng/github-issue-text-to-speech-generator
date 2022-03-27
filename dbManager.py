import sqlite3

class DBManager():

    conn = None

    def __init__(self):
        self.conn = sqlite3.connect("redditGenerator.db")

    def cleanTables(self):
        cursor = self.conn.cursor()
        cursor.execute("""DELETE FROM posts""")
        cursor.execute("""DELETE FROM comments""")
        self.conn.commit()

    def insertPost(self, post):
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO posts ('id', 'title') VALUES (?, ?)""", (post.id, post.title))
        self.conn.commit()

    def insertComment(self, comment, post_id):
        cursor = self.conn.cursor()
        cursor.execute("""INSERT INTO comments ('id', 'post_id', 'comment_text') VALUES (?, ?, ?)""", (comment.id, post_id, comment.body))
        self.conn.commit()

    def getPostWithId(self, post_id):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT * FROM posts WHERE id = (?)""", (post_id,))
        return cursor.fetchone()

DBManager().cleanTables()