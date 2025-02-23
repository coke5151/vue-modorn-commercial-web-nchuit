from models.database import get_db_connection

def create_user(email, password_hash, name, address, birth_date):
    """ 創建用戶 """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO users (email, password_hash, name, address, birth_date ) VALUES (%s, %s, %s, %s, %s)",
            (email, password_hash, name, address, birth_date)
        )
        conn.commit()
        return {"message": "User registered successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()

def get_user_by_email(email):
    """ 透過 Email 查詢用戶 """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return user

def get_user_by_id(user_id):
    """ 透過 ID 查詢用戶 """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    return user

def update_user(user_id, name, address, birth_date):
    """ 更新用戶資料 """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "UPDATE users SET name = %s, address = %s, birth_date = %s WHERE id = %s",
            (name, address, birth_date, user_id)
        )
        conn.commit()
        return {"message": "User updated successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()

