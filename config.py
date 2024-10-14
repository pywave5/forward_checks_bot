"""Конфиг файл"""

# токен от вашего телеграм-бота
TOKEN_API: str = "bot_token" # @BotFather

# ссылка на API
API_URL = "https://api.norbekovgroup.uz/api/v1/orders" # желательно не трогать)

# айди чата, куда должны отчеты придти
CHAT_ID_FORWARD: int = 0 # @username_to_id_bot

# здесь будут храниться чеки, файл создастся автоматически при активации бота
ORDERS_FILE = "orders.json" # файл для сохранения данных