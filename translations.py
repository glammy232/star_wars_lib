# -*- coding: utf-8 -*-
"""
Словари переводов для Star Wars API.
Ключи — точные английские названия из SWAPI (регистрозависимы!).
Если перевода нет — возвращается оригинал.
"""

PEOPLE_RU = {
    # --- Основные персонажи саги ---
    "Luke Skywalker": "Люк Скайуокер",
    "C-3PO": "C-3PO",
    "R2-D2": "R2-D2",
    "Darth Vader": "Дарт Вейдер",
    "Leia Organa": "Лея Органа",
    "Owen Lars": "Оуэн Ларс",
    "Beru Whitesun Lars": "Беру Уайтсан Ларс",
    "R5-D4": "R5-D4",
    "Biggs Darklighter": "Биггс Дарклайтер",
    "Obi-Wan Kenobi": "Оби-Ван Кеноби",
    "Anakin Skywalker": "Энакин Скайуокер",
    "Wilhuff Tarkin": "Уилхафф Таркин",
    "Chewbacca": "Чубакка",
    "Han Solo": "Хан Соло",
    "Greedo": "Гридо",
    "Jabba Desilijic Tiure": "Джабба Десилийк Тиуре",
    "Wedge Antilles": "Ведж Антиллес",
    "Jek Tono Porkins": "Джек Тоно Поркинс",
    "Yoda": "Йода",
    "Palpatine": "Палпатин",
    "Boba Fett": "Боба Фетт",
    "IG-88": "IG-88",
    "Bossk": "Босск",
    "Lando Calrissian": "Лэндо Калриссиан",
    "Lobot": "Лобот",
    "Ackbar": "Акбар",
    "Mon Mothma": "Мон Мотма",
    "Arvel Crynyd": "Арвел Крайнид",
    "Wicket Systri Warrick": "Уикет Систри Уоррик",
    "Nien Nunb": "Ниен Нанб",
    "Qui-Gon Jinn": "Квай-Гон Джинн",
    "Nute Gunray": "Нут Ганрей",
    "Finis Valorum": "Финис Валорум",
    "Padmé Amidala": "Падме Амидала",
    "Jar Jar Binks": "Джар Джар Бинкс",
    "Roos Tarpals": "Рус Тарпалс",
    "Rugor Nass": "Ругор Насс",
    "Ric Olié": "Рик Олие",
    "Watto": "Уотто",
    "Sebulba": "Себульба",
    "Quarsh Panaka": "Куарш Панака",
    "Shmi Skywalker": "Шми Скайуокер",
    "Darth Maul": "Дарт Мол",
    "Bib Fortuna": "Биб Фортуна",
    "Ayla Secura": "Айла Секура",
    "Ratts Tyerel": "Раттс Тайрел",
    "Dud Bolt": "Дад Болт",
    "Gasgano": "Гаскано",
    "Ben Quadinaros": "Бен Куадинарос",
    "Mace Windu": "Мейс Винду",
    "Ki-Adi-Mundi": "Ки-Ади-Мунди",
    "Kit Fisto": "Кит Фисто",
    "Eeth Koth": "Иит Кот",
    "Adi Gallia": "Ади Галлия",
    "Saesee Tiin": "Сейси Тиин",
    "Yarael Poof": "Яраэль Пуф",
    "Plo Koon": "Пло Кун",
    "Mas Amedda": "Мас Амедда",
    "Gregar Typho": "Грегар Тифо",
    "Cordé": "Корде",
    "Cliegg Lars": "Клигг Ларс",
    "Poggle the Lesser": "Поггл Меньший",
    "Luminara Unduli": "Луминара Ундули",
    "Barriss Offee": "Баррисс Оффи",
    "Dormé": "Дорме",
    "Dooku": "Дуку",
    "Bail Prestor Organa": "Бейл Престор Органа",
    "Jango Fett": "Джанго Фетт",
    "Zam Wesell": "Зэм Уэселл",
    "Dexter Jettster": "Декстер Джеттстер",
    "Lama Su": "Лама Су",
    "Taun We": "Таун Ви",
    "Jocasta Nu": "Джокаста Ню",
    "R4-P17": "R4-P17",
    "Wat Tambor": "Уот Тамбор",
    "San Hill": "Сан Хилл",
    "Shaak Ti": "Шаак Ти",
    "Grievous": "Гривус",
    "Tarfful": "Тарффул",
    "Raymus Antilles": "Реймус Антиллес",
    "Sly Moore": "Слай Мур",
    "Tion Medon": "Тион Медон",
    "Finn": "Финн",
    "Rey": "Рей",
    "Poe Dameron": "По Дэмерон",
    "BB8": "BB-8",
    "Captain Phasma": "Капитан Фазма",
    "Padmé Amidala (decoy)": "Падме Амидала (двойник)",
}

