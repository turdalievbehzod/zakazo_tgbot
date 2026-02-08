from aiogram import Router, F
from aiogram.types import Message
from core.config import DEVELOPER_ID

router = Router()


@router.message(F.from_user.id == DEVELOPER_ID)
async def admin_panel(message: Message):
    await message.answer("Admin panel opened 👑")
