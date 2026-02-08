from typing import List
from psycopg2.extras import DictRow

from core.db_settings import execute_query


def show_today_menu() -> List[DictRow] | None:
    return execute_query(
        """
        SELECT mp.id, p.title, p.price, mp.amount
        FROM menu_products mp
        JOIN products p ON p.id = mp.product_id
        WHERE mp.date_of_menu = CURRENT_DATE
        """,
        fetch="all"
    )


def add_product_to_menu(product_id: int, amount: int) -> None:
    execute_query(
        """
        INSERT INTO menu_products (product_id, amount)
        VALUES (%s, %s)
        """,
        (product_id, amount)
    )