PLANETS_RU = {
    "Tatooine": "Татуин",
    "Alderaan": "Альдераан",
    "Yavin IV": "Явин IV",
    "Hoth": "Хот",
    "Dagobah": "Дагоба",
    "Bespin": "Беспин",
    "Endor": "Эндор",
    "Naboo": "Набу",
    "Coruscant": "Корусант",
    "Kamino": "Камино",
    "Geonosis": "Джеонозис",
    "Utapau": "Утапау",
    "Mustafar": "Мустафар",
    "Kashyyyk": "Кашиик",
    "Felucia": "Фелуция",
    "Mygeeto": "Майгито",
    "Saleucami": "Салукемай",
    "Polis Massa": "Полис-Масса",
    "Cato Neimoidia": "Кейто-Неймодия",
    "Corellia": "Кореллия",
    "Dathomir": "Датомир",
    "Ryloth": "Рилот",
    "Shili": "Шили",
    "Kalee": "Кали",
    "Umbara": "Умбара",
    "Malastare": "Маластар",
    "Iridonia": "Иридония",
    "Mirial": "Мирал",
    "Serenno": "Серенно",
    "Concord Dawn": "Конкорд Даун",
    "Zolan": "Золан",
    "Ojom": "Ойом",
    "Skako": "Скако",
    "Muunilinst": "Муунилист",
    "Dantooine": "Дантуин",
    "Dorin": "Дорин",
    "Eriadu": "Эриаду",
    "Chandrila": "Чандрила",
    "Cerea": "Церея",
    "Champala": "Чампала",
    "Aleen Minor": "Алин Малый",
    "Vulpter": "Вулптер",
    "Troiken": "Тройкен",
    "Tund": "Тунд",
    "Haruun Kal": "Харуун Кал",
    "Glee Anselm": "Гли Ансельм",
    "Bestine IV": "Бестин IV",
    "Bespin (Cloud City)": "Беспин (Облачный город)",
    "Scarif": "Скариф",
    "Jedha": "Джедда",
    "Eadu": "Иду",
    "Lah'mu": "Ла'му",
    "Wobani": "Вобани",
    "Ring of Kafrene": "Кольцо Кафрена",
    "Hosnian Prime": "Хосниан-Прайм",
    "Starkiller Base": "База «Старкиллер»",
    "D'Qar": "Ди'Куар",
    "Takodana": "Такодана",
    "Jakku": "Джакку",
    "Ahch-To": "Ак-То",
    "Cantonica": "Кантоника",
    "Crait": "Крэйт",
    "Kessel": "Кессель",
    "Savareen": "Саварин",
    "Vandor": "Вандор",
    "Numidian Prime": "Нумидиан-Прайм",
    "Exegol": "Экзегол",
    "Pasaana": "Пасаана",
    "Kijimi": "Киджими",
    "Kef Bir": "Кеф'Бир",
    "Ajan Kloss": "Аджан Клосс",
    "Batuu": "Батуу",
}

