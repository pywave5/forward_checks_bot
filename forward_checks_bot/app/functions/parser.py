import os
import json
import requests

from config import API_URL, ORDERS_FILE

def load_saved_orders() -> dict:
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, 'r') as file:
            return json.load(file)
    return {'data': []}

def save_orders(orders: list) -> None:
    with open(ORDERS_FILE, 'w') as file:
        json.dump({'data': orders}, file, indent=4)

def get_new_orders() -> list:
    url = API_URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        saved_orders = load_saved_orders()
        saved_ids = {order['_id'] for order in saved_orders.get('data', [])}
        new_orders = []

        if data and 'data' in data:
            for order in data['data']:
                if order['status'] == 'ОПЛАЧЕНО' and order['_id'] not in saved_ids:
                    new_orders.append(order)
                    # print(f"Найден новый оплаченный заказ: {order['_id']}")

            if new_orders:
                all_orders = saved_orders['data'] + new_orders
                save_orders(all_orders)

        return new_orders

    except requests.exceptions.HTTPError as http_err:
        print(f"Ошибка получения данных - {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Ошибка: {err}")