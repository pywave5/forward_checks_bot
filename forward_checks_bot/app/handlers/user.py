import asyncio
from datetime import datetime

from aiogram import Router, F
from aiogram.filters.command import CommandStart
from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode

from app.functions.parser import get_new_orders
from config import CHAT_ID_FORWARD

user = Router()

def format_time(time):
    formatted_time = datetime.fromtimestamp(time / 1000)
    return formatted_time.strftime("%d-%m-%Y")

async def check_new_orders(bot):
    while True:
        new_order = get_new_orders()
        for order in new_order:
            await bot.send_message(
                chat_id=CHAT_ID_FORWARD,
                text=f"<b>Buyurtma detallari:</b>\n\n"
                     f"<b>Shartnoma raqami:</b> {order['invoiceNumber']}\n"
                     f"<b>Mijoz:</b> {order['clientName']}\n"
                     f"<b>Kurs:</b> {order.get('courseTitle', 'N/A')}\n"
                     f"<b>Miqdori:</b> {order['amount']} so'm\n"
                     f"<b>Holat:</b> {order['status']}\n"
                     f"<b>Yaratilgan sana:</b> {format_time(order['create_time'])}\n"
                     f"<b>Hizmat:</b> {order.get('paymentType', 'N/A')}\n"
                     f"<b>Mijoz telefoni:</b> {order['clientPhone']}\n"
                     f"<b>Mijoz manzili:</b> {order.get('clientAddress', 'N/A')}\n"
                     f"<b>Telegram foydalanuvchi nomi:</b> {order.get('tgUsername', 'N/A')}\n"
                     f"<b>Pasport:</b> {order.get('passport', 'N/A')}",
                parse_mode=ParseMode.HTML
            )
@user.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(f"Привет. это бот для получения чеков об оплате за услуги.")

    asyncio.create_task(check_new_orders(message.bot))