FILMS_RU = {
    "A New Hope": "Новая надежда",
    "The Empire Strikes Back": "Империя наносит ответный удар",
    "Return of the Jedi": "Возвращение джедая",
    "The Phantom Menace": "Скрытая угроза",
    "Attack of the Clones": "Атака клонов",
    "Revenge of the Sith": "Месть ситхов",
    "The Force Awakens": "Пробуждение силы",

    "Star Wars: Episode I - The Phantom Menace": "Звёздные войны: Эпизод I — Скрытая угроза",
    "Star Wars: Episode II - Attack of the Clones": "Звёздные войны: Эпизод II — Атака клонов",
    "Star Wars: Episode III - Revenge of the Sith": "Звёздные войны: Эпизод III — Месть ситхов",
    "Star Wars: Episode IV - A New Hope": "Звёздные войны: Эпизод IV — Новая надежда",
    "Star Wars: Episode V - The Empire Strikes Back": "Звёздные войны: Эпизод V — Империя наносит ответный удар",
    "Star Wars: Episode VI - Return of the Jedi": "Звёздные войны: Эпизод VI — Возвращение джедая",
    "Star Wars: Episode VII - The Force Awakens": "Звёздные войны: Эпизод VII — Пробуждение силы",
}

SPECIES_RU = {
    "Human": "Человек",
    "Droid": "Дроид",
    "Wookiee": "Вуки",
    "Rodian": "Родианец",
    "Hutt": "Хатт",
    "Yoda's species": "Вид Йоды",
    "Trandoshan": "Трандошанин",
    "Mon Calamari": "Мон-Каламари",
    "Ewok": "Эвок",
    "Sullustan": "Саллустанин",
    "Neimodian": "Неймодианец",
    "Gungan": "Гунган",
    "Toydarian": "Тойдарианец",
    "Dug": "Даг",
    "Zabrak": "Забрак",
    "Twi'lek": "Тви'лек",
    "Aleena": "Алина",
    "Vulptereen": "Вулптеррианец",
    "Xexto": "Ксексто",
    "Toong": "Тунг",
    "Cerean": "Цереанин",
    "Nautolan": "Наутоланин",
    "Zabrak (Dathomirian)": "Забрак (Датомирец)",
    "Tholothian": "Толотианин",
    "Iktotchi": "Иктотчи",
    "Quermian": "Квермианин",
    "Kel Dor": "Кел Дор",
    "Chagrian": "Чагрианин",
    "Geonosian": "Джеонозианец",
    "Mirialan": "Миралианин",
    "Clawdite": "Клодит",
    "Besalisk": "Безалиск",
    "Kaminoan": "Каминоанец",
    "Skakoan": "Скакоанец",
    "Muun": "Муун",
    "Togruta": "Тогрута",
    "Kaleesh": "Калиш",
    "Pau'an": "Пау'ан",
}

STARSHIPS_RU = {
    "CR90 corvette": "Корвет CR90",
    "Star Destroyer": "Звёздный разрушитель",
    "Sentinel-class landing craft": "Десантный корабль класса «Страж»",
    "Death Star": "Звезда Смерти",
    "Millennium Falcon": "Тысячелетний сокол",
    "Y-wing": "Y-wing",
    "X-wing": "X-wing",
    "TIE Advanced x1": "TIE Advanced x1",
    "Executor": "«Экзекутор»",
    "Rebel transport": "Транспорт повстанцев",
    "Slave 1": "«Слейв-1»",
    "Imperial shuttle": "Имперский шаттл",
    "EF76 Nebulon-B escort frigate": "Фрегат сопровождения EF76 «Небулон-Б»",
    "Calamari Cruiser": "Каламарианский крейсер",
    "A-wing": "A-wing",
    "B-wing": "B-wing",
    "Republic Cruiser": "Крейсер Республики",
    "Droid control ship": "Корабль управления дроидами",
    "Naboo fighter": "Набуанский истребитель",
    "Naboo Royal Starship": "Набуанский королевский звездолёт",
    "Scimitar": "«Скимитар»",
    "J-type diplomatic barge": "Дипломатическая баржа типа J",
    "AA-9 Coruscant freighter": "Корусантский грузовик AA-9",
    "Jedi starfighter": "Истребитель джедаев",
    "H-type Nubian yacht": "Нубианская яхта типа H",
    "Republic Assault ship": "Штурмовой корабль Республики",
    "Solar Sailer": "Солнечный парусник",
    "Trade Federation cruiser": "Крейсер Торговой федерации",
    "Theta-class T-2c shuttle": "Шаттл «Тета»-класса T-2c",
    "T-70 X-wing fighter": "Истребитель T-70 X-wing",
}


