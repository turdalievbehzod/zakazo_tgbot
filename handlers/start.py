from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext

from core.config import DEVELOPER_ID
from core.db_settings import execute_query
from states import RegisterState

router = Router()


@router.message(F.text == "/start")
async def start(message: Message, state: FSMContext):
    user = execute_query(
        "SELECT * FROM users WHERE id=%s",
        (message.from_user.id,),
        fetch="one"
    )

    if user:
        await message.answer(f"Welcome back, {user['full_name']} 👋")
        return

    await message.answer("Welcome! Please enter your full name:")
    await state.set_state(RegisterState.full_name)


@router.message(RegisterState.full_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)

    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Share phone", request_contact=True)]],
        resize_keyboard=True
    )

    await message.answer("Please share your phone number", reply_markup=kb)
    await state.set_state(RegisterState.phone)


@router.message(RegisterState.phone, F.contact)
async def get_phone(message: Message, state: FSMContext):
    data = await state.get_data()

    execute_query(
        """
        INSERT INTO users (id, full_name, phone, is_admin)
        VALUES (%s, %s, %s, %s)
        """,
        (
            message.from_user.id,
            data["full_name"],
            message.contact.phone_number,
            message.from_user.id == DEVELOPER_ID
        )
    )

    await message.answer("Registration completed ✅", reply_markup=None)
    await state.clear()
