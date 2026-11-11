class BaseModel:
    def __init__(self, data):
        self._data = data
        self.url = data.get("url", "")

    def __str__(self):
        return self._data.get("name") or self._data.get("title") or "Unknown"


class Person(BaseModel):
    @property
    def name(self): return self._data.get("name", "—")
    @property
    def height(self): return self._data.get("height", "—")
    @property
    def mass(self): return self._data.get("mass", "—")
    @property
    def hair_color(self): return self._data.get("hair_color", "—")
    @property
    def skin_color(self): return self._data.get("skin_color", "—")
    @property
    def eye_color(self): return self._data.get("eye_color", "—")
    @property
    def birth_year(self): return self._data.get("birth_year", "—")
    @property
    def gender(self): return self._data.get("gender", "—")
    @property
    def homeworld_url(self): return self._data.get("homeworld")
    @property
    def film_urls(self): return self._data.get("films", [])
    @property
    def species_urls(self): return self._data.get("species", [])
    @property
    def starship_urls(self): return self._data.get("starships", [])
    @property
    def vehicle_urls(self): return self._data.get("vehicles", [])


class Planet(BaseModel):
    @property
    def name(self): return self._data.get("name", "—")
    @property
    def diameter(self): return self._data.get("diameter", "—")
    @property
    def rotation_period(self): return self._data.get("rotation_period", "—")
    @property
    def orbital_period(self): return self._data.get("orbital_period", "—")
    @property
    def gravity(self): return self._data.get("gravity", "—")
    @property
    def population(self): return self._data.get("population", "—")
    @property
    def climate(self): return self._data.get("climate", "—")
    @property
    def terrain(self): return self._data.get("terrain", "—")
    @property
    def surface_water(self): return self._data.get("surface_water", "—")
    @property
    def resident_urls(self): return self._data.get("residents", [])
    @property
    def film_urls(self): return self._data.get("films", [])


class Film(BaseModel):
    @property
    def title(self): return self._data.get("title", "—")
    @property
    def episode_id(self): return self._data.get("episode_id", "—")
    @property
    def director(self): return self._data.get("director", "—")
    @property
    def producer(self): return self._data.get("producer", "—")
    @property
    def release_date(self): return self._data.get("release_date", "—")
    @property
    def opening_crawl(self): return self._data.get("opening_crawl", "—")
    @property
    def character_urls(self): return self._data.get("characters", [])
    @property
    def planet_urls(self): return self._data.get("planets", [])
    @property
    def starship_urls(self): return self._data.get("starships", [])
    @property
    def vehicle_urls(self): return self._data.get("vehicles", [])
    @property
    def species_urls(self): return self._data.get("species", [])


class Starship(BaseModel):
    @property
    def name(self): return self._data.get("name", "—")
    @property
    def model(self): return self._data.get("model", "—")
    @property
    def manufacturer(self): return self._data.get("manufacturer", "—")
    @property
    def cost_in_credits(self): return self._data.get("cost_in_credits", "—")
    @property
    def length(self): return self._data.get("length", "—")
    @property
    def max_atmosphering_speed(self): return self._data.get("max_atmosphering_speed", "—")
    @property
    def crew(self): return self._data.get("crew", "—")
    @property
    def passengers(self): return self._data.get("passengers", "—")
    @property
    def cargo_capacity(self): return self._data.get("cargo_capacity", "—")
    @property
    def consumables(self): return self._data.get("consumables", "—")
    @property
    def hyperdrive_rating(self): return self._data.get("hyperdrive_rating", "—")
    @property
    def starship_class(self): return self._data.get("starship_class", "—")
    @property
    def pilot_urls(self): return self._data.get("pilots", [])
    @property
    def film_urls(self): return self._data.get("films", [])


class Species(BaseModel):
    @property
    def name(self): return self._data.get("name", "—")
    @property
    def classification(self): return self._data.get("classification", "—")
    @property
    def designation(self): return self._data.get("designation", "—")
    @property
    def average_height(self): return self._data.get("average_height", "—")
    @property
    def average_lifespan(self): return self._data.get("average_lifespan", "—")
    @property
    def language(self): return self._data.get("language", "—")
    @property
    def homeworld_url(self): return self._data.get("homeworld")
    @property
    def people_urls(self): return self._data.get("people", [])
    @property
    def film_urls(self): return self._data.get("films", [])
