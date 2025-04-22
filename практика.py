from pathlib import Path
import requests
import pygame
import sys
import os
import random

def download():
    GRAPHQL_ENDPOINT = "https://graph.nordavind.ru/subgraphs/name/the-wall-polygon"
    DOWNLOAD_ENDPOINT = "https://thewall.global/api/download/"
    OWNER = "0x2c758d4cfc4da0cc3c680778b224232fa5610d33"
    X_MIN, X_MAX = 39, 61
    Y_MIN, Y_MAX = 13, 44
    SAVE_DIR = Path("C:/Users/1/PycharmProjects/puzzle/pictures_1")
    SAVE_DIR.mkdir(exist_ok=True)

    # GraphQL-запрос
    query = """
    {
      items(
        where: {
          area_: {
            x_gte: %d, 
            x_lte: %d, 
            y_gte: %d, 
            y_lte: %d
          }, 
          owner: "%s"
        },
        first: 1000
      ) {
        area {
          x
          y
          imageCID
        }
      }
    }
    """ % (X_MIN, X_MAX, Y_MIN, Y_MAX, OWNER)

    # Отправка запроса
    response = requests.post(GRAPHQL_ENDPOINT, json={'query': query})
    response.raise_for_status()
    data = response.json()["data"]["items"]

    # Сортировка: сначала по y по убыванию (сверху вниз), потом по x по возрастанию (слева направо)
    sorted_items = sorted(data, key=lambda i: (-int(i["area"]["y"]), int(i["area"]["x"])))

    # Скачивание изображений
    for idx, item in enumerate(sorted_items, start=1):
        img_url = item["area"]["imageCID"][0]
        if not img_url:
            print(f"Пропущена область без изображения: x={item['area']['x']}, y={item['area']['y']}")
            continue
        print(f"Скачиваю {img_url} -> {idx}.jpg")
        img_response = requests.get(DOWNLOAD_ENDPOINT + img_url) # Загрузка картинки: ссылка на endpoint для загрузки + CID картинки из графа
        img_response.raise_for_status()
        with open(SAVE_DIR / f"{idx}.webp", "wb") as f:
            f.write(img_response.content)

    print("Готово.")
