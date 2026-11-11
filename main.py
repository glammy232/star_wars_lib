import tkinter as tk
from tkinter import ttk
from api_client import SWAPI
from models import Person, Planet, Film, Starship, Species
from translations import (
    translate,
    translate_color,
    translate_gender,
    translate_birth_year,
    translate_measure,
    translate_climate,
    translate_terrain,
)

RESOURCE_MODELS = {
    "people": (Person, ["Имя", "Год рождения", "Пол"]),
    "planets": (Planet, ["Название", "Климат", "Население"]),
    "films": (Film, ["Название", "Эпизод", "Режиссёр"]),
    "starships": (Starship, ["Название", "Модель", "Класс"]),
    "species": (Species, ["Название", "Классификация", "Язык"]),
}

TAB_TITLES = {
    "people": "Персонажи",
    "planets": "Планеты",
    "films": "Фильмы",
    "starships": "Корабли",
    "species": "Виды",
}


class StarWarsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Star Wars Библиотека — расширенная версия")
        self.root.geometry("1000x720")
        self.api = SWAPI()

        # --- Стилизация ---
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", rowheight=32, font=("Helvetica", 10))
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), padding=(8, 6))
        style.configure("TNotebook.Tab", padding=(12, 6))

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, expand=True, fill="both", padx=10)

        self.tabs = {}
        for resource, (model_class, columns) in RESOURCE_MODELS.items():
            self.create_tab(resource, model_class, columns)

    # ---------- Построение вкладки ----------

    def create_tab(self, resource, model_class, columns):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=TAB_TITLES[resource])
        self.tabs[resource] = {
            "frame": frame,
            "model": model_class,
            "columns": columns,
            "items": [],
        }

        # --- Панель поиска ---
        search_frame = tk.Frame(frame)
        search_frame.pack(pady=8, fill="x", padx=8)

        tk.Label(search_frame, text="Поиск:").pack(side="left")
        entry = tk.Entry(search_frame)
        entry.pack(side="left", padx=5, expand=True, fill="x")
        entry.bind("<Return>", lambda e: self.do_search(resource))
        tk.Button(search_frame, text="Найти", command=lambda: self.do_search(resource)).pack(side="left")
        tk.Button(search_frame, text="Показать все", command=lambda: self.load_all(resource)).pack(side="left", padx=5)

        self.tabs[resource]["entry"] = entry

        # --- Прогресс-бар (скрыт по умолчанию) ---
        progress = ttk.Progressbar(frame, mode="determinate")
        progress.pack(fill="x", padx=8, pady=(0, 4))
        progress.pack_forget()
        self.tabs[resource]["progress"] = progress

        # --- Основная область: слева список, справа детали ---
        paned = tk.PanedWindow(frame, orient="horizontal")
        paned.pack(fill="both", expand=True, padx=8, pady=8)

        # Левая часть — Treeview
        left = tk.Frame(paned)
        paned.add(left, width=480)

        tree_columns = tuple(columns)
        tree = ttk.Treeview(left, columns=tree_columns, show="headings", selectmode="browse")
        for col in tree_columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(fill="both", expand=True)
        tree.bind("<<TreeviewSelect>>", lambda e: self.show_details(resource))
        self.tabs[resource]["tree"] = tree

        # Правая часть — Text для деталей
        right = tk.Frame(paned)
        paned.add(right, width=480)

        scroll = tk.Scrollbar(right)
        scroll.pack(side="right", fill="y")
        text = tk.Text(
            right,
            wrap="word",
            yscrollcommand=scroll.set,
            state="disabled",
            bg="#f7f7f7",
            font=("Helvetica", 10),
            padx=10,
            pady=10,
            spacing1=2,
            spacing3=4,
        )
        text.pack(fill="both", expand=True)
        scroll.config(command=text.yview)

        # Теги для разных типов текста
        text.tag_configure("header", font=("Helvetica", 13, "bold"), spacing3=8)
        text.tag_configure("section", font=("Helvetica", 10, "bold"), spacing1=8, spacing3=2)

        self.tabs[resource]["details"] = text

    # ---------- Поиск и загрузка ----------

    def do_search(self, resource):
        entry = self.tabs[resource]["entry"]
        query = entry.get().strip()
        if not query:
            return
        results = self.api.search(resource, query)
        self.populate_tree(resource, results)
        self.update_tab_title(resource, len(results))

    def load_all(self, resource):
        """Загружает все страницы с прогресс-баром."""
        progress = self.tabs[resource]["progress"]
        progress.pack(fill="x", padx=8, pady=(0, 4))
        progress["value"] = 0
        self.root.update_idletasks()

        results = []
        url = f"{resource}/"
        first = self.api._get(url)
        if not first:
            progress.pack_forget()
            return

        total_count = first.get("count", 0)
        per_page = len(first.get("results", [])) or 10
        total_pages = max(1, (total_count + per_page - 1) // per_page)
        progress["maximum"] = total_pages

        results.extend(first.get("results", []))
        progress["value"] = 1
        self.root.update_idletasks()

        next_url = first.get("next")
        page_num = 1
        while next_url:
            data = self.api._get(next_url)
            if not data:
                break
            results.extend(data.get("results", []))
            next_url = data.get("next")
            page_num += 1
            progress["value"] = page_num
            self.root.update_idletasks()

        progress.pack_forget()
        self.populate_tree(resource, results)
        self.update_tab_title(resource, len(results))

    def populate_tree(self, resource, raw_results):
        tree = self.tabs[resource]["tree"]
        tree.delete(*tree.get_children())
        model_class = self.tabs[resource]["model"]

        items = [model_class(r) for r in raw_results]
        self.tabs[resource]["items"] = items

        for idx, item in enumerate(items):
            tree.insert("", "end", iid=str(idx), values=self.get_row_values(resource, item))

    def get_row_values(self, resource, item):
        if resource == "people":
            return (translate(item.name, "people"), translate_birth_year(item.birth_year), translate_gender(item.gender))
        if resource == "planets":
            return (translate(item.name, "planets"), item.climate, item.population)
        if resource == "films":
            return (translate(item.title, "films"), item.episode_id, item.director)
        if resource == "starships":
            return (translate(item.name, "starships"), item.model, item.starship_class)
        if resource == "species":
            return (translate(item.name, "species"), item.classification, item.language)
        return ()

    def update_tab_title(self, resource, count):
        frame = self.tabs[resource]["frame"]
        self.notebook.tab(frame, text=f"{TAB_TITLES[resource]} ({count})")

    # ---------- Показ деталей ----------

    def show_details(self, resource):
        tree = self.tabs[resource]["tree"]
        selection = tree.selection()
        if not selection:
            return
        idx = int(selection[0])
        items = self.tabs[resource]["items"]
        if idx >= len(items):
            return
        item = items[idx]

        text = self.tabs[resource]["details"]
        text.config(state="normal")
        text.delete("1.0", tk.END)

        self.render_details(resource, item, text)

        text.config(state="disabled")

    def insert_link(self, text_widget, display_name, target_resource, search_query):
        """Вставляет кликабельную ссылку в Text."""
        tag_name = f"link_{target_resource}_{abs(hash(search_query))}_{id(display_name)}"
        text_widget.tag_configure(tag_name, foreground="#0645AD", underline=True)
        text_widget.insert(tk.END, display_name, (tag_name,))
        text_widget.tag_bind(
            tag_name,
            "<Button-1>",
            lambda e, r=target_resource, q=search_query: self.navigate_to(r, q),
        )
        text_widget.tag_bind(
            tag_name,
            "<Enter>",
            lambda e, w=text_widget: w.config(cursor="hand2"),
        )
        text_widget.tag_bind(
            tag_name,
            "<Leave>",
            lambda e, w=text_widget: w.config(cursor=""),
        )

    def insert_link_list(self, text_widget, urls, target_resource, empty="—"):
        """Вставляет список кликабельных ссылок (перевод для показа, оригинал для поиска)."""
        if not urls:
            text_widget.insert(tk.END, empty)
            return
        for i, url in enumerate(urls):
            name = self.api.resolve_name(url)          # оригинал для поиска
            display = translate(name, target_resource) # перевод для отображения
            self.insert_link(text_widget, display, target_resource, name)
            if i < len(urls) - 1:
                text_widget.insert(tk.END, ", ")

    def navigate_to(self, resource, query):
        frame = self.tabs[resource]["frame"]
        self.notebook.select(frame)
        entry = self.tabs[resource]["entry"]
        entry.delete(0, tk.END)
        entry.insert(0, query)
        self.root.after(50, lambda: self.do_search(resource))

    def render_details(self, resource, item, text):
        if resource == "people":
            text.insert(tk.END, f"👤 {translate(item.name, 'people')}\n", "header")
            text.insert(tk.END, f"Рост: {translate_measure(item.height, 'см')}\n")
            text.insert(tk.END, f"Масса: {translate_measure(item.mass, 'кг')}\n")
            text.insert(tk.END, f"Цвет волос: {translate_color(item.hair_color)}\n")
            text.insert(tk.END, f"Цвет кожи: {translate_color(item.skin_color)}\n")
            text.insert(tk.END, f"Цвет глаз: {translate_color(item.eye_color)}\n")
            text.insert(tk.END, f"Год рождения: {translate_birth_year(item.birth_year)}\n")
            text.insert(tk.END, f"Пол: {translate_gender(item.gender)}\n") 

            text.insert(tk.END, "\n🏠 Родная планета\n", "section")
            if item.homeworld_url:
                name = self.api.resolve_name(item.homeworld_url)
                self.insert_link(text, translate(name, "planets"), "planets", name)
            else:
                text.insert(tk.END, "—")

            text.insert(tk.END, "\n\n👽 Виды\n", "section")
            self.insert_link_list(text, item.species_urls, "species")

            text.insert(tk.END, "\n\n🎬 Фильмы\n", "section")
            self.insert_link_list(text, item.film_urls, "films")

            text.insert(tk.END, "\n\n🚀 Корабли\n", "section")
            self.insert_link_list(text, item.starship_urls, "starships")

        elif resource == "planets":
            text.insert(tk.END, f"🪐 {translate(item.name, 'planets')}\n", "header")
            text.insert(tk.END, f"Диаметр: {translate_measure(item.diameter, 'км')}\n")
            text.insert(tk.END, f"Период вращения: {translate_measure(item.rotation_period, 'ч')}\n")
            text.insert(tk.END, f"Период обращения: {translate_measure(item.orbital_period, 'дн')}\n")
            text.insert(tk.END, f"Гравитация: {item.gravity}\n")
            text.insert(tk.END, f"Население: {translate_measure(item.population, 'чел.')}\n")
            text.insert(tk.END, f"Климат: {translate_climate(item.climate)}\n")
            text.insert(tk.END, f"Местность: {translate_terrain(item.terrain)}\n")
            text.insert(tk.END, f"Поверхностная вода: {translate_measure(item.surface_water, '%')}\n")
            
            text.insert(tk.END, "\n👥 Жители\n", "section")
            self.insert_link_list(text, item.resident_urls, "people")

            text.insert(tk.END, "\n\n🎬 Фильмы\n", "section")
            self.insert_link_list(text, item.film_urls, "films")

        elif resource == "films":
            text.insert(tk.END, f"🎬 {translate(item.title, 'films')}\n", "header")
            text.insert(tk.END, f"Эпизод: {item.episode_id}\n")
            text.insert(tk.END, f"Режиссёр: {item.director}\n")
            text.insert(tk.END, f"Продюсер: {item.producer}\n")
            text.insert(tk.END, f"Дата выхода: {item.release_date}\n")

            text.insert(tk.END, "\n👥 Персонажи\n", "section")
            self.insert_link_list(text, item.character_urls, "people")

            text.insert(tk.END, "\n\n🪐 Планеты\n", "section")
            self.insert_link_list(text, item.planet_urls, "planets")

            text.insert(tk.END, "\n\n🚀 Корабли\n", "section")
            self.insert_link_list(text, item.starship_urls, "starships")

            text.insert(tk.END, "\n\n👽 Виды\n", "section")
            self.insert_link_list(text, item.species_urls, "species")

            text.insert(tk.END, "\n\n📖 Вступительный текст\n", "section")
            text.insert(tk.END, item.opening_crawl)

        elif resource == "starships":
            text.insert(tk.END, f"🚀 {translate(item.name, 'starships')}\n", "header")
            text.insert(tk.END, f"Модель: {item.model}\n")
            text.insert(tk.END, f"Производитель: {item.manufacturer}\n")
            text.insert(tk.END, f"Стоимость: {item.cost_in_credits} кредитов\n")
            text.insert(tk.END, f"Длина: {item.length} м\n")
            text.insert(tk.END, f"Макс. скорость: {item.max_atmosphering_speed}\n")
            text.insert(tk.END, f"Экипаж: {item.crew}\n")
            text.insert(tk.END, f"Пассажиры: {item.passengers}\n")
            text.insert(tk.END, f"Грузоподъёмность: {item.cargo_capacity}\n")
            text.insert(tk.END, f"Гипердрайв: {item.hyperdrive_rating}\n")
            text.insert(tk.END, f"Класс: {item.starship_class}\n")

            text.insert(tk.END, "\n👤 Пилоты\n", "section")
            self.insert_link_list(text, item.pilot_urls, "people")

            text.insert(tk.END, "\n\n🎬 Фильмы\n", "section")
            self.insert_link_list(text, item.film_urls, "films")

        elif resource == "species":
            text.insert(tk.END, f"👽 {translate(item.name, 'species')}\n", "header")
            text.insert(tk.END, f"Классификация: {item.classification}\n")
            text.insert(tk.END, f"Обозначение: {item.designation}\n")
            text.insert(tk.END, f"Средний рост: {item.average_height} см\n")
            text.insert(tk.END, f"Средняя жизнь: {item.average_lifespan} лет\n")
            text.insert(tk.END, f"Язык: {item.language}\n")

            text.insert(tk.END, "\n🏠 Родная планета\n", "section")
            if item.homeworld_url:
                name = self.api.resolve_name(item.homeworld_url)
                self.insert_link(text, translate(name, "planets"), "planets", name)
            else:
                text.insert(tk.END, "—")

            text.insert(tk.END, "\n\n👥 Представители\n", "section")
            self.insert_link_list(text, item.people_urls, "people")

            text.insert(tk.END, "\n\n🎬 Фильмы\n", "section")
            self.insert_link_list(text, item.film_urls, "films")


if __name__ == "__main__":
    root = tk.Tk()
    app = StarWarsApp(root)
    root.mainloop()
