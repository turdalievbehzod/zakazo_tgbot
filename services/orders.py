from datetime import datetime, timedelta
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from core.db_settings import execute_query
from states.states import OrderState


async def make_order_start(message: Message, state: FSMContext):
    await message.answer("Enter menu product ID:")
    await state.set_state(OrderState.menu_id)


async def order_menu_id(message: Message, state: FSMContext):
    await state.update_data(menu_id=int(message.text))
    await message.answer("Enter amount:")
    await state.set_state(OrderState.amount)


async def order_amount(message: Message, state: FSMContext):
    await state.update_data(amount=int(message.text))
    await message.answer("Choose: Take away / Dine in")
    await state.set_state(OrderState.order_type)
