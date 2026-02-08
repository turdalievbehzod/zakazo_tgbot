users = """
CREATE TABLE IF NOT EXISTS users (
    id BIGINT PRIMARY KEY,              -- telegram_id
    full_name VARCHAR(255),
    phone VARCHAR(30),
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
"""

products = """
CREATE TABLE IF NOT EXISTS products (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price BIGINT NOT NULL CHECK (price > 0),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
menu_products = """
CREATE TABLE IF NOT EXISTS menu_products (
    id BIGSERIAL PRIMARY KEY,
    date_of_menu DATE DEFAULT CURRENT_DATE,
    product_id BIGINT NOT NULL REFERENCES products(id) ON DELETE CASCADE,
    amount BIGINT NOT NULL CHECK (amount >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
durations = """
CREATE TABLE IF NOT EXISTS durations (
    id BIGSERIAL PRIMARY KEY,
    from_time TIMESTAMP NOT NULL,
    to_time TIMESTAMP NOT NULL,
    seats INT DEFAULT 20 CHECK (seats >= 0),
    status BOOLEAN DEFAULT TRUE,               -- TRUE = active
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

orders = """
CREATE TABLE IF NOT EXISTS orders (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    menu_product_id BIGINT NOT NULL REFERENCES menu_products(id),
    amount BIGINT NOT NULL CHECK (amount > 0),
    duration_id BIGINT REFERENCES durations(id),
    status BOOLEAN DEFAULT TRUE,               -- TRUE = active, FALSE = finished
    order_type BOOLEAN NOT NULL,               -- FALSE = take away, TRUE = dine in
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""