def translate(name, resource="people"):
    maps = {
        "people": PEOPLE_RU,
        "planets": PLANETS_RU,
        "films": FILMS_RU,
        "species": SPECIES_RU,
        "starships": STARSHIPS_RU,
    }
    return maps.get(resource, {}).get(name, name)


def translate_or_none(name, resource="people"):
    maps = {
        "people": PEOPLE_RU,
        "planets": PLANETS_RU,
        "films": FILMS_RU,
        "species": SPECIES_RU,
        "starships": STARSHIPS_RU,
    }
    return maps.get(resource, {}).get(name)

# ============================================================
# Переводы полей: цвет волос/кожи/глаз, пол, год рождения
# ============================================================

COLORS_RU = {
    # --- Цвета волос ---
    "blond": "блонд",
    "blonde": "блонд",
    "brown": "каштановый",
    "black": "чёрный",
    "white": "белый",
    "red": "рыжий",
    "auburn": "тёмно-рыжий",
    "grey": "серый",
    "gray": "серый",
    "green": "зелёный",
    "blue": "синий",
    "gold": "золотой",
    "yellow": "жёлтый",
    "orange": "оранжевый",
    "purple": "фиолетовый",
    "pink": "розовый",
    "silver": "серебряный",
    "fair": "светлый",
    "light": "светлый",
    "dark": "тёмный",
    "tan": "загорелый",
    "pale": "бледный",
    "none": "нет",
    "n/a": "н/д",
    "unknown": "неизвестно",
    "bald": "лысый",
    # --- Комбинированные значения (через запятую) ---
    "brown, grey": "каштановый, серый",
    "brown, white": "каштановый, белый",
    "black, brown": "чёрный, каштановый",
    "blond, brown": "блонд, каштановый",
    "white, blue": "белый, синий",
    "red, blue, white": "красный, синий, белый",
    "red, blue": "красный, синий",
    "red, green": "красный, зелёный",
    "green, yellow": "зелёный, жёлтый",
    "blue, grey": "синий, серый",
    "brown, black": "каштановый, чёрный",
    "grey, blue": "серый, синий",
    "green, grey": "зелёный, серый",
    "pale, white": "бледный, белый",
    "fair, green": "светлый, зелёный",
    "light, brown": "светлый, каштановый",
    "dark, brown": "тёмный, каштановый",
}

GENDERS_RU = {
    "male": "мужской",
    "female": "женский",
    "hermaphrodite": "гермафродит",
    "none": "нет",
    "n/a": "н/д",
    "unknown": "неизвестно",
}

CLIMATE_RU = {
    "temperate": "умеренный",
    "tropical": "тропический",
    "arid": "засушливый",
    "frozen": "ледяной",
    "frigid": "холодный",
    "hot": "жаркий",
    "humid": "влажный",
    "windy": "ветреный",
    "polluted": "загрязнённый",
    "dry": "сухой",
    "subarctic": "субарктический",
    "arctic": "арктический",
    "superheated": "раскалённый",
    "unknown": "неизвестно",
    "n/a": "н/д",
    "temperate, tropical": "умеренный, тропический",
    "temperate, arid": "умеренный, засушливый",
    "frozen, arid": "ледяной, засушливый",
    "tropical, arid": "тропический, засушливый",
    "frigid, arid": "холодный, засушливый",
    "temperate, frozen": "умеренный, ледяной",
    "arid, temperate": "засушливый, умеренный",
}

