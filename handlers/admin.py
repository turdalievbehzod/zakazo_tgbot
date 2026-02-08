from aiogram import Router, F
from aiogram.types import Message

from core.config import DEVELOPER_ID
from services.products import get_all_products, add_product
from services.menu_products import add_product_to_menu

router = Router()


def is_admin(message: Message) -> bool:
    return message.from_user.id == DEVELOPER_ID


@router.message(F.text == "👑 Admin")
async def admin_menu(message: Message):
    if not is_admin(message):
        return

    await message.answer(
        "Admin panel:\n"
        "1️⃣ Show products\n"
        "2️⃣ Add product\n"
        "3️⃣ Add product to menu\n\n"
        "Send number:"
    )


@router.message(F.text == "1️⃣")
async def admin_show_products(message: Message):
    if not is_admin(message):
        return

    products = get_all_products()

    if not products:
        await message.answer("No products yet")
        return

    for p in products:
        await message.answer(
            f"{p['id']}. {p['title']} - {p['price']}"
        )


@router.message(F.text.startswith("add "))
async def admin_add_product(message: Message):
    """
    add Pizza 10000 tasty pizza
    """
    if not is_admin(message):
        return

    _, title, price, *desc = message.text.split()
    description = " ".join(desc)

    add_product(title, int(price), description)
    await message.answer("Product added ✅")


@router.message(F.text.startswith("menu "))
async def admin_add_to_menu(message: Message):
    """
    menu 1 50
    """
    if not is_admin(message):
        return

    _, product_id, amount = message.text.split()

    add_product_to_menu(int(product_id), int(amount))
    await message.answer("Product added to today's menu ✅")
