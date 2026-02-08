from typing import List
from psycopg2.extras import DictRow

from core.db_settings import execute_query


def get_all_products() -> List[DictRow] | None:
    """
    Get all products
    """
    return execute_query(
        "SELECT * FROM products ORDER BY id",
        fetch="all"
    )


def add_product(title: str, price: int, description: str) -> None:
    """
    Add new product
    """
    execute_query(
        """
        INSERT INTO products (title, price, description)
        VALUES (%s, %s, %s)
        """,
        (title, price, description)
    )


def delete_product(product_id: int) -> None:
    """
    Delete product by id
    """
    execute_query(
        "DELETE FROM products WHERE id = %s",
        (product_id,)
    )
