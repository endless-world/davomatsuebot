from functools import wraps
from tgbot.bot.filters.who_is import is_admin

def admin_only(func):
    @wraps(func)
    async def wrapper(message, data=None, *args, **kwargs):
        user_id = message.from_user.id
        if not is_admin(user_id):
            return  # Silently ignore or provide an appropriate message
        return await func(message, data, *args, **kwargs)
    return wrapper


def user_only(func):
    @wraps(func)
    async def wrapper(message, data=None, *args, **kwargs):
        user_id = message.from_user.id
        if is_admin(user_id):
            return  # Silently ignore or provide an appropriate message
        return await func(message, data, *args, **kwargs)
    return wrapper
