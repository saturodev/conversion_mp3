from .callbacks import user_callback
from .commands import user_command
from .messages import user_message


def setup_routers(dp):
    dp.include_router(user_callback.router)
    dp.include_router(user_command.router)
    dp.include_router(user_message.router)
