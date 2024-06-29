from app.connection import get_db

class Post:
    @staticmethod
    def get_all():
        try:
            conn = get_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM post")
            posts = cursor.fetchall()
            return posts
        except Exception as e:
            raise Exception(f"Error retrieving posts: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def create(created_by, content):
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO post (created_by, content) VALUES (%s, %s)", (created_by, content))
            conn.commit()
            post_id = cursor.lastrowid
            return post_id
        except Exception as e:
            conn.rollback()
            raise Exception(f"Error creating post: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_by_id(post_id):
        try:
            conn = get_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM post WHERE id = %s", (post_id,))
            post = cursor.fetchone()
            return post
        except Exception as e:
            raise Exception(f"Error retrieving post: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update(post_id, content):
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE post SET content = %s WHERE id = %s", (content, post_id))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Error updating post: {str(e)}")
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete(post_id):
        try:
            conn = get_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM post WHERE id = %s", (post_id,))
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise Exception(f"Error deleting post: {str(e)}")
        finally:
            cursor.close()
            conn.close()