import sqlite3

def init_db():
    conn = sqlite3.connect('wallets.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users_wallets (
            id INTEGER PRIMARY KEY,
            user_id TEXT NOT NULL UNIQUE,
            wallet_address TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

def add_user_wallet(user_id, wallet_address):
    conn = sqlite3.connect('wallets.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO users_wallets (user_id, wallet_address) VALUES (?, ?)', (user_id, wallet_address))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

    return True

def user_wallet_exists(user_id=None, wallet_address=None):
    conn = sqlite3.connect('wallets.db')
    cursor = conn.cursor()

    # Проверка наличия user_id
    if user_id:
        cursor.execute('''
            SELECT * FROM users_wallets WHERE user_id=?
        ''', (user_id,))
        if cursor.fetchone():
            conn.close()
            return True

    # Проверка наличия wallet_address
    if wallet_address:
        cursor.execute('''
            SELECT * FROM users_wallets WHERE wallet_address=?
        ''', (wallet_address,))
        if cursor.fetchone():
            conn.close()
            return True

    conn.close()
    return False


def get_next_id():
    conn = sqlite3.connect('wallets.db')
    cursor = conn.cursor()

    # Найти наименьший неиспользуемый идентификатор
    cursor.execute('''
        SELECT MIN(id) FROM users_wallets
        WHERE id NOT IN (SELECT id FROM users_wallets)
    ''')
    next_id = cursor.fetchone()[0]

    if next_id is None:
        # Если нет пустых идентификаторов, используйте максимальный + 1
        cursor.execute('SELECT MAX(id) FROM users_wallets')
        max_id = cursor.fetchone()[0]
        next_id = (max_id or 0) + 1

    conn.close()
    return next_id

