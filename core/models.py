users = """
CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY,              -- telegram_id
    full_name VARCHAR(255),
    phone VARCHAR(30),
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""