TERRAIN_RU = {
    "desert": "пустыня",
    "grasslands": "луга",
    "mountains": "горы",
    "mountain": "горы",
    "jungle": "джунгли",
    "jungles": "джунгли",
    "rainforests": "тропические леса",
    "forests": "леса",
    "forest": "лес",
    "ocean": "океан",
    "oceans": "океаны",
    "tundra": "тундра",
    "ice caves": "ледяные пещеры",
    "rocky islands": "скалистые острова",
    "islands": "острова",
    "volcanoes": "вулканы",
    "volcanic": "вулканическая",
    "swamp": "болото",
    "swamps": "болота",
    "cityscape": "городской ландшафт",
    "urban": "городская",
    "barren": "бесплодная",
    "scrublands": "кустарники",
    "savanna": "саванна",
    "canyons": "каньоны",
    "caves": "пещеры",
    "salt flats": "соляные равнины",
    "lakes": "озёра",
    "rivers": "реки",
    "grassy hills": "травянистые холмы",
    "hills": "холмы",
    "plains": "равнины",
    "rocky": "скалистая",
    "gas giant": "газовый гигант",
    "unknown": "неизвестно",
    "n/a": "н/д",
    "desert, mountains": "пустыня, горы",
    "desert, rocky": "пустыня, скалы",
    "jungle, rainforests": "джунгли, тропические леса",
    "forests, mountains, lakes": "леса, горы, озёра",
    "mountains, volcanoes, canyons": "горы, вулканы, каньоны",
    "ocean, islands": "океан, острова",
    "grassy hills, swamps, forests, mountains": "травянистые холмы, болота, леса, горы",
    "cityscape, mountains": "городской ландшафт, горы",
    "tundra, ice caves, mountain ranges": "тундра, ледяные пещеры, горные хребты",
    "scrublands, savanna, canyons, barren": "кустарники, саванна, каньоны, бесплодная",
    "rocky islands, oceans": "скалистые острова, океаны",
}


def translate_climate(value):
    if not value:
        return "—"
    v = value.strip()
    if v in CLIMATE_RU:
        return CLIMATE_RU[v]
    parts = [p.strip() for p in v.split(",")]
    return ", ".join(CLIMATE_RU.get(p, p) for p in parts)


def translate_terrain(value):
    if not value:
        return "—"
    v = value.strip()
    if v in TERRAIN_RU:
        return TERRAIN_RU[v]
    parts = [p.strip() for p in v.split(",")]
    return ", ".join(TERRAIN_RU.get(p, p) for p in parts)


def translate_color(value):
    """Переводит цвет; умеет обрабатывать списки через запятую."""
    if not value or value in ("n/a", "unknown", "none", ""):
        return COLORS_RU.get(value, value)
    value = value.strip()
    # Если точное совпадение — отдаём сразу
    if value in COLORS_RU:
        return COLORS_RU[value]
    # Иначе разбиваем по запятой и переводим каждую часть
    parts = [p.strip() for p in value.split(",")]
    return ", ".join(COLORS_RU.get(p, p) for p in parts)


def translate_gender(value):
    """Переводит пол."""
    if not value:
        return "—"
    return GENDERS_RU.get(value.strip().lower(), value)


def translate_birth_year(value):
    """
    Расшифровывает формат SWAPI:
      44BBY  -> 44 г. до Явина
      19BBY  -> 19 г. до Явина
      112BBY -> 112 г. до Явина
      896BBY -> 896 г. до Явина
      19ABY  -> 19 г. после Явина
      unknown / n/a -> неизвестно / н/д
    """
    if not value:
        return "—"
    v = str(value).strip()
    if v.lower() in ("unknown", "n/a", "none", ""):
        return {"unknown": "неизвестно", "n/a": "н/д", "none": "нет"}.get(v.lower(), v)
    if v.upper().endswith("BBY"):
        num = v[:-3].strip()
        return f"{num} г. до Явина"
    if v.upper().endswith("ABY"):
        num = v[:-3].strip()
        return f"{num} г. после Явина"
    return v


def translate_measure(value, unit=""):
    """Для роста/массы: 'unknown'/'n/a' -> 'неизвестно'/'н/д'."""
    if not value:
        return "—"
    v = str(value).strip()
    low = v.lower()
    if low in ("unknown", "n/a", "none", ""):
        return {"unknown": "неизвестно", "n/a": "н/д", "none": "нет"}.get(low, v)
    return f"{v}{(' ' + unit) if unit else ''}"
