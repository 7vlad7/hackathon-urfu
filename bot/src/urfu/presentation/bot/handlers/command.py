from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from urfu.domain.entities.user import UserEntity
from urfu.presentation.bot.keyboards.menu import menu_keyboard

router = Router(name=__name__)


@router.message(CommandStart())
async def start_handler(message: Message, user: UserEntity) -> None:
    bot_info = await message.bot.me()

    await message.answer(
        (
            "<b>Привет, будущий студент УрФУ! 👋</b>\n\n"
            "Помнишь этот мучительный вопрос <i>«Куда поступить?»</i>. Мы - помним. "
            "Поэтому создали этого бота, чтобы помочь тебе разобраться.\n\n"
            "Здесь ты сможешь:\n"
            "✅ Узнать, на какие направления ты проходишь по баллам ЕГЭ.\n"
            "✅ Получить персональные рекомендации на основе твоих интересов.\n"
            "✅ Увидеть, как менялся проходной балл последние годы.\n"
            "✅ И главное — перестать нервничать и принять взвешенное решение!\n\n"
            "Готов сделать первый шаг к своей карьере? "
            "Нажми на кнопку «Заполнить анкету»! 🚀"
        ),
        reply_markup=menu_keyboard(
            user.is_profile_created,
            bot_info.username,
        ),
    )
