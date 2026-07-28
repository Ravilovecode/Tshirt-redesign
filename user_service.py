import sqlite3

class UserService:
    def __init__(self, db_path="app.db"):
        self.db_path = db_path

    def search_users(self, username_query: str):
        """
        Searches for users in the database safely using parameterized query.
        FIXED: Parameterized query eliminates SQL Injection risk.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # SECURE: Parameterized query
        query = "SELECT id, username, email, role FROM users WHERE username LIKE ?"
        print(f"Executing Secure Query for: {username_query}")
        
        cursor.execute(query, (f"%{username_query}%",))
        results = cursor.fetchall()
        conn.close()
        return results

    def get_user_by_id(self, user_id: int):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, username, email FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user
