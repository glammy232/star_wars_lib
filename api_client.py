import requests

class SWAPI:
    BASE_URL = "https://swapi.dev/api"

    def __init__(self):
        self.session = requests.Session()
        self._cache = {}

    def _get(self, url, params=None):
        if not url.startswith("http"):
            url = f"{self.BASE_URL}/{url}"
        
        cache_key = (url, tuple(sorted(params.items())) if params else None)
        if cache_key in self._cache:
            return self._cache[cache_key]

        try:
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            self._cache[cache_key] = data
            return data
        except requests.exceptions.RequestException as e:
            print(f"Ошибка сети: {e}")
            return None

    def search(self, resource, query):
        """Универсальный поиск: resource = 'people', 'planets', 'films', 'starships', 'species'."""
        data = self._get(f"{resource}/", params={"search": query})
        return data.get("results", []) if data else []

    def get_all(self, resource):
        """Получить все записи (с пагинацией)."""
        results = []
        url = f"{resource}/"
        while url:
            data = self._get(url)
            if not data:
                break
            results.extend(data.get("results", []))
            url = data.get("next")
        return results

    def resolve_name(self, url):
        """Превращает URL ресурса в его имя/название."""
        if not url:
            return "—"
        data = self._get(url)
        if not data:
            return "Ошибка"
        # У разных ресурсов разные поля для имени
        return data.get("name") or data.get("title") or "—"

    def resolve_names(self, urls):
        """Превращает список URL в список имён."""
        if not urls:
            return []
        return [self.resolve_name(u) for u in urls]
