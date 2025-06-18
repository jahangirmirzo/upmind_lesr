
import requests
import json
from bs4 import BeautifulSoup
import time

# ✅ Укажите сюда токен и chat_id вашего Telegram-бота
TELEGRAM_TOKEN = "ВАШ_ТОКЕН"
TELEGRAM_CHAT_ID = "ВАШ_CHAT_ID"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def send_to_telegram(message, token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        r = requests.post(url, data=payload)
        if r.status_code != 200:
            print(f"❌ Ошибка отправки: {r.text}")
    except Exception as e:
        print(f"⚠️ Ошибка Telegram: {e}")

def get_detail_data(link):
    try:
        response = requests.get(link, headers=HEADERS)
        if response.status_code != 200:
            return {}

        soup = BeautifulSoup(response.text, "html.parser")
        details = {}

        blocks = soup.find_all("div", class_="lf-list__row")
        for block in blocks:
            key_tag = block.find("div", class_="lf-list__label")
            val_tag = block.find("div", class_="lf-list__value")
            if key_tag and val_tag:
                key = key_tag.text.strip().lower()
                val = val_tag.text.strip()
                details[key] = val

        desc_tag = soup.find("div", class_="lf-detail__description")
        if desc_tag:
            details["описание"] = desc_tag.text.strip()

        location_tag = soup.find("a", class_="lf-detail__location")
        if location_tag:
            details["город"] = location_tag.text.strip()

        return details

    except Exception as e:
        return {}

def parse_lalafo_transport(pages=1):
    base_url = "https://lalafo.kg/bishkek/transport"
    results = []

    for page in range(1, pages + 1):
        url = f"{base_url}?page={page}" if page > 1 else base_url
        print(f"🔄 Страница {page}...")
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", class_="lf-ad-tile")

        for article in articles:
            title_tag = article.find("p", class_="lf-ad-tile__title")
            price_tag = article.find("p", class_="LFSubHeading")
            image_tag = article.find("img")
            link_tag = article.find("a", href=True)

            title = title_tag.text.strip() if title_tag else ""
            price = price_tag.text.strip() if price_tag else ""
            image = image_tag["src"] if image_tag else ""
            link = "https://lalafo.kg" + link_tag["href"] if link_tag else ""

            details = get_detail_data(link)
            time.sleep(1)

            message = f"<b>{title}</b>\nЦена: {price}\n<a href='{link}'>Смотреть объявление</a>"
            send_to_telegram(message, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID)

            results.append({
                "название": title,
                "цена": price,
                "ссылка": link,
                "фото": image,
                "детали": details
            })

    with open("lalafo_transport_with_telegram.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"✅ Сохранено {len(results)} объявлений и отправлено в Telegram")

if __name__ == "__main__":
    parse_lalafo_transport(pages=2)
