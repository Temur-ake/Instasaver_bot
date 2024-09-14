from aiogram import Router

from My_bot.downloads.handlers import router

begin_router = Router()

begin_router.include_router(
    router,
)
