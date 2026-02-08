from aiogram import Router, F
from aiogram.types import Message

from services.menu_products import show_today_menu
from services.orders import make_order_start
from states.states import OrderState

router = Router()


@router.message(F.text == "📋 Menu")
async def menu(message: Message):
    menu = show_today_menu()

    if not menu:
        await message.answer("😔 Menu is empty for today ")
        return

    for m in menu:
        await message.answer(
            f"{m['id']}. {m['title']} - {m['price']} ({m['amount']})"
        )


@router.message(F.text == "🛒 Order")
async def order(message: Message, state):
    await message.answer("Send menu product ID:")
    await state.set_state(OrderState.menu_id)
