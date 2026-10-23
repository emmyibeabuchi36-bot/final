from database import get_connection

def authenticate(username, password):
    conn = get_connection()
    row = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    ).fetchone()
    conn.close()
    return row is not None
