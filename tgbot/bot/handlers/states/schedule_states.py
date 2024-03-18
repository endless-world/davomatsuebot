from aiogram.dispatcher.filters.state import State, StatesGroup


class ScheduleState(StatesGroup):
    day = State()
