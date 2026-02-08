from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    full_name = State()
    phone = State()

class OrderState(StatesGroup):
    menu_id = State()
    amount = State()
    order_type = State()
