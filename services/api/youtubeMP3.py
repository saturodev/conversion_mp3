import requests
import re
import config

YOUTUBE_REGEX = re.compile(
    r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
)


def get_url(url):
    match = YOUTUBE_REGEX.search(url)
    video_id = match.group(1)
    url = config.RAPID_URL
    querystring = {"id": video_id}
    headers = {
        "x-rapidapi-key": config.RAPID_KEY,
        "x-rapidapi-host": config.RAPID_HOST,
    }
    response = requests.get(url, headers=headers, params=querystring)
    result = response.json()
    get_link = result["link"]
    return get_link, video_id


def get_youtube(url):
    match = YOUTUBE_REGEX.search(url)
    video_id = match.group(1)
    url = f"{config.YOUTUBE_URL}?part=snippet&id={video_id}&key={config.YOUTUBE_KEY}"
    response = requests.get(url)
    data = response.json()
    snippet = data["items"][0]["snippet"]
    title = snippet["title"]
    thumbnail = snippet["thumbnails"]["maxres"]["url"]
    return thumbnail, title


def is_music(url):
    match = YOUTUBE_REGEX.search(url)
    try:
        video_id = match.group(1)
        url = (
            f"{config.YOUTUBE_URL}?part=snippet&id={video_id}&key={config.YOUTUBE_KEY}"
        )
        response = requests.get(url).json()
        items = response.get("items", [])
        if not items:
            return "❌ Видео не найдено. Возможно, ID неверный."

        status = items[0].get("status", {})
        if status.get("uploadStatus") == "deleted":
            return "🚫 Это видео было удалено с YouTube."

        # проверяем категорию
        category_id = items[0]["snippet"]["categoryId"]
        if category_id == "10":
            return True  # это музыка
        else:
            return "❌ Это видео не относится к категории 'Музыка'."
    except AttributeError:
        result = "⚠️ Не удалось найти YouTube ID. Отправь правильную ссылку."
        return result


if __name__ == "__main__":
    pass
