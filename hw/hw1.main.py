import json
from pathlib import Path

# 08  Поиск профиля
# Напишите функцию find_player(player_id). Она должна вернуть словарь игрока или None. Проверьте существующий и отсутствующий id.
# Проверяемый навык: Поиск по идентификатору

FILE_PATH = Path("players.json")

def find_player(player_id):
    if not FILE_PATH.exists():
        return None
    try:
        with FILE_PATH.open("r", encoding = "utf-8") as file:
            players = json.load(file)
            for player in players:
                if player.get("id") == player_id:
                    return player
    except json.JSONDecodeError:
        return None
    return None

if __name__ == "__main__":
    print("Поиск id = 1: ", find_player(1))
    print("Поиск id = 9: ", find_player(9))

# 09  Повышение уровня
# Напишите функцию level_up(player_id), которая увеличивает level на 1, сохраняет изменения и возвращает True. Если игрок не найден, верните False.
# Проверяемый навык: Изменение записи



# 10  Архив профиля
# Напишите функцию deactivate_player(player_id), которая меняет active на False и сохраняет данные. Удалять запись не нужно.
# Проверяемый навык: Мягкое удаление
